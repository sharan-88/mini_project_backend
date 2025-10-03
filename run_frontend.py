"""
Startup script for AI Learning Planner Frontend
===============================================

This script starts the backend API server to serve the frontend.
"""

import os
import sys
import subprocess
from pathlib import Path

def main():
    """Start the backend API server"""
    
    print("🚀 Starting AI Learning Planner Frontend")
    print("=" * 50)
    
    # Check if Flask is installed
    try:
        import flask
        import flask_cors
        print("✅ Flask and Flask-CORS are installed")
    except ImportError:
        print("❌ Flask or Flask-CORS not found. Installing...")
        subprocess.run([sys.executable, "-m", "pip", "install", "flask", "flask-cors"], check=True)
        print("✅ Flask and Flask-CORS installed successfully")
    
    # Start the backend server
    print("\n🌐 Starting backend API server...")
    print("📡 API will be available at: http://localhost:5000")
    print("🎨 Frontend will be available at: http://localhost:5000")
    print("=" * 50)
    print("Press Ctrl+C to stop the server")
    print("=" * 50)
    
    try:
        # Import and run the backend
        from backend_api import app
        app.run(debug=True, host='0.0.0.0', port=5000)
    except KeyboardInterrupt:
        print("\n👋 Server stopped. Goodbye!")
    except Exception as e:
        print(f"❌ Error starting server: {e}")
        print("Please check your Python environment and dependencies.")

if __name__ == "__main__":
    main()

