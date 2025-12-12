import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.scrolledtext import ScrolledText
from RANDOMGEN import gen_entries

class GeneratorGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Random Entry Generator")
        self.geometry("650x500")
        self.create_widgets()

    
    def create_widgets(self):
        top = ttk.Frame(self, padding = 10)
        top.pack(fill="x")

        ttk.Label(top, text = "Number of entries:").pack(side="left")
        self.num_var = tk.IntVar(value=5)
        ttk.Spinbox(top, from_ =1, to =1000, textvariable = self.num_var, width=8).pack(side="left", padx=5)

        ttk.Button(top, text="Generate", command=self.generate).pack(side="left", padx=10)

        self.box = ScrolledText(self, wrap="word", height =20)
        self.box.pack(fill="both", expand=True, padx=10, pady=5)

    def generate(self):
        n = self.num_var.get()
        if n<=0:
            messagebox.showerror("Error", "Enter a valid number which is greater than 0")
            return
    
        data =gen_entries(n)
        self.box.delete("1.0", "end")

        for i, e in enumerate(data, 1):
            self.box.insert("end", f"Entry {i}\n")
            self.box.insert("end", f"Name: {e['Name']}\n")
            self.box.insert("end", f"Email: {e['E-Mail']}\n")
            self.box.insert("end", f"Password: {e['Password']}\n")
            self.box.insert("end", f"end", "-"*40 + "\n")

if __name__ == "__main__":
    app = GeneratorGUI()
    app.mainloop()

