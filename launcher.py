#!/usr/bin/env python3
"""
Text Summarizer Pro - Launcher
Choose between Web UI (Streamlit) or Desktop UI (Tkinter)
"""

import subprocess
import sys
import os

def install_requirements():
    """Install required packages"""
    print("🔧 Installing required packages...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Packages installed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing packages: {e}")
        return False

def run_streamlit_app():
    """Run the Streamlit web application"""
    print("🌐 Starting Streamlit web application...")
    try:
        subprocess.run([sys.executable, "-m", "streamlit", "run", "app.py"])
    except KeyboardInterrupt:
        print("\n👋 Streamlit app stopped.")
    except Exception as e:
        print(f"❌ Error running Streamlit app: {e}")

def run_desktop_app():
    """Run the Tkinter desktop application"""
    print("🖥️ Starting desktop application...")
    try:
        subprocess.run([sys.executable, "desktop_app.py"])
    except KeyboardInterrupt:
        print("\n👋 Desktop app stopped.")
    except Exception as e:
        print(f"❌ Error running desktop app: {e}")

def main():
    print("=" * 60)
    print("📝 TEXT SUMMARIZER PRO - LAUNCHER")
    print("=" * 60)
    print()
    
    # Check if requirements are installed
    try:
        import streamlit
        import googletrans
    except ImportError:
        print("📦 Required packages not found. Installing...")
        if not install_requirements():
            print("❌ Failed to install requirements. Please install manually:")
            print("   pip install -r requirements.txt")
            return
    
    print("Choose your preferred interface:")
    print()
    print("1. 🌐 Web Interface (Streamlit) - Modern, colorful, feature-rich")
    print("2. 🖥️ Desktop Interface (Tkinter) - Native desktop app")
    print("3. ❌ Exit")
    print()
    
    while True:
        choice = input("Enter your choice (1-3): ").strip()
        
        if choice == "1":
            run_streamlit_app()
            break
        elif choice == "2":
            run_desktop_app()
            break
        elif choice == "3":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()


