import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox, filedialog
import re
from googletrans import Translator
import threading

class TextSummarizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Summarizer Pro - Desktop Edition")
        self.root.geometry("1000x700")
        self.root.configure(bg='#f0f2f6')
        
        # Configure style
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Configure colors
        self.style.configure('Title.TLabel', font=('Arial', 16, 'bold'), foreground='#2c3e50')
        self.style.configure('Header.TLabel', font=('Arial', 12, 'bold'), foreground='#34495e')
        self.style.configure('Custom.TButton', font=('Arial', 10, 'bold'))
        
        self.setup_ui()
        
    def setup_ui(self):
        # Main title
        title_frame = tk.Frame(self.root, bg='#f0f2f6')
        title_frame.pack(pady=20)
        
        title_label = tk.Label(
            title_frame, 
            text="📝 Text Summarizer Pro", 
            font=('Arial', 20, 'bold'),
            fg='#2c3e50',
            bg='#f0f2f6'
        )
        title_label.pack()
        
        subtitle_label = tk.Label(
            title_frame,
            text="Transform your text into concise summaries with beautiful translations",
            font=('Arial', 10),
            fg='#7f8c8d',
            bg='#f0f2f6'
        )
        subtitle_label.pack()
        
        # Main content frame
        main_frame = tk.Frame(self.root, bg='#f0f2f6')
        main_frame.pack(fill='both', expand=True, padx=20, pady=10)
        
        # Left panel - Input
        left_panel = tk.Frame(main_frame, bg='white', relief='raised', bd=2)
        left_panel.pack(side='left', fill='both', expand=True, padx=(0, 10))
        
        # Input section
        input_label = tk.Label(
            left_panel, 
            text="📝 Enter your text here:", 
            font=('Arial', 12, 'bold'),
            fg='#2c3e50',
            bg='white'
        )
        input_label.pack(anchor='w', padx=15, pady=(15, 5))
        
        self.text_input = scrolledtext.ScrolledText(
            left_panel, 
            height=15, 
            width=50,
            font=('Arial', 10),
            wrap=tk.WORD,
            relief='solid',
            bd=1
        )
        self.text_input.pack(fill='both', expand=True, padx=15, pady=(0, 15))
        
        # Right panel - Controls and Output
        right_panel = tk.Frame(main_frame, bg='white', relief='raised', bd=2)
        right_panel.pack(side='right', fill='both', expand=True, padx=(10, 0))
        
        # Settings section
        settings_label = tk.Label(
            right_panel,
            text="⚙️ Settings",
            font=('Arial', 12, 'bold'),
            fg='#2c3e50',
            bg='white'
        )
        settings_label.pack(anchor='w', padx=15, pady=(15, 5))
        
        # Summary length
        length_frame = tk.Frame(right_panel, bg='white')
        length_frame.pack(fill='x', padx=15, pady=5)
        
        tk.Label(length_frame, text="Summary length:", bg='white').pack(side='left')
        self.length_var = tk.IntVar(value=3)
        length_spinbox = tk.Spinbox(
            length_frame, 
            from_=1, 
            to=10, 
            textvariable=self.length_var,
            width=5
        )
        length_spinbox.pack(side='right')
        
        # Translation options
        trans_frame = tk.Frame(right_panel, bg='white')
        trans_frame.pack(fill='x', padx=15, pady=5)
        
        tk.Label(trans_frame, text="Translate to:", bg='white').pack(side='left')
        self.trans_var = tk.StringVar(value="None")
        trans_combo = ttk.Combobox(
            trans_frame,
            textvariable=self.trans_var,
            values=["None", "Hindi", "Marathi", "Spanish", "French", "German"],
            state="readonly",
            width=15
        )
        trans_combo.pack(side='right')
        
        # Process button
        process_btn = tk.Button(
            right_panel,
            text="🚀 Generate Summary",
            command=self.process_text,
            font=('Arial', 12, 'bold'),
            bg='#3498db',
            fg='white',
            relief='raised',
            bd=2,
            padx=20,
            pady=10
        )
        process_btn.pack(pady=20)
        
        # Output section
        output_label = tk.Label(
            right_panel,
            text="🎯 Summary",
            font=('Arial', 12, 'bold'),
            fg='#2c3e50',
            bg='white'
        )
        output_label.pack(anchor='w', padx=15, pady=(20, 5))
        
        self.summary_output = scrolledtext.ScrolledText(
            right_panel,
            height=8,
            width=40,
            font=('Arial', 10),
            wrap=tk.WORD,
            relief='solid',
            bd=1,
            state='disabled'
        )
        self.summary_output.pack(fill='both', expand=True, padx=15, pady=(0, 10))
        
        # Translation output
        self.trans_output = scrolledtext.ScrolledText(
            right_panel,
            height=6,
            width=40,
            font=('Arial', 10),
            wrap=tk.WORD,
            relief='solid',
            bd=1,
            state='disabled'
        )
        self.trans_output.pack(fill='x', padx=15, pady=(0, 15))
        
        # Bottom buttons
        button_frame = tk.Frame(self.root, bg='#f0f2f6')
        button_frame.pack(fill='x', padx=20, pady=10)
        
        tk.Button(
            button_frame,
            text="📁 Load File",
            command=self.load_file,
            bg='#27ae60',
            fg='white',
            relief='raised',
            bd=2,
            padx=15
        ).pack(side='left', padx=5)
        
        tk.Button(
            button_frame,
            text="💾 Save Summary",
            command=self.save_summary,
            bg='#e74c3c',
            fg='white',
            relief='raised',
            bd=2,
            padx=15
        ).pack(side='left', padx=5)
        
        tk.Button(
            button_frame,
            text="🗑️ Clear All",
            command=self.clear_all,
            bg='#95a5a6',
            fg='white',
            relief='raised',
            bd=2,
            padx=15
        ).pack(side='left', padx=5)
        
        # Status bar
        self.status_var = tk.StringVar(value="Ready")
        status_bar = tk.Label(
            self.root,
            textvariable=self.status_var,
            relief='sunken',
            anchor='w',
            bg='#ecf0f1',
            fg='#2c3e50'
        )
        status_bar.pack(side='bottom', fill='x')
    
    def simple_summarize(self, text, num_sentences=3):
        """Simple extractive summarization based on sentence length and word frequency"""
        
        # Split into sentences
        sentences = re.split(r'[.!?]+', text)
        sentences = [s.strip() for s in sentences if s.strip()]
        
        # Simple scoring based on sentence length and word frequency
        word_freq = {}
        words = re.findall(r'\b\w+\b', text.lower())
        
        for word in words:
            if len(word) > 3:  # Only count words longer than 3 characters
                word_freq[word] = word_freq.get(word, 0) + 1
        
        # Score sentences
        sentence_scores = []
        for sentence in sentences:
            score = 0
            words_in_sentence = re.findall(r'\b\w+\b', sentence.lower())
            for word in words_in_sentence:
                if word in word_freq:
                    score += word_freq[word]
            # Add bonus for longer sentences (up to a point)
            score += min(len(sentence) / 10, 10)
            sentence_scores.append((score, sentence))
        
        # Get top sentences
        sentence_scores.sort(reverse=True)
        top_sentences = [sent for score, sent in sentence_scores[:num_sentences]]
        
        return '. '.join(top_sentences) + '.'
    
    def translate_text(self, text, target_language):
        """Translate text to target language using Google Translate"""
        try:
            translator = Translator()
            result = translator.translate(text, dest=target_language)
            return result.text
        except Exception as e:
            return f"Translation error: {str(e)}"
    
    def process_text(self):
        """Process the text and generate summary"""
        text = self.text_input.get("1.0", tk.END).strip()
        
        if not text:
            messagebox.showwarning("Warning", "Please enter some text to summarize!")
            return
        
        self.status_var.set("Processing...")
        self.root.update()
        
        def process_in_thread():
            try:
                # Generate summary
                summary = self.simple_summarize(text, self.length_var.get())
                
                # Update UI in main thread
                self.root.after(0, self.update_summary, summary)
                
                # Translate if requested
                if self.trans_var.get() != "None":
                    lang_codes = {
                        "Hindi": "hi",
                        "Marathi": "mr",
                        "Spanish": "es",
                        "French": "fr",
                        "German": "de"
                    }
                    
                    translated = self.translate_text(summary, lang_codes[self.trans_var.get()])
                    self.root.after(0, self.update_translation, translated)
                
                self.root.after(0, lambda: self.status_var.set("Ready"))
                
            except Exception as e:
                self.root.after(0, lambda: messagebox.showerror("Error", f"An error occurred: {str(e)}"))
                self.root.after(0, lambda: self.status_var.set("Error"))
        
        # Run in separate thread to avoid blocking UI
        threading.Thread(target=process_in_thread, daemon=True).start()
    
    def update_summary(self, summary):
        """Update the summary output"""
        self.summary_output.config(state='normal')
        self.summary_output.delete("1.0", tk.END)
        self.summary_output.insert("1.0", summary)
        self.summary_output.config(state='disabled')
    
    def update_translation(self, translation):
        """Update the translation output"""
        self.trans_output.config(state='normal')
        self.trans_output.delete("1.0", tk.END)
        self.trans_output.insert("1.0", f"Translation:\n{translation}")
        self.trans_output.config(state='disabled')
    
    def load_file(self):
        """Load text from file"""
        file_path = filedialog.askopenfilename(
            title="Select a text file",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        
        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    self.text_input.delete("1.0", tk.END)
                    self.text_input.insert("1.0", content)
                    self.status_var.set(f"Loaded: {file_path}")
            except Exception as e:
                messagebox.showerror("Error", f"Could not load file: {str(e)}")
    
    def save_summary(self):
        """Save summary to file"""
        if not self.summary_output.get("1.0", tk.END).strip():
            messagebox.showwarning("Warning", "No summary to save!")
            return
        
        file_path = filedialog.asksaveasfilename(
            title="Save summary",
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        
        if file_path:
            try:
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write(self.summary_output.get("1.0", tk.END))
                    self.status_var.set(f"Saved: {file_path}")
            except Exception as e:
                messagebox.showerror("Error", f"Could not save file: {str(e)}")
    
    def clear_all(self):
        """Clear all text areas"""
        self.text_input.delete("1.0", tk.END)
        self.summary_output.config(state='normal')
        self.summary_output.delete("1.0", tk.END)
        self.summary_output.config(state='disabled')
        self.trans_output.config(state='normal')
        self.trans_output.delete("1.0", tk.END)
        self.trans_output.config(state='disabled')
        self.status_var.set("Cleared")

def main():
    root = tk.Tk()
    app = TextSummarizerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()


