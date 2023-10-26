import csv
import tkinter as tk
from tkinter import messagebox


class SettingsPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Settings Page")
        label.pack(pady=10, padx=10)

        # Create a function to handle the delete action
        def delete_data():
            confirm = messagebox.askyesno("Confirmation",
                                          "Are you sure you want to delete all data "
                                          "inside Varieties Ground Truth?"
                                          "WARNING: Data cannot be recovered after "
                                          "deletion."
                                          " This action is irreversible.",
                                          icon='warning')
            if confirm:
                with open("database/Varieties_Ground_Truth.csv", 'w', newline='') as csvfile:
                    # Create a CSV writer object
                    csv_writer = csv.writer(csvfile)

                    # Write an empty list to clear the contents
                    csv_writer.writerows([])

                print("Data deleted!")

        # Create a button for deleting data
        deleteButton = tk.Button(self, text="Delete Data", command=delete_data)
        deleteButton.pack()

        welcomeButton = tk.Button(self, text="🏠 Go to Home Page", command=lambda: controller.show_frame("WelcomePage"))
        welcomeButton.place(x=0, y=0)
