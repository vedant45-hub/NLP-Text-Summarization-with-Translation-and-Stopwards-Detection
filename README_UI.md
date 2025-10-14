# 📝 Text Summarizer Pro - UI Edition

A beautiful, modern text summarization application with user input and multi-language translation support. Choose between a stunning web interface or a native desktop application.

## ✨ Features

### 🎯 Core Features
- **Smart Text Summarization** - Extract key sentences using advanced algorithms
- **User Input Interface** - Easy text input with real-time processing
- **Multi-language Translation** - Translate summaries to Hindi, Marathi, Spanish, French, and German
- **Beautiful UI** - Modern, colorful, and responsive design
- **Real-time Statistics** - View compression ratios and text metrics
- **File Operations** - Load text from files and save summaries

### 🌐 Web Interface (Streamlit)
- **Gradient Backgrounds** - Beautiful color schemes
- **Interactive Controls** - Sliders, dropdowns, and real-time updates
- **Responsive Design** - Works on desktop, tablet, and mobile
- **Download Options** - Save summaries and translations as files
- **Progress Indicators** - Visual feedback during processing

### 🖥️ Desktop Interface (Tkinter)
- **Native Look & Feel** - Integrated with your operating system
- **Multi-threaded Processing** - Non-blocking UI during processing
- **File Dialogs** - Easy file loading and saving
- **Status Bar** - Real-time status updates
- **Keyboard Shortcuts** - Efficient workflow

## 🚀 Quick Start

### Option 1: Easy Launcher (Recommended)
```bash
python launcher.py
```
This will:
1. Install all required packages automatically
2. Let you choose between web or desktop interface
3. Launch your preferred application

### Option 2: Manual Installation

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run Web Interface**
   ```bash
   streamlit run app.py
   ```

3. **Run Desktop Interface**
   ```bash
   python desktop_app.py
   ```

## 📱 Usage Guide

### Web Interface
1. **Open** the web interface in your browser
2. **Paste** your text in the input area
3. **Adjust** summary length using the slider
4. **Select** translation language (optional)
5. **Click** "Generate Summary" button
6. **Download** results if needed

### Desktop Interface
1. **Launch** the desktop application
2. **Type or paste** text in the input area
3. **Adjust** settings in the right panel
4. **Click** "Generate Summary" button
5. **Use** file menu for loading/saving

## 🎨 UI Features

### Color Scheme
- **Primary**: Blue gradient (#667eea to #764ba2)
- **Secondary**: Pink gradient (#f093fb to #f5576c)
- **Accent**: Cyan gradient (#4facfe to #00f2fe)
- **Background**: Light gray (#f0f2f6)

### Interactive Elements
- **Hover Effects** - Buttons and cards respond to mouse interaction
- **Smooth Transitions** - Elegant animations throughout
- **Progress Indicators** - Visual feedback during processing
- **Responsive Layout** - Adapts to different screen sizes

## 🌍 Translation Support

### Supported Languages
- **Hindi** (हिंदी)
- **Marathi** (मराठी)
- **Spanish** (Español)
- **French** (Français)
- **German** (Deutsch)

### Translation Features
- **Real-time Translation** - Instant translation of summaries
- **Download Options** - Save translated summaries
- **Error Handling** - Graceful handling of translation errors
- **Language Detection** - Automatic source language detection

## 📊 Statistics & Metrics

### Text Analysis
- **Character Count** - Original vs. summary length
- **Compression Ratio** - Percentage of text reduction
- **Sentence Count** - Number of sentences in summary
- **Word Frequency** - Most important words highlighted

### Performance Metrics
- **Processing Time** - Real-time processing speed
- **Memory Usage** - Efficient resource utilization
- **Success Rate** - Translation and summarization success

## 🛠️ Technical Details

### Dependencies
- **Streamlit** - Web interface framework
- **Tkinter** - Desktop GUI framework (built-in)
- **googletrans** - Google Translate API
- **re** - Regular expressions for text processing

### Architecture
- **Modular Design** - Separate UI and processing logic
- **Threading** - Non-blocking operations in desktop app
- **Error Handling** - Comprehensive error management
- **State Management** - Efficient UI state handling

## 📁 Project Structure

```
Text-Summarization-NLP-main/
├── app.py                 # Streamlit web application
├── desktop_app.py         # Tkinter desktop application
├── launcher.py           # Application launcher
├── requirements.txt      # Python dependencies
├── README_UI.md         # This file
├── basic_summarization.py # Core summarization logic
└── text-summarization.py  # Original script
```

## 🔧 Customization

### UI Customization
- **Colors**: Modify CSS in `app.py` or colors in `desktop_app.py`
- **Layout**: Adjust column widths and spacing
- **Fonts**: Change font families and sizes
- **Icons**: Replace emoji icons with custom images

### Functionality Customization
- **Summary Length**: Adjust min/max sentence limits
- **Languages**: Add more translation options
- **Algorithms**: Modify summarization logic
- **File Formats**: Support additional file types

## 🐛 Troubleshooting

### Common Issues

1. **Translation Errors**
   - Check internet connection
   - Verify googletrans installation
   - Try different language combinations

2. **UI Not Loading**
   - Ensure all dependencies are installed
   - Check Python version compatibility
   - Restart the application

3. **File Loading Issues**
   - Check file encoding (UTF-8 recommended)
   - Verify file permissions
   - Try different file formats

### Error Messages
- **"Module not found"** → Run `pip install -r requirements.txt`
- **"Translation error"** → Check internet connection
- **"File not found"** → Verify file path and permissions

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. **Fork** the repository
2. **Create** a feature branch
3. **Make** your changes
4. **Test** thoroughly
5. **Submit** a pull request

### Areas for Contribution
- **UI Improvements** - Better designs and animations
- **New Languages** - Additional translation support
- **Algorithms** - Better summarization techniques
- **Performance** - Faster processing and loading
- **Documentation** - Better guides and examples

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Streamlit** team for the amazing web framework
- **Google Translate** for translation services
- **NLTK** community for natural language processing tools
- **Contributors** who helped improve this project

## 📞 Support

If you encounter any issues or have questions:

1. **Check** the troubleshooting section
2. **Search** existing issues
3. **Create** a new issue with details
4. **Contact** the maintainers

---

**Made with ❤️ using Python, Streamlit, and Tkinter**

*Transform your text into beautiful summaries with just a few clicks!*


