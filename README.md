# 📝 NLP Text Summarization with Translation and Stopwords Detection

This project is an **extractive text summarization toolkit** built with Python, **NLTK**, and **Streamlit**. Beyond summarization, it detects and analyzes **stopwords**, performs basic **POS tagging** and **sentiment scoring**, and can **translate summaries into multiple languages** (Hindi, Marathi, Spanish, French, German, Japanese, Chinese, Arabic, and more) using `deep-translator`.

The repo ships with several interchangeable front ends — a full-featured "Robust NLP" web app, simpler web apps, desktop (Tkinter) apps, and plain command-line scripts — plus launcher scripts that let you pick which one to run.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Core Functions Explained](#core-functions-explained)
- [App Variants](#app-variants)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

---

## Features

- **Extractive Summarization** — Scores sentences by word frequency (with stopwords removed) and selects the top N as the summary. Summary length is adjustable.
- **Stopwords Detection** — Identifies and counts stopwords vs. meaningful words in your input text, with a breakdown you can inspect.
- **Text Analysis** — Basic POS tagging, average sentence/word length, and a simple positive/negative sentiment score.
- **Multi-language Translation** — Translates the generated summary into Hindi, Marathi, Spanish, French, German, Japanese, Chinese, or Arabic via `deep-translator` (Google Translate backend).
- **Multiple Interfaces** — Choose between a rich Streamlit web UI, a simpler Streamlit UI, or a native Tkinter desktop app.
- **Fallback-safe NLP** — The "Robust" app degrades gracefully to regex-based tokenization if NLTK data isn't available, so it still works offline.
- **File & Report Downloads** — Export the summary or a full text report (with stats) as `.txt` files.
- **Interactive Launchers** — Menu-driven scripts (`launcher.py`, `run_app.py`, `launch_robust.py`, etc.) so you don't need to remember which file to run.

---

## Installation

1. Clone this repository:
```bash
   git clone https://github.com/sanchitc05/NLP-Text-Summarization-with-Translation-and-Stopwards-Detection.git
   cd NLP-Text-Summarization-with-Translation-and-Stopwards-Detection
```

2. Install the required packages:
```bash
   pip install -r requirements.txt
```
   The main "Robust" app needs `streamlit`, `nltk`, `deep-translator`, `matplotlib`, and `pandas`. Some legacy variants also reference `googletrans` and `requests`. Tkinter ships with most standard Python installs (on Linux you may need `sudo apt install python3-tk`).

3. Download NLTK resources (the apps also attempt this automatically on first run):
```python
   import nltk
   nltk.download('punkt')
   nltk.download('punkt_tab')
   nltk.download('stopwords')
   nltk.download('averaged_perceptron_tagger')
```

---

## Usage

### Quickest way — use a launcher
```bash
python launch_robust.py
```
This opens a menu where you can choose the Robust NLP web app, a translation-enabled web app, a simple web app, the desktop app, or a CLI test script.

### Run the flagship app directly
```bash
streamlit run streamlit_robust_nlp.py
```
Then in the browser:
1. Paste or type your text into the input box.
2. Adjust the summary length slider.
3. Click **Generate Summary** to get the extractive summary, stopword breakdown, and text analysis.
4. Optionally pick a target language to translate the summary.
5. Download the summary or full report as a `.txt` file.

### Run a plain script (no UI)
```bash
python text-summarization.py
```
