import os
import tkinter as tk
from tkinter import filedialog

import pandas as pd


class CompareData(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Compare against baseline data")
        label.pack(pady=10, padx=10)

        # Button to upload an external file
        upload_button = tk.Button(self, text="Upload File", command=self.load_external_file)
        upload_button.pack()

        # Field to enter the variety name
        self.variety_entry = tk.Entry(self)
        self.variety_entry.pack()

        # Button to perform the Comparison
        search_button = tk.Button(self, text="Compare", command=self.verify_variety)
        search_button.pack()

        # Label to display various messages
        self.message = tk.Label(self, text="")
        self.message.pack()

        # Numeric entry field for the allowed difference
        self.allowed_difference = tk.Entry(self, textvariable=tk.IntVar())
        self.allowed_difference.pack()

    def load_external_file(self):
        file_path = filedialog.askopenfilename()

        if file_path:
            try:
                # Read the file type and handle the case appropriately
                if file_path.endswith(".csv"):
                    self.df = pd.read_csv(file_path)
                elif file_path.endswith(".xlsx"):
                    self.df = pd.read_excel(file_path)
                elif file_path.endswith(".txt"):
                    self.df = pd.read_csv(file_path, sep="\t")
                elif file_path.endswith(".json"):
                    self.df = pd.read_json(file_path)
                elif file_path.endswith(".xls"):
                    self.df = pd.read_excel(file_path)
                else:
                    raise FileNotFoundError

                self.message.config(text="Dataset loaded successfully")
            except FileNotFoundError:
                self.message.config(text="Selected file not found or is not in appropriate format.")

    def verify_variety(self):
        # Get the user input from the Entry field
        user_input = self.variety_entry.get()
        # Check if the DataFrame has been loaded
        if hasattr(self, 'df'):
            # Rename the first column to Sample
            self.df.rename(columns={self.df.columns[0]: "Sample"}, inplace=True)
            # Search for the user input in the DataFrame
            result = self.df[self.df[
                                 'Sample'] == user_input]

            if not result.empty:
                # Check if a match is found
                print("Variety found:", result)
                # Correct the variety numbers based on the ground truth file
                csv_file_path = os.path.join(os.path.join(os.path.expanduser("~"), "Vinesco"), "database",
                                             "Varieties_Ground_Truth.csv")
                try:
                    varieties_ground_truth_df = pd.read_csv(csv_file_path)
                except FileNotFoundError:
                    self.message.config(text="No ground truth numbers file found. No correction will be applied.")
                    varieties_ground_truth_df = None
                if varieties_ground_truth_df is not None:
                    difs = {}
                    for column in result:
                        if column != 'Sample' and column in varieties_ground_truth_df.columns:
                            if user_input in varieties_ground_truth_df['Variety'].values:
                                difs[column] = varieties_ground_truth_df.loc[
                                                   varieties_ground_truth_df['Variety'] == user_input, column].iloc[0] - \
                                               result[column].iloc[0]

                # Based on the keys of the difs dictionary, update the values in the self.df DataFrame by adding or
                # subtracting the difference
                for key in difs:
                    self.df[key] = self.df[key] + difs[key]
                print(self.df)

                # Create a dictionary to store the close matches
                close_match = {}
                # If the user has entered a value for the allowed difference, use it. Otherwise, use 2
                if self.allowed_difference.get():
                    allowed_difference = int(self.allowed_difference.get())
                else:
                    allowed_difference = 2
                for column in result:
                    # Don't fetch the column that is used for the search
                    if column != 'Sample':
                        upper_bound = result[column].iloc[0] + allowed_difference
                        lower_bound = result[column].iloc[0] - allowed_difference
                        close_match[column] = self.df.index[self.df[column].between(lower_bound, upper_bound)].tolist()
                print("Close matches:", close_match)
                # The close match contains indices that are close enough to the original match.
                # We create a new df that has True in the indices that are close enough and False in the rest.
                new_df = pd.DataFrame(index=self.df.index)
                for column in close_match:
                    new_df[column] = new_df.index.isin(close_match[column])
                # In this new df we sum the number of True values for each row.
                # If the sum is almost equal to the number of columns, then all the values are close enough.
                new_df['sum'] = new_df.sum(axis=1)
                print(new_df)
                print("123")
            else:
                self.message.config(text="Variety not found in the dataset. Make sure the spelling is correct.")
        else:
            self.message.config(text="No dataset loaded. Please upload a dataset first.")


if __name__ == "__main__":
    app = tk.Tk()
    app.geometry("800x400")  # Set the window size
    app.title("Grape Variety Search")

    frame = CompareData(app, None)
    frame.pack(fill="both", expand=True)

    app.mainloop()
