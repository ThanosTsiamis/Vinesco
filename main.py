import tkinter as tk

from pages.compareData import CompareData
from pages.insertNewData import InsertNewData
from pages.settingsPage import SettingsPage
from pages.welcomePage import WelcomePage


class MainApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for PageClass in (WelcomePage, SettingsPage, InsertNewData, CompareData):
            page_name = PageClass.__name__
            frame = PageClass(container, self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("WelcomePage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


if __name__ == "__main__":
    app = MainApp()
    # TODO: Add the ico image
    app.title("Vinesco")
    app.geometry("800x400")  # Set the window size
    app.mainloop()
