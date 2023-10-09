import tkinter as tk
from tkinter import ttk


class compareData(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Welcome")
        label.pack(pady=10, padx=10)

