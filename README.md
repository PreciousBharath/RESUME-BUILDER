# ResumePro — Resume Builder

Build a polished, role-focused resume with a simple Flask web application. ResumePro lets users enter their career details, preview different resume styles, generate a professional summary from their inputs, and export the finished resume as PDF or editable Word (DOCX).

## Features

- **Account flow:** registration, login, and logout.
- **Resume editor:** capture contact details, target role, skills, education, experience, projects, certifications, languages, achievements, LinkedIn, and portfolio links.
- **Generated professional summary:** creates a role- and experience-level-based summary using the user's role, experience level, skills, and career goal.
- **Three resume styles:** Classic, Modern, and Creative.
- **Custom appearance:** choose blue, purple, green, or orange accents.
- **Profile photo:** upload an optional photo and control whether it appears in the exported resume.
- **Live preview and progress feedback:** review your resume while editing and track form completion.
- **Export to PDF or DOCX:** create a shareable PDF or an editable Word document.
- **Resume history:** reopen, edit, download, and delete previously generated resumes.
- **Career resources:** access resume-writing tips and a career toolkit.
- **Responsive interface:** HTML, CSS, and JavaScript with a modern, mobile-aware layout.

## Technology Stack

| Layer | Technologies |
| --- | --- |
| Backend | Python, Flask |
| Frontend | HTML5, CSS3, Vanilla JavaScript |
| Resume documents | ReportLab (PDF), python-docx (DOCX) |
| UI assets | Font Awesome, Google Fonts (Poppins) |
| Local persistence | JSON files for user and resume records |

## Screenshots

No verified application screenshots are currently available in the repository. To keep this README authentic, screenshots have not been fabricated or replaced with unrelated images.

When you capture screenshots of the running application, add them to `docs/screenshots/` and update this section. Useful screenshots include:

- Landing / login page
- Resume editor with live preview and template controls
- Classic, Modern, and Creative resume examples
- Resume history and dashboard

Example Markdown once real screenshots are added:

```md
![Resume editor](docs/screenshots/resume-editor.png)
```

## Getting Started

### Requirements

- Python 3.10 or later recommended
- pip
- A modern web browser

The project pins its Python packages in `requirements.txt`.

### 1. Clone the repository

```bash
git clone https://github.com/PreciousBharath/RESUME-BUILDER.git
cd RESUME-BUILDER
```

### 2. Create and activate a virtual environment

**Windows (PowerShell):**

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

**Windows (Command Prompt):**

```bat
python -m venv .venv
.venv\Scripts\activate.bat
```

**macOS / Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Configure the Flask secret key

Set a unique secret key in your terminal before running the app.

**Windows PowerShell:**

```powershell
$env:SECRET_KEY = "replace-with-a-long-random-secret"
```

**Windows Command Prompt:**

```bat
set SECRET_KEY=replace-with-a-long-random-secret
```

**macOS / Linux:**

```bash
export SECRET_KEY="replace-with-a-long-random-secret"
```

### 5. Start the application

```bash
python app.py
```

Open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser. Register an account, sign in, and start creating a resume.

The repository also includes `setup.bat` and `setup.sh` helper scripts; review them before running them.

## How to Use

1. Open the application and create an account.
2. Sign in and open the resume builder.
3. Enter your contact information, target role, experience level, skills, education, experience, and career goal.
4. Add optional details such as a profile photo, projects, certifications, achievements, languages, LinkedIn, and portfolio links.
5. Select Classic, Modern, or Creative; choose an accent color and photo preference.
6. Review the generated professional summary and resume preview.
7. Choose PDF or DOCX and generate your resume.
8. Revisit the dashboard or history page to edit, download, or delete saved resumes.

## Project Structure

```text
RESUME-BUILDER/
├── app.py                    # Flask routes, login, resume workflow and history
├── config.py                 # App settings and validation configuration
├── prompt_engine.py           # Professional summary generation
├── create_resume.py           # PDF and DOCX generation
├── requirements.txt           # Python dependencies
├── setup.bat                  # Windows setup helper
├── setup.sh                   # macOS/Linux setup helper
├── templates/
│   ├── index.html             # Login page
│   ├── register.html          # Registration page
│   ├── create_resume.html     # Resume editor
│   ├── dashboard.html         # Dashboard and style selection
│   ├── history.html           # Saved resume management
│   ├── tips.html              # Resume-writing tips
│   └── toolkit.html           # Career toolkit
├── static/
│   ├── css/style.css          # Application styling
│   ├── js/app.js              # Client-side interactions
│   ├── images/                # Static images
│   ├── img/                   # Placeholder images
│   └── uploads/               # Uploaded photos and generated files
├── tests/                     # Automated tests
├── users.json                 # Local account records
└── resumes.json               # Local resume records
```

## Tests

Test files are provided under `tests/`. Install the project requirements, then run:

```bash
python -m unittest discover -s tests -v
```

Review individual test files for their coverage and any additional test-specific dependencies.

## Security and Deployment Notes

This repository is currently best treated as a **local learning / development project**, not a production-ready service. Before deploying it publicly:

- Replace the fallback Flask secret key with a securely managed environment variable and disable debug mode.
- Passwords are currently stored as plain text in `users.json`; use a suitable password-hashing method and consider a proper user database.
- Do not commit real user records, resumes, profile photos, or generated documents. The tracked JSON files and upload folders may contain personal data; remove private data from version control and add appropriate ignore rules.
- Add server-side validation and file size/type checks for uploaded images.
- Add CSRF protection, secure session-cookie settings, and production-grade error handling.
- Review the authentication, file access, and data-retention approach before hosting the application.

Do not put real passwords, personal resumes, or other sensitive information into a public repository.

## Documentation

- [Getting Started](GETTING_STARTED.md)
- [Project Summary](PROJECT_SUMMARY.md)
- [File Structure](FILE_STRUCTURE.md)
- [Upgrade Notes](UPGRADES.md)

## Future Improvements

- Store accounts and resume records in a database.
- Hash passwords and add password reset flows.
- Add more export themes and improve accessibility.
- Add automated tests for registration, authentication, resume export, and access control.
- Add genuine screenshots and a short demo video.
- Prepare a production deployment configuration.

## Author

**PreciousBharath**  
GitHub: [github.com/PreciousBharath](https://github.com/PreciousBharath)

---

*Built with Python, Flask, and a focus on helping people present their skills and experience clearly.*
