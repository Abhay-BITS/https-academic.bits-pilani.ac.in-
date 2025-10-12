#!/usr/bin/env python3
"""
BITS Pilani Academic Website Launcher
This script launches a local HTTP server to run the academic website.
"""

import http.server
import socketserver
import webbrowser
import os
import sys
from pathlib import Path

def launch_website():
    # Get the directory where this script is located
    script_dir = Path(__file__).parent.absolute()
    os.chdir(script_dir)
    
    # Set the port
    PORT = 8000
    
    # Create a custom handler to serve files
    class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
        def end_headers(self):
            # Add CORS headers to allow local development
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
            self.send_header('Access-Control-Allow-Headers', 'Content-Type')
            super().end_headers()
        
        def log_message(self, format, *args):
            # Suppress default logging to reduce console output
            pass
    
    # Try to start the server
    try:
        with socketserver.TCPServer(("", PORT), CustomHTTPRequestHandler) as httpd:
            print("=" * 60)
            print("🚀 BITS PILANI ACADEMIC WEBSITE LAUNCHER")
            print("=" * 60)
            print(f"📍 Server running at: http://localhost:{PORT}")
            print(f"📁 Serving files from: {script_dir}")
            print("=" * 60)
            print("🌐 Opening website in your default browser...")
            print("=" * 60)
            print("💡 To stop the server, press Ctrl+C")
            print("=" * 60)
            
            # Open the website in the default browser
            webbrowser.open(f'http://localhost:{PORT}/index.html')
            
            # Start serving
            httpd.serve_forever()
            
    except OSError as e:
        if e.errno == 48:  # Address already in use
            print(f"❌ Port {PORT} is already in use. Trying port {PORT + 1}...")
            PORT += 1
            with socketserver.TCPServer(("", PORT), CustomHTTPRequestHandler) as httpd:
                print(f"📍 Server running at: http://localhost:{PORT}")
                webbrowser.open(f'http://localhost:{PORT}/index.html')
                httpd.serve_forever()
        else:
            print(f"❌ Error starting server: {e}")
            sys.exit(1)
    except KeyboardInterrupt:
        print("\n🛑 Server stopped by user.")
        sys.exit(0)

if __name__ == "__main__":
    launch_website()
