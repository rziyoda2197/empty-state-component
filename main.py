import tkinter as tk
from tkinter import ttk

class EmptyStateComponent:
    def __init__(self, root):
        self.root = root
        self.root.title("Empty State Component")
        self.root.geometry("800x600")

        self.illustration = tk.Label(self.root, text="Illustration", font=("Arial", 24))
        self.illustration.pack(pady=100)

        self.call_to_action = tk.Button(self.root, text="Call to Action", command=self.on_call_to_action)
        self.call_to_action.pack(pady=20)

    def on_call_to_action(self):
        print("Call to action clicked")

if __name__ == "__main__":
    root = tk.Tk()
    component = EmptyStateComponent(root)
    root.mainloop()
