#!/bin/bash
# Quick Start Script for ResumePro

echo "=================================="
echo "  ResumePro - Advanced Resume Builder"
echo "=================================="
echo ""

# Check if Python is installed
if ! command -v python &> /dev/null; then
    echo "❌ Python is not installed. Please install Python 3.7+"
    exit 1
fi

echo "✅ Python found: $(python --version)"
echo ""

# Create virtual environment
echo "📦 Creating virtual environment..."
python -m venv venv

# Activate virtual environment
echo "🔄 Activating virtual environment..."
if [ -d "venv/Scripts" ]; then
    source venv/Scripts/activate
else
    source venv/bin/activate
fi

# Install dependencies
echo "📚 Installing dependencies..."
pip install -r requirements.txt

echo ""
echo "=================================="
echo "✨ Setup Complete!"
echo "=================================="
echo ""
echo "To start the application, run:"
echo "  python app.py"
echo ""
echo "Then visit: http://localhost:5000"
echo ""
