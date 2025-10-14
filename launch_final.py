#!/usr/bin/env python3
"""
Text Summarizer Pro - Final Launcher with Working NLP
"""

import subprocess
import sys
import os

def main():
    print("=" * 80)
    print("📝 TEXT SUMMARIZER PRO - FINAL VERSION WITH WORKING NLP")
    print("=" * 80)
    print()
    
    print("Choose your preferred interface:")
    print()
    print("1. 🔬 Advanced NLP Web Interface - Stopwords detection, sentiment analysis, POS tagging")
    print("2. 🌐 Web Interface with Translation - Basic version with translation")
    print("3. 🌐 Simple Web Interface - Basic version without translation")
    print("4. 🖥️ Desktop Interface - Native desktop app")
    print("5. 🧪 Test Stopwords Detection - Test stopwords functionality")
    print("6. ❌ Exit")
    print()
    
    while True:
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == "1":
            print("🔬 Starting Advanced NLP Streamlit application...")
            print("Features: Stopwords detection, sentiment analysis, POS tagging, word frequency")
            print("The app will open in your browser at http://localhost:8501")
            try:
                subprocess.run([sys.executable, "-m", "streamlit", "run", "streamlit_nlp_simple.py"])
            except KeyboardInterrupt:
                print("\n👋 Advanced NLP app stopped.")
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
            print("🧪 Testing stopwords detection functionality...")
            try:
                subprocess.run([sys.executable, "test_stopwords.py"])
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


