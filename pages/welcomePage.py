import os
import tkinter as tk
from tkinter import ttk


class WelcomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Welcome")
        label.pack(pady=10, padx=10)
        self.app_directory = os.path.join(os.path.expanduser("~"), "Vinesco")
        # Check if the directory exists; if not, create it
        if not os.path.exists(self.app_directory):
            os.makedirs(self.app_directory)

        # Copy the database directory to the app directory
        database_directory = os.path.join(self.app_directory, "database")
        if not os.path.exists(database_directory):
            os.makedirs(database_directory)
        database_file = os.path.join(database_directory, "Varieties_Ground_Truth.csv")
        if not os.path.exists(database_file):
            import shutil
            shutil.copy(os.path.join("database", "Varieties_Ground_Truth.csv"), database_file)
        settingsButton = ttk.Button(self, text="Go to Settings Page", command=lambda: controller.show_frame("SettingsPage"))
        settingsButton.pack()
        page3Button = ttk.Button(self, text="Ιnsert/Edit Variety Numbers", command=lambda: controller.show_frame("InsertNewData"))
        page3Button.pack()
