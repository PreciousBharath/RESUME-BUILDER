"""
Configuration and settings for ResumePro Advanced Resume Builder
"""

# Application Settings
DEBUG_MODE = True
HOST = "localhost"
PORT = 5000

# Upload Settings
MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp'}
UPLOAD_FOLDER = "static/uploads"

# Resume Settings
RESUME_TEMPLATES = {
    1: "Modern Professional (Blue Theme)",
    2: "Classic Minimal (Purple Theme)"
}

EXPORT_FORMATS = {
    'docx': 'Word Document (.docx)',
    'pdf': 'PDF Document (.pdf)'
}

EXPERIENCE_LEVELS = [
    "Fresher",
    "Experienced",
    "Senior"
]

# UI Settings
COLORS = {
    'primary': '#00a88f',
    'secondary': '#0fd1b2',
    'accent': '#667eea',
    'accent_dark': '#764ba2'
}

ANIMATIONS = {
    'transition_speed': '0.3s',
    'easing': 'ease-out'
}

# Form Validation
VALIDATION_RULES = {
    'name': {
        'required': True,
        'min_length': 2,
        'max_length': 100,
        'pattern': r'^[a-zA-Z\s]+$'
    },
    'email': {
        'required': True,
        'pattern': r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    },
    'phone': {
        'required': True,
        'min_length': 10
    },
    'role': {
        'required': True,
        'min_length': 2,
        'max_length': 100
    },
    'skills': {
        'required': True,
        'min_items': 1
    },
    'education': {
        'required': True,
        'min_length': 10
    },
    'experience': {
        'required': True,
        'min_length': 10
    },
    'goal': {
        'required': True,
        'min_length': 10
    }
}
