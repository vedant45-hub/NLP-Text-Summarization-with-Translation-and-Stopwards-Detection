#!/usr/bin/env python3
"""
Text Summarizer Pro - Quick Launcher
"""

import subprocess
import sys
import os

def main():
    print("=" * 60)
    print("📝 TEXT SUMMARIZER PRO - QUICK LAUNCHER")
    print("=" * 60)
    print()
    
    print("Choose your preferred interface:")
    print()
    print("1. 🌐 Web Interface (Streamlit) - Modern, colorful, feature-rich")
    print("2. 🖥️ Desktop Interface (Tkinter) - Native desktop app")
    print("3. 📱 Demo Script - Command line demonstration")
    print("4. ❌ Exit")
    print()
    
    while True:
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == "1":
            print("🌐 Starting Streamlit web application...")
            print("The app will open in your browser at http://localhost:8501")
            try:
                subprocess.run([sys.executable, "-m", "streamlit", "run", "final_app.py"])
            except KeyboardInterrupt:
                print("\n👋 Web app stopped.")
            break
        elif choice == "2":
            print("🖥️ Starting desktop application...")
            try:
                subprocess.run([sys.executable, "desktop_app_simple.py"])
            except KeyboardInterrupt:
                print("\n👋 Desktop app stopped.")
            break
        elif choice == "3":
            print("📱 Running demo script...")
            try:
                subprocess.run([sys.executable, "basic_summarization.py"])
            except KeyboardInterrupt:
                print("\n👋 Demo stopped.")
            break
        elif choice == "4":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()


