import tkinter as tk


class SettingsPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Settings Page")
        label.pack(pady=10, padx=10)
        welcomeButton = tk.Button(self, text="Go to Welcome Page", command=lambda: controller.show_frame("WelcomePage"))
        welcomeButton.pack()
