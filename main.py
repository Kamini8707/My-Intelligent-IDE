import tkinter as tk
from tkinter import scrolledtext, messagebox, ttk
from code_generator import generate_code
from debugger import debug_code
from tester import run_tests
from documentation import generate_docs
import threading

class IntelligentIDE:
    def __init__(self, root):
        self.root = root
        self.root.title("Intelligent IDE")
        self.root.geometry("1200x800")

        # Create main frame
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Create left panel for editor
        self.left_panel = ttk.Frame(self.main_frame)
        self.left_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Create right panel for output
        self.right_panel = ttk.Frame(self.main_frame)
        self.right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Create prompt entry
        self.prompt_frame = ttk.LabelFrame(self.left_panel, text="Enter Prompt")
        self.prompt_frame.pack(fill=tk.X, padx=5, pady=5)
        
        self.prompt_entry = scrolledtext.ScrolledText(self.prompt_frame, height=3)
        self.prompt_entry.pack(fill=tk.X, padx=5, pady=5)

        # Create code editor
        self.editor_frame = ttk.LabelFrame(self.left_panel, text="Code Editor")
        self.editor_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.editor = scrolledtext.ScrolledText(self.editor_frame, wrap=tk.NONE)
        self.editor.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        # Create output display
        self.output_frame = ttk.LabelFrame(self.right_panel, text="Output")
        self.output_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.output = scrolledtext.ScrolledText(self.output_frame, wrap=tk.WORD)
        self.output.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        # Create button frame
        self.button_frame = ttk.Frame(self.left_panel)
        self.button_frame.pack(fill=tk.X, padx=5, pady=5)

        # Create progress bar
        self.progress = ttk.Progressbar(self.left_panel, mode='indeterminate')
        self.progress.pack(fill=tk.X, padx=5, pady=5)

        # Create buttons
        self.create_buttons()

    def create_buttons(self):
        button_configs = [
            ("Generate Code", self.generate_code),
            ("Debug Code", self.debug_code),
            ("Run Tests", self.run_tests),
            ("Generate Docs", self.generate_docs),
            ("Clear All", self.clear_all)
        ]

        for text, command in button_configs:
            btn = ttk.Button(self.button_frame, text=text, command=command)
            btn.pack(side=tk.LEFT, padx=5)

    def show_progress(self):
        self.progress.start(10)

    def hide_progress(self):
        self.progress.stop()

    def clear_all(self):
        self.prompt_entry.delete(1.0, tk.END)
        self.editor.delete(1.0, tk.END)
        self.output.delete(1.0, tk.END)

    def update_output(self, text):
        self.output.delete(1.0, tk.END)
        self.output.insert(tk.END, text)

    def run_async(self, func, *args):
        def wrapper():
            try:
                self.show_progress()
                result = func(*args)
                self.root.after(0, self.update_output, result)
            except Exception as e:
                self.root.after(0, self.update_output, f"Error: {str(e)}")
            finally:
                self.hide_progress()

        thread = threading.Thread(target=wrapper)
        thread.start()

    def generate_code(self):
        prompt = self.prompt_entry.get(1.0, tk.END).strip()
        if not prompt:
            messagebox.showwarning("Warning", "Please enter a prompt first!")
            return
        self.run_async(generate_code, prompt)

    def debug_code(self):
        code = self.editor.get(1.0, tk.END).strip()
        if not code:
            messagebox.showwarning("Warning", "No code to debug!")
            return
        self.run_async(debug_code, code)

    def run_tests(self):
        code = self.editor.get(1.0, tk.END).strip()
        if not code:
            messagebox.showwarning("Warning", "No code to test!")
            return
        self.run_async(run_tests, code)

    def generate_docs(self):
        code = self.editor.get(1.0, tk.END).strip()
        if not code:
            messagebox.showwarning("Warning", "No code to document!")
            return
        self.run_async(generate_docs, code)

if __name__ == "__main__":
    root = tk.Tk()
    ide = IntelligentIDE(root)
    root.mainloop()
