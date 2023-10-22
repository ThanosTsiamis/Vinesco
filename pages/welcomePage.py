import os
import tkinter as tk
from tkinter import ttk


class WelcomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # We need big bold letters for the welcome. And use a different font.
        label = tk.Label(self, text="Vinesco: An automated matching system", font=("Helvetica", 16))
        label.pack(side="top", anchor="nw")
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

        subtext = tk.Label(self, text=" Unveiling Grape Varieties Through DNA Analysis", font=("Helvetica", 12),
                           fg="gray")
        subtext.place(x=50, y=50)
        image = tk.PhotoImage(file=os.path.join("resources", "Vinesco.png"))
        image = image.subsample(2, 2)
        image_label = tk.Label(self, image=image)
        image_label.image = image
        image_label.pack(pady=10, padx=10)

        button_style = ttk.Style()
        button_style.configure("TButton", font=("Helvetica", 12))

        settingsButton = ttk.Button(self, text="🔧 Go to Settings Page",
                                    command=lambda: controller.show_frame("SettingsPage"), style="TButton")
        settingsButton.pack(ipady=10, ipadx=10)

        insertEditGroundTruth = ttk.Button(self, text="Ιnsert/Edit Variety Numbers",
                                           command=lambda: controller.show_frame("InsertNewData"))
        insertEditGroundTruth.pack()

        compareButton = ttk.Button(self, text="Compare against baseline data",
                                   command=lambda: controller.show_frame("CompareData"))
        compareButton.pack()

        # Footer Frame
        footer_frame = tk.Frame(self)
        footer_frame.pack(side="bottom", fill="x")

        # Add labels or buttons in the footer as needed, for example:
        github_link = tk.Label(footer_frame, text="GitHub: https://github.com/your_username/Vinesco")
        github_link.pack(side="left", padx=10)

        about_link = tk.Label(footer_frame, text="About Us")
        about_link.pack(side="right", padx=10)