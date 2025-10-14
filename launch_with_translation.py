#!/usr/bin/env python3
"""
Text Summarizer Pro - Launcher with Working Translation
"""

import subprocess
import sys
import os

def main():
    print("=" * 70)
    print("📝 TEXT SUMMARIZER PRO - WITH WORKING TRANSLATION")
    print("=" * 70)
    print()
    
    print("Choose your preferred interface:")
    print()
    print("1. 🌐 Web Interface (Streamlit) - Modern, colorful, with translation")
    print("2. 🖥️ Desktop Interface (Tkinter) - Native desktop app with translation")
    print("3. 🌐 Web Interface (Simple) - Basic version without translation")
    print("4. 🖥️ Desktop Interface (Simple) - Basic desktop version")
    print("5. 🧪 Test Translation - Test translation functionality")
    print("6. ❌ Exit")
    print()
    
    while True:
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == "1":
            print("🌐 Starting Streamlit web application with translation...")
            print("The app will open in your browser at http://localhost:8501")
            try:
                subprocess.run([sys.executable, "-m", "streamlit", "run", "app_with_working_translation.py"])
            except KeyboardInterrupt:
                print("\n👋 Web app stopped.")
            break
        elif choice == "2":
            print("🖥️ Starting desktop application with translation...")
            try:
                subprocess.run([sys.executable, "desktop_app_with_translation.py"])
            except KeyboardInterrupt:
                print("\n👋 Desktop app stopped.")
            break
        elif choice == "3":
            print("🌐 Starting simple web application...")
            print("The app will open in your browser at http://localhost:8501")
            try:
                subprocess.run([sys.executable, "-m", "streamlit", "run", "final_app.py"])
            except KeyboardInterrupt:
                print("\n👋 Web app stopped.")
            break
        elif choice == "4":
            print("🖥️ Starting simple desktop application...")
            try:
                subprocess.run([sys.executable, "desktop_app_simple.py"])
            except KeyboardInterrupt:
                print("\n👋 Desktop app stopped.")
            break
        elif choice == "5":
            print("🧪 Testing translation functionality...")
            try:
                subprocess.run([sys.executable, "test_translation.py"])
            except KeyboardInterrupt:
                print("\n👋 Test stopped.")
            break
        elif choice == "6":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please enter 1-6.")

if __name__ == "__main__":
    main()


