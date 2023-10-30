import csv
import os
import tkinter as tk
from tkinter import messagebox


class SettingsPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Settings Page")
        label.pack(pady=10, padx=10)

        # label to display that the data is deleted
        self.message = tk.Label(self, text="")
        self.message.pack()

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
                try:
                    with open("database/Varieties_Ground_Truth.csv", 'w', newline='') as csvfile:
                        # Create a CSV writer object
                        csv_writer = csv.writer(csvfile)

                        # Write an empty list to clear the contents
                        csv_writer.writerows([])

                    # Also delete the data from the persistent storage
                    self.app_directory = os.path.join(os.path.expanduser("~"), "Vinesco")
                    database_directory = os.path.join(self.app_directory, "database")
                    database_file = os.path.join(database_directory, "Varieties_Ground_Truth.csv")
                    with open(database_file, 'w', newline='') as csvfile:
                        # Create a CSV writer object
                        csv_writer = csv.writer(csvfile)

                        # Write an empty list to clear the contents
                        csv_writer.writerows([])

                    self.message.config(text="Data deleted successfully")

                #         catch the error if the file is open which is permission denied
                except PermissionError:
                    self.message.config(text="Data not deleted. Make sure the file is not open in another window.")

        # Create a button for deleting data
        deleteButton = tk.Button(self, text="Delete Data", command=delete_data)
        deleteButton.pack()

        welcomeButton = tk.Button(self, text="🏠 Go to Home Page", command=lambda: controller.show_frame("WelcomePage"))
        welcomeButton.place(x=0, y=0)
