import json
import os
import uuid
from datetime import datetime
from functools import wraps

from flask import Flask, abort, flash, redirect, render_template, request, send_file, session, url_for
from werkzeug.utils import secure_filename

from create_resume import generate_resume_docx, generate_resume_pdf
from prompt_engine import generate_summary

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, "static", "uploads")
USERS_FILE = os.path.join(BASE_DIR, "users.json")
RESUMES_FILE = os.path.join(BASE_DIR, "resumes.json")

app = Flask(__name__, static_folder="static", template_folder="templates")
app.secret_key = os.environ.get("SECRET_KEY", "resume_builder_secret_2026")
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def ensure_users_file():
    if not os.path.exists(USERS_FILE):
        with open(USERS_FILE, "w", encoding="utf-8") as f:
            json.dump({}, f)


def ensure_resumes_file():
    if not os.path.exists(RESUMES_FILE):
        with open(RESUMES_FILE, "w", encoding="utf-8") as f:
            json.dump({}, f)


def load_users():
    ensure_users_file()
    with open(USERS_FILE, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except ValueError:
            return {}


def save_users(users):
    with open(USERS_FILE, "w", encoding="utf-8") as f:
        json.dump(users, f, indent=2)


def load_resume_store():
    ensure_resumes_file()
    with open(RESUMES_FILE, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except ValueError:
            return {}


def save_resume_store(store):
    with open(RESUMES_FILE, "w", encoding="utf-8") as f:
        json.dump(store, f, indent=2)


def load_resume_history(user_email):
    store = load_resume_store()
    records = [record for record in store.values() if record.get("user_email") == user_email]
    return sorted(records, key=lambda item: item.get("created_at", ""), reverse=True)


def save_resume_record(user_email, data, file_path, download_name):
    store = load_resume_store()
    record_id = str(uuid.uuid4())[:8]
    record = {
        "id": record_id,
        "user_email": user_email,
        "name": data.get("name", "Untitled Resume"),
        "role": data.get("role", ""),
        "template": data.get("template", 1),
        "accent_color": data.get("accent_color", "blue"),
        "format": data.get("format", "docx"),
        "download_name": download_name,
        "file_path": file_path,
        "created_at": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"),
        "updated_at": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"),
        "data": data,
    }
    store[record_id] = record
    save_resume_store(store)
    return record


def update_resume_record(user_email, record_id, data, file_path=None, download_name=None):
    store = load_resume_store()
    record = store.get(record_id)
    if not record or record.get("user_email") != user_email:
        return None

    record.update(
        {
            "name": data.get("name", record.get("name", "Untitled Resume")),
            "role": data.get("role", ""),
            "template": data.get("template", record.get("template", 1)),
            "accent_color": data.get("accent_color", record.get("accent_color", "blue")),
            "format": data.get("format", record.get("format", "docx")),
            "updated_at": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"),
            "data": data,
        }
    )
    if file_path:
        record["file_path"] = file_path
    if download_name:
        record["download_name"] = download_name
    store[record_id] = record
    save_resume_store(store)
    return record


def get_resume_record(user_email, record_id):
    store = load_resume_store()
    record = store.get(record_id)
    if not record or record.get("user_email") != user_email:
        return None
    return record


def delete_resume_record(user_email, record_id):
    store = load_resume_store()
    record = store.get(record_id)
    if not record or record.get("user_email") != user_email:
        return False

    file_path = record.get("file_path")
    if file_path and os.path.exists(file_path):
        try:
            os.remove(file_path)
        except OSError:
            pass

    del store[record_id]
    save_resume_store(store)
    return True


def save_resume_artifact(user_email, data, buffer, download_name, file_format):
    safe_name = secure_filename(data.get("name") or "resume") or "resume"
    folder = os.path.join(app.config["UPLOAD_FOLDER"], "history", secure_filename(user_email.lower()) or "user")
    os.makedirs(folder, exist_ok=True)
    file_path = os.path.join(folder, f"{safe_name}_{datetime.utcnow().strftime('%Y%m%d%H%M%S')}.{file_format}")
    with open(file_path, "wb") as handle:
        handle.write(buffer.getvalue())
    return file_path


def login_required(view):
    @wraps(view)
    def wrapped(*args, **kwargs):
        if "user" not in session:
            flash("Please log in to continue.", "warning")
            return redirect(url_for("login"))
        return view(*args, **kwargs)

    return wrapped


@app.route("/")
def index():
    if "user" in session:
        return redirect(url_for("create"))
    return redirect(url_for("login"))


@app.route("/login", methods=["GET", "POST"])
def login():
    if "user" in session:
        return redirect(url_for("create"))

    error = None
    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")
        users = load_users()
        user = users.get(email)
        if user and user.get("password") == password:
            session["user"] = {"email": email, "name": user.get("name", email)}
            session["welcome_message"] = "WELCOME TO RESUME BUILDER"
            flash("WELCOME TO RESUME BUILDER", "success")
            return redirect(url_for("create"))
        error = "Invalid email or password."

    return render_template("index.html", error=error)


@app.route("/register", methods=["GET", "POST"])
def register():
    if "user" in session:
        return redirect(url_for("create"))

    error = None
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")
        confirm_password = request.form.get("confirm_password", "")

        if not name or not email or not password:
            error = "Please complete all required fields."
        elif "@" not in email:
            error = "Please enter a valid email address."
        elif password != confirm_password:
            error = "Passwords do not match."
        else:
            users = load_users()
            if email in users:
                error = "This email is already registered."
            else:
                users[email] = {"name": name, "password": password}
                save_users(users)
                flash("Account created successfully. Please log in.", "success")
                return redirect(url_for("login"))

    return render_template("register.html", error=error)


@app.route("/logout")
def logout():
    session.pop("user", None)
    flash("You have been logged out.", "info")
    return redirect(url_for("login"))


@app.route("/toolkit")
def toolkit():
    return render_template("toolkit.html", user=session.get("user"))


@app.route("/tips")
def tips():
    return render_template("tips.html", user=session.get("user"))


@app.route("/dashboard", methods=["GET", "POST"])
@login_required
def dashboard():
    if request.method == "POST":
        session["selected_style"] = {
            "template": request.form.get("template", "1"),
            "accent": request.form.get("accent", "blue"),
        }
        flash("Dashboard style updated.", "success")
        return redirect(url_for("dashboard"))

    selected_style = session.get("selected_style", {"template": "1", "accent": "blue"})
    resumes = load_resume_history(session.get("user", {}).get("email", ""))
    return render_template("dashboard.html", user=session.get("user"), resumes=resumes, selected_style=selected_style)


@app.route("/history")
@login_required
def history():
    resumes = load_resume_history(session.get("user", {}).get("email", ""))
    return render_template("history.html", user=session.get("user"), resumes=resumes)


@app.route("/resume/<record_id>/download")
@login_required
def download_resume(record_id):
    record = get_resume_record(session.get("user", {}).get("email", ""), record_id)
    if not record:
        abort(404)
    if not record.get("file_path") or not os.path.exists(record["file_path"]):
        flash("The saved resume file could not be found.", "warning")
        return redirect(url_for("history"))

    return send_file(
        record["file_path"],
        as_attachment=True,
        download_name=record.get("download_name", "resume.docx"),
        mimetype="application/pdf" if record.get("format") == "pdf" else "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    )


@app.route("/resume/<record_id>/delete", methods=["POST"])
@login_required
def delete_resume(record_id):
    deleted = delete_resume_record(session.get("user", {}).get("email", ""), record_id)
    if deleted:
        flash("Resume deleted successfully.", "success")
    else:
        flash("Unable to delete the selected resume.", "warning")
    return redirect(url_for("history"))


@app.route("/resume/<record_id>/edit", methods=["GET", "POST"])
@login_required
def edit_resume(record_id):
    user = session.get("user", {})
    record = get_resume_record(user.get("email", ""), record_id)
    if not record:
        abort(404)

    if request.method == "POST":
        form = request.form
        file = request.files.get("photo")
        photo_path = None
        existing_data = record.get("data", {})
        existing_photo = existing_data.get("photo")

        if file and file.filename:
            filename = secure_filename(file.filename)
            photo_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            file.save(photo_path)
        elif existing_photo and os.path.exists(existing_photo):
            photo_path = existing_photo

        summary = generate_summary(
            form.get("role", ""),
            form.get("experience_level", ""),
            form.get("skills", ""),
            form.get("goal", "")
        )

        data = {
            "name": form.get("name", ""),
            "email": form.get("email", ""),
            "phone": form.get("phone", ""),
            "role": form.get("role", ""),
            "summary": summary,
            "skills": form.get("skills", ""),
            "education": form.get("education", ""),
            "experience": form.get("experience", ""),
            "goal": form.get("goal", ""),
            "linkedin": form.get("linkedin", ""),
            "portfolio": form.get("portfolio", ""),
            "certifications": form.get("certifications", ""),
            "projects": form.get("projects", ""),
            "languages": form.get("languages", ""),
            "achievements": form.get("achievements", ""),
            "photo": photo_path,
            "template": int(form.get("template", record.get("template", 1))),
            "accent_color": form.get("accent_color", record.get("accent_color", "blue")),
            "show_photo": bool(form.get("show_photo")),
            "format": form.get("format", record.get("format", "docx")).lower(),
        }

        template = data["template"]
        file_format = data["format"]
        try:
            if file_format == "pdf":
                buffer = generate_resume_pdf(data, template)
                download_name = f"{data['name'] or 'resume'}_Resume.pdf"
                mimetype = "application/pdf"
            else:
                buffer = generate_resume_docx(data, template)
                download_name = f"{data['name'] or 'resume'}_Resume.docx"
                mimetype = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"

            file_path = save_resume_artifact(user.get("email", ""), data, buffer, download_name, file_format)
            update_resume_record(user.get("email", ""), record_id, data, file_path=file_path, download_name=download_name)
            flash("Resume updated successfully.", "success")
            return redirect(url_for("history"))
        except Exception as exc:
            return f"Error updating resume: {str(exc)}", 500

    resume_data = record.get("data", {})
    welcome_message = session.pop("welcome_message", None)
    return render_template("create_resume.html", user=user, resume_data=resume_data, editing_record=record, welcome_message=welcome_message)


@app.route("/create", methods=["GET", "POST"])
@login_required
def create():
    if request.method == "POST":
        form = request.form
        file = request.files.get("photo")
        photo_path = None
        if file and file.filename:
            filename = secure_filename(file.filename)
            photo_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            file.save(photo_path)

        summary = generate_summary(
            form.get("role", ""),
            form.get("experience_level", ""),
            form.get("skills", ""),
            form.get("goal", "")
        )

        data = {
            "name": form.get("name", ""),
            "email": form.get("email", ""),
            "phone": form.get("phone", ""),
            "role": form.get("role", ""),
            "summary": summary,
            "skills": form.get("skills", ""),
            "education": form.get("education", ""),
            "experience": form.get("experience", ""),
            "goal": form.get("goal", ""),
            "linkedin": form.get("linkedin", ""),
            "portfolio": form.get("portfolio", ""),
            "certifications": form.get("certifications", ""),
            "projects": form.get("projects", ""),
            "languages": form.get("languages", ""),
            "achievements": form.get("achievements", ""),
            "photo": photo_path,
            "template": int(form.get("template", 1)),
            "accent_color": form.get("accent_color", "blue"),
            "show_photo": bool(form.get("show_photo")),
            "format": form.get("format", "docx").lower(),
        }

        template = data["template"]
        file_format = data["format"]
        user_email = session.get("user", {}).get("email", "")

        try:
            if file_format == "pdf":
                buffer = generate_resume_pdf(data, template)
                download_name = f"{data['name'] or 'resume'}_Resume.pdf"
                mimetype = "application/pdf"
            else:
                buffer = generate_resume_docx(data, template)
                download_name = f"{data['name'] or 'resume'}_Resume.docx"
                mimetype = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"

            file_path = save_resume_artifact(user_email, data, buffer, download_name, file_format)
            save_resume_record(user_email, data, file_path, download_name)
            flash("Resume exported successfully.", "success")
            return send_file(
                file_path,
                as_attachment=True,
                download_name=download_name,
                mimetype=mimetype,
            )
        except Exception as exc:
            return f"Error generating resume: {str(exc)}", 500

    welcome_message = session.pop("welcome_message", None)
    return render_template("create_resume.html", user=session.get("user"), resume_data=None, welcome_message=welcome_message)


if __name__ == "__main__":
    app.run(debug=True)
