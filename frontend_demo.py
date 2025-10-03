"""
Frontend Demo - AI Learning Planner
===================================

This script demonstrates the frontend functionality without requiring a running server.
"""

import webbrowser
import http.server
import socketserver
import os
import sys
from pathlib import Path

def start_frontend_server():
    """Start a simple HTTP server to serve the frontend"""
    
    print("🎓 AI Learning Planner - Frontend Demo")
    print("=" * 50)
    
    # Change to frontend directory
    frontend_dir = Path(__file__).parent / "frontend"
    os.chdir(frontend_dir)
    
    # Create a simple HTTP server
    PORT = 8000
    
    class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
        def end_headers(self):
            # Add CORS headers
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
            self.send_header('Access-Control-Allow-Headers', 'Content-Type')
            super().end_headers()
    
    try:
        with socketserver.TCPServer(("", PORT), CustomHTTPRequestHandler) as httpd:
            print(f"🌐 Frontend server starting on port {PORT}")
            print(f"📱 Open your browser and go to: http://localhost:{PORT}")
            print("=" * 50)
            print("🎯 Features available:")
            print("   • Create personalized learning plans")
            print("   • Track learning progress")
            print("   • Take weekly tests")
            print("   • Get adaptive recommendations")
            print("=" * 50)
            print("Press Ctrl+C to stop the server")
            print("=" * 50)
            
            # Try to open browser automatically
            try:
                webbrowser.open(f'http://localhost:{PORT}')
                print("🚀 Browser opened automatically!")
            except:
                print("🌐 Please open your browser manually")
            
            httpd.serve_forever()
            
    except KeyboardInterrupt:
        print("\n👋 Server stopped. Goodbye!")
    except OSError as e:
        if e.errno == 10048:  # Port already in use
            print(f"❌ Port {PORT} is already in use. Trying port {PORT + 1}...")
            start_frontend_server_port(PORT + 1)
        else:
            print(f"❌ Error starting server: {e}")

def start_frontend_server_port(port):
    """Start server on specific port"""
    try:
        with socketserver.TCPServer(("", port), http.server.SimpleHTTPRequestHandler) as httpd:
            print(f"🌐 Frontend server starting on port {port}")
            print(f"📱 Open your browser and go to: http://localhost:{port}")
            webbrowser.open(f'http://localhost:{port}')
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n👋 Server stopped. Goodbye!")

def show_frontend_info():
    """Show information about the frontend"""
    
    print("🎓 AI Learning Planner - Frontend")
    print("=" * 50)
    print("📁 Frontend files:")
    print("   • frontend/index.html - Main interface")
    print("   • frontend/style.css - Styling")
    print("   • frontend/script.js - Functionality")
    print()
    print("🚀 To start the frontend:")
    print("   1. Run: python frontend_demo.py")
    print("   2. Open: http://localhost:8000")
    print("   3. Start learning!")
    print()
    print("🎯 Example requests to try:")
    print("   • 'I want to learn Python for 3 months with weekly tests'")
    print("   • 'I need to master JavaScript in 6 weeks for a job interview'")
    print("   • 'I want to learn Machine Learning for 6 months with projects'")
    print("   • 'I need to become a web developer in 1 year'")
    print()
    print("✨ Features:")
    print("   • Dynamic learning plan creation")
    print("   • Real-time progress tracking")
    print("   • Weekly test simulation")
    print("   • Adaptive learning recommendations")
    print("   • Responsive design")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "info":
        show_frontend_info()
    else:
        start_frontend_server()

