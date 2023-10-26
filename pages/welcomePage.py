import os
import tkinter as tk
import webbrowser
from tkinter import ttk


def open_github_link(event):
    webbrowser.open("https://github.com/ThanosTsiamis/Vinesco", new=2)

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
        image_label.place(x=10, y=90)

        button_style = ttk.Style()
        button_style.configure("TButton", font=("Helvetica", 12))

        settingsButton = ttk.Button(self, text="🔧 Go to Settings Page",
                                    command=lambda: controller.show_frame("SettingsPage"), style="TButton")
        settingsButton.place(relx=1.0, rely=0.0, anchor="ne")

        insertEditGroundTruth = ttk.Button(self, text="Ιnsert/Edit Variety Numbers",
                                           command=lambda: controller.show_frame("InsertNewData"))
        insertEditGroundTruth.pack()

        compareButton = ttk.Button(self, text="Compare against baseline data",
                                   command=lambda: controller.show_frame("CompareData"))
        compareButton.pack()

        # Create the footer frame with a grid layout and multiple rows
        footer_frame = tk.Frame(self)
        footer_frame.pack(side="bottom", fill="x")

        # Left column with "About" and project description
        about_label = tk.Label(footer_frame, text="About")
        about_label.grid(row=0, column=0, padx=(10, 5), sticky="w")

        about_text = tk.Label(footer_frame,
                              text="Vinesco is a software application that aims to automate the detection of grape "
                                   "varieties through DNA analysis. ")
        about_text.grid(row=0, column=1, columnspan=3, padx=(5, 10), sticky="w")

        # Right column with "Links" and the GitHub link
        links_label = tk.Label(footer_frame, text="Code Repository:")
        links_label.grid(row=1, column=0, padx=(10, 5), sticky="w")

        github_link = tk.Label(footer_frame, text="GitHub: https://github.com/ThanosTsiamis/Vinesco", cursor="hand2")
        github_link.grid(row=1, column=1, columnspan=3, padx=(5, 10), sticky="w")
        github_link.bind("<Button-1>", open_github_link)  # Bind the link to the label
