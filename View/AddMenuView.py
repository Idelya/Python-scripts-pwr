from tkinter import *

from View.AddFormView import AddStudentView, AddAdministrationView, AddLecturerView


class AddMenuView(Frame):
    def __init__(self, parent, viewController, storage):
        Frame.__init__(self, parent)
        self.entryPhrase = StringVar()

        label = Label(self, text="Dodaj osobę do listy ")
        label.grid(row=0, column=0, padx=10, pady=10)

        buttonAddStudent = Button(self, text="Dodaj studenta", fg='white', bg='#003f00',height=2, width=15,
                            command=lambda: viewController.show_frame(AddStudentView))

        buttonAddStudent.grid(row=1, column=0, padx=10, pady=5)


        buttonAddAdmin = Button(self, text="Dodaj administracje", fg='white', bg='#003f00', height=2, width=15,
                                  command=lambda: viewController.show_frame(AddAdministrationView))

        buttonAddAdmin.grid(row=2, column=0, padx=10, pady=5)

        buttonAddLecturer = Button(self, text="Dodaj wykładowcę", fg='white', bg='#003f00', height=2, width=15,
                                  command=lambda: viewController.show_frame(AddLecturerView))

        buttonAddLecturer.grid(row=3, column=0, padx=10, pady=5)


        buttonBack = Button(self, text="Powrót", fg='white', bg='#003f00', height=2, width=10,
                             command=lambda: viewController.to_menu())

        buttonBack.grid(row=4, column=0, padx=10, pady=5)