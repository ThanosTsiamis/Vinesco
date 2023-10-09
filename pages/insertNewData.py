import tkinter as tk
from tkinter import filedialog, messagebox

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

        # Label to display the result
        self.result_label = tk.Label(self, text="")
        self.result_label.pack()

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
                self.result_label.config(text=result.to_string(index=False))
                edit_button = tk.Button(self, text="Edit", command=lambda: self.edit_result(user_input))
                edit_button.pack()
            else:
                response = messagebox.askyesno("Variety Not Found",
                                               "Variety not found in database. Do you want to add it?")
                if response:
                    # Add the new variety to the database
                    new_row = pd.DataFrame({'Variety': [user_input]})
                    df = pd.concat([df, new_row], ignore_index=True)
                    df.to_csv("database/Varieties_Ground_Truth.csv", index=False)
                    self.result_label.config(text="Variety added to database.")
        except FileNotFoundError:
            self.result_label.config(text=f"File not found.Make sure the database exists.")

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

    def edit_result(self, user_input):
        """Open a new window to edit the result. A text input should be displayed that searches for the column in the
        dataset. If the column is found, the user should be able to edit the value. If not, a new column should be
        created."""
        # Create a new window
        window = tk.Toplevel(self)
        window.title("Edit Result")

        # Create a label to display the result
        result_label = tk.Label(window, text=f"Variety: {user_input}")
        result_label.pack()

        # Create a text input to search for the column
        column_entry = tk.Entry(window)
        column_entry.pack()

        # Create a text input to edit the value
        value_entry = tk.Entry(window)
        value_entry.pack()

        # Create a button to perform the search
        search_button = tk.Button(window, text="Enter DNA marker/value", command=lambda: self.edit_result_search(column_entry.get(),
                                                                                                 value_entry.get(),
                                                                                                 user_input))
        search_button.pack()

    def edit_result_search(self, column, value, user_input):
        """Search for the column in the dataset. If the column is found, the user should be able to edit the value. If
        not, a new column should be created."""
        try:
            df = pd.read_csv("database/Varieties_Ground_Truth.csv")
            result = df[df['Variety'] == user_input]

            if not result.empty:
                # If the column exists, edit the value
                df.loc[df['Variety'] == user_input, column] = value
                df.to_csv("database/Varieties_Ground_Truth.csv", index=False)
                self.result_label.config(text="Value updated.")
            else:
                # If the column doesn't exist, create a new one
                df[column] = value
                df.to_csv("database/Varieties_Ground_Truth.csv", index=False)
                self.result_label.config(text="Column created.")
        except FileNotFoundError:
            self.result_label.config(text=f"File not found.Make sure the database exists.")


if __name__ == "__main__":
    app = tk.Tk()
    app.geometry("800x400")  # Set the window size
    app.title("Grape Variety Search")

    frame = InsertNewData(app, None)
    frame.pack(fill="both", expand=True)

    app.mainloop()
