function showToast(message, type = "success") {
    const toast = document.createElement("div");
    toast.className = `toast toast-${type}`;
    toast.textContent = message;
    document.body.appendChild(toast);

    requestAnimationFrame(() => toast.classList.add("visible"));
    setTimeout(() => toast.classList.remove("visible"), 3500);
    setTimeout(() => toast.remove(), 4200);
}

function showExportPopup() {
    const overlay = document.getElementById("exportOverlay");
    if (!overlay) return;
    overlay.classList.add("visible");
    overlay.setAttribute("aria-hidden", "false");

    const audioContext = window.AudioContext || window.webkitAudioContext;
    if (audioContext) {
        const ctx = new audioContext();
        const oscillator = ctx.createOscillator();
        const gain = ctx.createGain();
        oscillator.type = "triangle";
        oscillator.frequency.setValueAtTime(880, ctx.currentTime);
        oscillator.frequency.exponentialRampToValueAtTime(1320, ctx.currentTime + 0.15);
        gain.gain.setValueAtTime(0.08, ctx.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.0001, ctx.currentTime + 0.35);
        oscillator.connect(gain);
        gain.connect(ctx.destination);
        oscillator.start();
        oscillator.stop(ctx.currentTime + 0.35);
        setTimeout(() => ctx.close(), 400);
    }

    setTimeout(() => {
        overlay.classList.remove("visible");
        overlay.setAttribute("aria-hidden", "true");
    }, 2200);
}

function updatePreview() {
    const fields = {
        name: "Your Name",
        role: "Professional Title",
        email: "email@example.com",
        phone: "+1 (555) 000-0000",
        skills: "Python, JavaScript, React",
        education: "Bachelor of Science in Computer Science",
        experience: "Designed and delivered feature-rich web applications.",
        goal: "A motivated professional ready to contribute to your team.",
        linkedin: "linkedin.com/in/yourname",
        portfolio: "yourportfolio.com",
        certifications: "AWS Cloud Practitioner",
        projects: "Built a customer dashboard with React and Python",
        languages: "English, Hindi",
        achievements: "Increased adoption by 25%"
    };

    Object.keys(fields).forEach(key => {
        const input = document.getElementById(key);
        const value = input && input.value.trim() ? input.value.trim() : fields[key];
        const preview = document.getElementById(`preview_${key}`);
        if (preview) preview.textContent = value;
    });

    const accentSelect = document.getElementById("accent_color");
    const previewCard = document.getElementById("previewCard");
    if (previewCard && accentSelect) {
        previewCard.dataset.accent = accentSelect.value;
    }

    const photoInput = document.getElementById("photo");
    const photoPreview = document.getElementById("preview_photo");
    const showPhotoInput = document.getElementById("show_photo");
    const shouldShowPhoto = !showPhotoInput || showPhotoInput.checked;

    if (photoInput && photoInput.files && photoInput.files[0] && shouldShowPhoto) {
        const reader = new FileReader();
        reader.onload = e => {
            photoPreview.style.backgroundImage = `url('${e.target.result}')`;
            photoPreview.textContent = "";
        };
        reader.readAsDataURL(photoInput.files[0]);
    } else if (shouldShowPhoto) {
        photoPreview.style.backgroundImage = "none";
        photoPreview.textContent = "Photo";
    } else {
        photoPreview.style.backgroundImage = "none";
        photoPreview.textContent = "Photo hidden";
    }
}

function setupResumePage() {
    const form = document.getElementById("resumeForm");
    const templateButtons = document.querySelectorAll(".template-button");
    const themeToggle = document.getElementById("themeToggle");
    const previewCard = document.getElementById("previewCard");
    const templateInput = document.getElementById("template");

    if (!form) return;

    form.addEventListener("submit", () => {
        showExportPopup();
    });

    const initialTemplate = templateInput && templateInput.value ? parseInt(templateInput.value, 10) : 1;
    if (previewCard && templateInput) {
        switchTemplate(initialTemplate.toString(), previewCard, templateInput, templateButtons, Array.from(templateButtons).find(btn => btn.dataset.template === initialTemplate.toString()) || templateButtons[0]);
    }

    document.querySelectorAll("#resumeForm input, #resumeForm textarea, #resumeForm select").forEach(el => {
        el.addEventListener("input", updatePreview);
        el.addEventListener("change", updatePreview);
    });

    templateButtons.forEach(button => {
        button.addEventListener("click", () => {
            const index = button.dataset.template;
            switchTemplate(index, previewCard, templateInput, templateButtons, button);
        });
    });

    initThemeToggle();
    updatePreview();
}

function switchTemplate(index, previewCard, templateInput, templateButtons, currentButton) {
    templateInput.value = index;
    previewCard.classList.remove("template-1", "template-2", "template-3");
    previewCard.classList.add(`template-${index}`);
    templateButtons.forEach(btn => btn.classList.toggle("active", btn === currentButton));
}

function initThemeToggle() {
    const themeToggle = document.getElementById("themeToggle");
    if (!themeToggle) return;

    themeToggle.addEventListener("click", () => {
        const activeTheme = document.documentElement.classList.toggle("theme-dark") ? "dark" : "light";
        themeToggle.textContent = activeTheme === "dark" ? "Light Mode" : "Dark Mode";
        localStorage.setItem("resumeTheme", activeTheme);
    });

    const savedTheme = localStorage.getItem("resumeTheme") || "light";
    if (savedTheme === "dark") {
        document.documentElement.classList.add("theme-dark");
        themeToggle.textContent = "Light Mode";
    }
}

document.addEventListener("DOMContentLoaded", () => {
    setupResumePage();
    const flash = document.querySelector(".flash-banner");
    if (flash) {
        setTimeout(() => flash.classList.add("visible"), 50);
        setTimeout(() => flash.classList.remove("visible"), 4000);
    }

    document.querySelectorAll('.template-option').forEach(option => {
        option.addEventListener('click', () => {
            option.querySelector('input')?.click();
        });
    });

    const welcomeOverlay = document.getElementById("welcomeOverlay");
    if (welcomeOverlay) {
        setTimeout(() => {
            welcomeOverlay.style.opacity = "0";
            welcomeOverlay.style.pointerEvents = "none";
            setTimeout(() => welcomeOverlay.remove(), 400);
        }, 2200);
    }
});
