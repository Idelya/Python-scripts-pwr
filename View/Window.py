from tkinter import *

from View.MainView import MainView


class Window(Tk):

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        container = Frame(self)
        container.pack()

        self.frames = {}

        for F in (MainView, MainView):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(MainView)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def to_menu(self):
        self.show_frame(MainView)
