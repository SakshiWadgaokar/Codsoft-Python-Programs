import tkinter as tk
from tkinter import filedialog, messagebox

class SmartTextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Smart Text Editor")
        self.text_area = tk.Text(self.root, wrap="word", undo=True)
        self.text_area.pack(expand=True, fill="both")
        self.main_menu = tk.Menu(root)
        self.root.config(menu=self.main_menu)
        self.file_menu = tk.Menu(self.main_menu, tearoff=False)
        self.main_menu.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_command(label="Save As", command=self.save_as_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=root.destroy)

    def new_file(self):
        self.text_area.delete(1.0, tk.END)

    def open_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, "r") as file:
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, file.read())

    def save_file(self):
        content = self.text_area.get(1.0, tk.END).strip()
        if not content:
            messagebox.showwarning("Warning", "There is no content to save.")
        else:
            file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
            if file_path:
                with open(file_path, "w") as file:
                    file.write(content)

    def save_as_file(self):
        content = self.text_area.get(1.0, tk.END).strip()
        if not content:
            messagebox.showwarning("Warning", "There is no content to save.")
        else:
            file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
            if file_path:
                with open(file_path, "w") as file:
                    file.write(content)

def main():
    root = tk.Tk()
    app = SmartTextEditor(root)
    root.mainloop()

if __name__ == "__main__":
    main()
