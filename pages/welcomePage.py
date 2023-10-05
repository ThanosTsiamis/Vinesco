import tkinter as tk
from tkinter import ttk


class WelcomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Welcome")
        label.pack(pady=10, padx=10)
        settingsButton = ttk.Button(self, text="Go to Settings Page", command=lambda: controller.show_frame("SettingsPage"))
        settingsButton.pack()
        page3Button = ttk.Button(self, text="Go to Page 3", command=lambda: controller.show_frame("InsertNewData"))
        page3Button.pack()
