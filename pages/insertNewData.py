import tkinter as tk
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

        welcomeButton = tk.Button(self, text="Go to Home Page", command=lambda: controller.show_frame("WelcomePage"))
        # Put the welcome Button on the upper left side of the screen
        welcomeButton.place(x=0, y=0)

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
            print("CSV file not found.")