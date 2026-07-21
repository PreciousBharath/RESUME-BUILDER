# 🚀 ResumePro - Advanced AI-Powered Resume Builder

A modern, feature-rich resume builder application with intelligent content generation, multiple templates, and instant PDF/DOCX export.

## ✨ Features

### 🎨 **Advanced UI Design**
- Modern, responsive interface with gradient backgrounds
- Smooth animations and transitions
- Real-time live preview of your resume
- Professional color scheme and typography
- Mobile-friendly responsive design

### 📝 **Smart Resume Generation**
- **AI-Powered Content**: Intelligent prompt engineering generates context-aware professional summaries
- **Multiple Templates**: Choose from 2 professionally designed templates
- **Live Preview**: See your resume update in real-time as you type
- **Profile Photo Support**: Add and preview your profile photo instantly

### 💾 **Export Options**
- **PDF Export**: Download as professional PDF document
- **DOCX Export**: Download as editable Word document
- Both formats include proper formatting and styling

### 📊 **Enhanced Features**
- Progress tracking - see how complete your resume is
- Form validation with helpful error messages
- Photo upload with drag-and-drop support
- Experience level-based content generation (Fresher, Experienced, Senior)
- Multiple professional sections:
  - Personal Information
  - Professional Summary
  - Technical Skills
  - Work Experience
  - Education

## 🛠️ Installation

### Prerequisites
- Python 3.7+
- pip (Python package manager)

### Setup Instructions

1. **Clone/Extract the project**
   ```bash
   cd "resume builder/code/prompt_RESUME"
   ```

2. **Create a virtual environment** (optional but recommended)
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Access the application**
   - Open your browser and navigate to: `http://localhost:5000`

## 📖 Usage

### Creating a Resume

1. **Visit the Home Page**
   - Click "Start Building" to go to the resume builder

2. **Fill in Your Information**
   - Enter your name, email, and phone number
   - Specify your target job role and experience level
   - Add your skills (comma-separated)
   - Include your education and work experience
   - Write your career objective

3. **Upload Profile Photo** (Optional)
   - Click the upload area or drag & drop your photo
   - Photo will appear in the preview immediately

4. **Preview Your Resume**
   - View real-time preview on the right side
   - Switch between Template 1 and Template 2
   - Check the progress bar to ensure all fields are complete

5. **Select Format & Download**
   - Choose between PDF or DOCX format
   - Click "Download Resume"
   - Your professional resume will be downloaded

## 🎯 Template Options

### Template 1: Professional Modern
- Centered header with profile photo
- Color-coded sections with modern styling
- Blue theme with professional appearance
- Best for: Creative and tech roles

### Template 2: Classic Minimal
- Traditional layout with emphasis on content
- Clean, simple design
- Purple accents for subtle highlighting
- Best for: Corporate and formal roles

## 🔧 Technical Stack

- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Backend**: Flask (Python)
- **Document Generation**: 
  - python-docx (for Word documents)
  - reportlab (for PDF documents)
- **AI**: Advanced prompt engineering for content generation

## 📁 Project Structure

```
prompt_RESUME/
├── app.py                 # Flask application main file
├── prompt_engine.py      # AI prompt engineering module
├── create_resume.py      # Resume generation module (DOCX & PDF)
├── requirements.txt      # Python dependencies
├── templates/
│   ├── index.html        # Landing page
│   └── create_resume.html # Resume builder interface
├── static/
│   ├── css/
│   │   └── style.css     # Global styles
│   └── uploads/          # Uploaded photos directory
└── README.md             # This file
```

## 🎨 Customization

### Modify Colors
Edit `static/css/style.css` to change the color scheme:
```css
:root {
    --primary: #00a88f;    /* Main color */
    --secondary: #0fd1b2;  /* Accent color */
}
```

### Add New Templates
1. Add new template HTML in `create_resume.html`
2. Create corresponding generation function in `create_resume.py`
3. Update the template toggle in the UI

### Enhance AI Summaries
Edit `prompt_engine.py` to add more sophisticated content generation based on your needs.

## 🚀 Advanced Features

### Progress Tracking
The form includes a progress bar that fills as you complete each field, helping you ensure all sections are complete before downloading.

### Real-Time Validation
Form fields provide immediate visual feedback and validation as you type.

### Template Switching
Switch between different resume templates while maintaining all your entered data.

### Photo Management
Upload, preview, and manage your profile photo directly in the interface.

## ⚡ Performance Optimizations

- Efficient real-time preview updates
- Optimized image handling
- Fast PDF and DOCX generation
- Responsive design that works on all devices

## 🐛 Troubleshooting

### Issue: Module not found errors
- **Solution**: Ensure all dependencies are installed: `pip install -r requirements.txt`

### Issue: Images not showing in downloaded resume
- **Solution**: Use standard image formats (PNG, JPG). Keep image size reasonable.

### Issue: PDF formatting issues
- **Solution**: Try using the DOCX format instead, or check that your content doesn't exceed typical resume length.

### Issue: Port 5000 already in use
- **Solution**: Change the port in `app.py`:
  ```python
  app.run(debug=True, port=5001)
  ```

## 📝 Tips for Best Results

1. **Keep it concise**: Use clear, bullet-point style content
2. **Use proper formatting**: Separate multiple entries with line breaks
3. **Optimize skills**: List relevant, industry-specific skills
4. **Professional photo**: Use a high-quality, professional headshot
5. **Proofread**: Check for typos and grammar before downloading

## 🤝 Contributing

Feel free to customize and extend this project for your needs!

## 📄 License

This project is open source and available for personal and commercial use.

## 👨‍💻 Author

Built with ❤️ using Flask and modern web technologies.

---

**Happy Resume Building! 🎉**
