import tkinter as tk
from tkinter import ttk, filedialog

import pandas as pd


class InsertNewData(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Insert a base pair number for the grape variety")
        label.pack(pady=10, padx=10)

        # Entry field for user input
        self.variety_entry = tk.Entry(self)
        self.variety_entry.pack()

        # Button to perform the search
        search_button = tk.Button(self, text="Search", command=self.search_variety)
        search_button.pack()

        # Button to upload an external file
        upload_button = tk.Button(self, text="Upload File", command=self.load_external_file)
        upload_button.pack()

        welcome_button = tk.Button(self, text="Go to Home Page", command=lambda: controller.show_frame("WelcomePage"))
        welcome_button.place(x=0, y=0)

    def search_variety(self):
        # Get the user input from the entry field
        user_input = self.variety_entry.get()

        # Load the CSV file and search for the variety
        try:
            df = pd.read_csv("database/Varieties_Ground_Truth.csv")
            result = df[df['Variety'] == user_input]

            if not result.empty:
                # Display the result (you can update this part as needed)
                print(result)
            else:
                print("Variety not found.")

        except FileNotFoundError:
            print("123123")

    def load_external_file(self):
        # Prompt the user to select a CSV file
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])

        if file_path:
            try:
                # Read the file type and handle the case appropriately
                if file_path.endswith(".csv"):
                    df = pd.read_csv(file_path)
                elif file_path.endswith(".xlsx"):
                    df = pd.read_excel(file_path)
                elif file_path.endswith(".txt"):
                    df = pd.read_csv(file_path, sep="\t")
                elif file_path.endswith(".json"):
                    df = pd.read_json(file_path)
                elif file_path.endswith(".xls"):
                    df = pd.read_excel(file_path)
                else:
                    raise FileNotFoundError

                # Load the selected CSV file
                df = pd.read_csv(file_path)

                # Update the existing database with the new data
                try:
                    db = pd.read_csv("../database/Varieties_Ground_Truth.csv")
                    merged_db = pd.concat([db, df], ignore_index=True)
                    merged_db.to_csv("../database/Varieties_Ground_Truth.csv", index=False)
                except FileNotFoundError:
                    # If the database doesn't exist yet, create a new one
                    df.to_csv("../database/Varieties_Ground_Truth.csv", index=False)

                print("File uploaded and merged with the database.")

            except FileNotFoundError:
                print("Selected file not found or is not in appropriate format.")


if __name__ == "__main__":
    app = tk.Tk()
    app.geometry("800x400")  # Set the window size
    app.title("Grape Variety Search")

    frame = InsertNewData(app, None)
    frame.pack(fill="both", expand=True)

    app.mainloop()
