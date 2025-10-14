#!/usr/bin/env python3
"""
Text Summarizer Pro - Enhanced Launcher with Advanced NLP
"""

import subprocess
import sys
import os

def main():
    print("=" * 80)
    print("📝 TEXT SUMMARIZER PRO - ENHANCED WITH ADVANCED NLP")
    print("=" * 80)
    print()
    
    print("Choose your preferred interface:")
    print()
    print("1. 🔬 Enhanced Web Interface - Advanced NLP with stopwords detection")
    print("2. 🌐 Web Interface with Translation - Basic version with translation")
    print("3. 🌐 Simple Web Interface - Basic version without translation")
    print("4. 🖥️ Desktop Interface - Native desktop app")
    print("5. 🧪 Test NLP Features - Test advanced NLP functionality")
    print("6. ❌ Exit")
    print()
    
    while True:
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == "1":
            print("🔬 Starting Enhanced Streamlit application with advanced NLP...")
            print("Features: Stopwords detection, sentiment analysis, POS tagging, word frequency")
            print("The app will open in your browser at http://localhost:8501")
            try:
                subprocess.run([sys.executable, "-m", "streamlit", "run", "enhanced_streamlit_app.py"])
            except KeyboardInterrupt:
                print("\n👋 Enhanced app stopped.")
            break
        elif choice == "2":
            print("🌐 Starting Streamlit web application with translation...")
            print("The app will open in your browser at http://localhost:8501")
            try:
                subprocess.run([sys.executable, "-m", "streamlit", "run", "app_with_working_translation.py"])
            except KeyboardInterrupt:
                print("\n👋 Web app stopped.")
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
            print("🖥️ Starting desktop application...")
            try:
                subprocess.run([sys.executable, "desktop_app_simple.py"])
            except KeyboardInterrupt:
                print("\n👋 Desktop app stopped.")
            break
        elif choice == "5":
            print("🧪 Testing advanced NLP functionality...")
            try:
                subprocess.run([sys.executable, "test_nlp.py"])
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


