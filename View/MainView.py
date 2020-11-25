from tkinter import *

from View.AddFormView import AddStudentView, AddAdministrationView, AddLecturerView
from View.AddMenuView import AddMenuView
from View.MenuView import MenuView


class MainView(Tk):

    def __init__(self, storage, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.storage = storage
        container = Frame(self)
        container.pack()

        self.frames = {}

        for F in (AddMenuView, MenuView, AddStudentView, AddAdministrationView, AddLecturerView):
            frame = F(container, self, storage)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(MenuView)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise() # Raise this widget in the stacking order.

    def to_menu(self):
        self.show_frame(MenuView)


