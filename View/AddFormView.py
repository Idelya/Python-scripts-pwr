from tkinter import *
from tkcalendar import DateEntry
from Controllers import *


class AddStudentView(Frame):
    def __init__(self, parent, viewController, storage):
        Frame.__init__(self, parent)
        self.storage = storage
        self.viewController = viewController
        self.entryName = StringVar()
        self.entrySurname = StringVar()
        self.entryFaculty = StringVar()
        self.entryPesel = StringVar()
        self.entryIndex = StringVar()

        label = Label(self, text="Podaj dane  studenta")
        label.grid(row=0, column=0, padx=10, pady=10)

        labelName = Label(self, text="Imie: ")
        labelName.grid(row=1, column=0, pady=10)

        entryName = Entry(self, text=self.entryName, fg='black', bg='white', width=10, font=("Calibri", 16))
        entryName.grid(row=1, column=1)

        labelSurname = Label(self, text="Nazwisko: ")
        labelSurname.grid(row=2, column=0, pady=10)

        entrySurname = Entry(self, text=self.entrySurname, fg='black', bg='white', width=10, font=("Calibri", 16))
        entrySurname.grid(row=2, column=1)

        labelBirthday = Label(self, text="Data urodzenia: ")
        labelBirthday.grid(row=3, column=0, pady=10)

        self.birthdayCal = DateEntry(self, width=12, background='darkblue',
                                foreground='white', borderwidth=2)

        self.birthdayCal.grid(row=3, column=1, pady=10)

        labelPesel = Label(self, text="Pesel: ")
        labelPesel.grid(row=4, column=0, pady=10)

        entryPesel = Entry(self, text=self.entryPesel, fg='black', bg='white', width=10, font=("Calibri", 16))
        entryPesel.grid(row=4, column=1)

        labelFaculty = Label(self, text="Wydział: ")
        labelFaculty.grid(row=5, column=0, pady=10)

        entryFaculty = Entry(self, text=self.entryFaculty, fg='black', bg='white', width=10, font=("Calibri", 16))
        entryFaculty.grid(row=5, column=1)

        labelIndex = Label(self, text="Indeks: ")
        labelIndex.grid(row=6, column=0, pady=10)

        entryIndex = Entry(self, text=self.entryIndex, fg='black', bg='white', width=10, font=("Calibri", 16))
        entryIndex.grid(row=6, column=1)

        buttonConfirm = Button(self, text="Potwierdz", fg='white', bg='#003f00', height=2, width=15,
                               command=lambda: self.storage.log_wrapper(self.add_student))

        buttonConfirm.grid(row=7, column=1, padx=10, pady=5)

    def add_student(self):
        stud = self.storage.add_student(
            self.entryName.get(),
            self.entrySurname.get(),
            self.birthdayCal.get_date(),
            self.entryPesel.get(),
            self.entryFaculty.get(),
            self.entryIndex.get())

        self.viewController.to_menu()
        return 'Student: ' + stud.get_full_name()


class AddAdministrationView(Frame):
    def __init__(self, parent, viewController, storage):
        Frame.__init__(self, parent)
        self.storage = storage
        self.viewController = viewController
        self.entryName = StringVar()
        self.entrySurname = StringVar()
        self.entryFaculty = StringVar()
        self.entryPesel = StringVar()
        self.entryOffice = StringVar()

        label = Label(self, text="Podaj dane administracji")
        label.grid(row=0, column=0, padx=10, pady=10)

        labelName = Label(self, text="Imie: ")
        labelName.grid(row=1, column=0, pady=10)

        entryName = Entry(self, text=self.entryName, fg='black', bg='white', width=10, font=("Calibri", 16))
        entryName.grid(row=1, column=1)

        labelSurname = Label(self, text="Nazwisko: ")
        labelSurname.grid(row=2, column=0, pady=10)

        entrySurname = Entry(self, text=self.entrySurname, fg='black', bg='white', width=10, font=("Calibri", 16))
        entrySurname.grid(row=2, column=1)

        labelBirthday = Label(self, text="Data urodzenia: ")
        labelBirthday.grid(row=3, column=0, pady=10)

        self.birthdayCal = DateEntry(self, width=12, background='darkblue',
                                foreground='white', borderwidth=2)

        self.birthdayCal.grid(row=3, column=1, pady=10)

        labelPesel = Label(self, text="Pesel: ")
        labelPesel.grid(row=4, column=0, pady=10)

        entryPesel = Entry(self, text=self.entryPesel, fg='black', bg='white', width=10, font=("Calibri", 16))
        entryPesel.grid(row=4, column=1)

        labelFaculty = Label(self, text="Wydział: ")
        labelFaculty.grid(row=5, column=0, pady=10)

        entryFaculty = Entry(self, text=self.entryFaculty, fg='black', bg='white', width=10, font=("Calibri", 16))
        entryFaculty.grid(row=5, column=1)


        labelEmploy = Label(self, text="Data zatrudnienia: ")
        labelEmploy.grid(row=6, column=0, pady=10)

        self.employmentCal = DateEntry(self, width=12, background='darkblue',
                                foreground='white', borderwidth=2)

        self.employmentCal.grid(row=6, column=1, pady=10)

        labelOffice = Label(self, text="Stanowisko: ")
        labelOffice.grid(row=7, column=0, pady=10)

        entryOffice = Entry(self, text=self.entryOffice, fg='black', bg='white', width=10, font=("Calibri", 16))
        entryOffice.grid(row=7, column=1)

        buttonConfirm = Button(self, text="Potwierdz", fg='white', bg='#003f00', height=2, width=15,
                               command=lambda: self.storage.log_wrapper(self.add_administration))

        buttonConfirm.grid(row=8, column=1, padx=10, pady=5)

    def add_administration(self):
        admin = self.storage.add_administration(
            self.entryName.get(),
            self.entrySurname.get(),
            self.birthdayCal.get_date(),
            self.entryPesel.get(),
            self.entryFaculty.get(),
            self.employmentCal.get_date(),
            self.entryOffice.get())

        self.viewController.to_menu()

        return "Administration: " + admin.get_full_name()

class AddLecturerView(Frame):
    def __init__(self, parent, viewController, storage):
        Frame.__init__(self, parent)
        self.storage = storage
        self.viewController = viewController
        self.entryName = StringVar()
        self.entrySurname = StringVar()
        self.entryFaculty = StringVar()
        self.entryPesel = StringVar()
        self.entryDepartment = StringVar()

        label = Label(self, text="Podaj dane wykładowcę")
        label.grid(row=0, column=0, padx=10, pady=10)

        labelName = Label(self, text="Imie: ")
        labelName.grid(row=1, column=0, pady=10)

        entryName = Entry(self, text=self.entryName, fg='black', bg='white', width=10, font=("Calibri", 16))
        entryName.grid(row=1, column=1)

        labelSurname = Label(self, text="Nazwisko: ")
        labelSurname.grid(row=2, column=0, pady=10)

        entrySurname = Entry(self, text=self.entrySurname, fg='black', bg='white', width=10, font=("Calibri", 16))
        entrySurname.grid(row=2, column=1)

        labelBirthday = Label(self, text="Data urodzenia: ")
        labelBirthday.grid(row=3, column=0, pady=10)

        self.birthdayCal = DateEntry(self, width=12, background='darkblue',
                                foreground='white', borderwidth=2)

        self.birthdayCal.grid(row=3, column=1, pady=10)

        labelPesel = Label(self, text="Pesel: ")
        labelPesel.grid(row=4, column=0, pady=10)

        entryPesel = Entry(self, text=self.entryPesel, fg='black', bg='white', width=10, font=("Calibri", 16))
        entryPesel.grid(row=4, column=1)

        labelFaculty = Label(self, text="Wydział: ")
        labelFaculty.grid(row=5, column=0, pady=10)

        entryFaculty = Entry(self, text=self.entryFaculty, fg='black', bg='white', width=10, font=("Calibri", 16))
        entryFaculty.grid(row=5, column=1)

        labelEmploy = Label(self, text="Data zatrudnienia: ")
        labelEmploy.grid(row=6, column=0, pady=10)

        self.employmentCal = DateEntry(self, width=12, background='darkblue',
                                       foreground='white', borderwidth=2)

        self.employmentCal.grid(row=6, column=1, pady=10)

        labelOffice = Label(self, text="Stanowisko: ")
        labelOffice.grid(row=7, column=0, pady=10)

        entryDepartment = Entry(self, text=self.entryDepartment, fg='black', bg='white', width=10, font=("Calibri", 16))
        entryDepartment.grid(row=7, column=1)

        buttonConfirm = Button(self, text="Potwierdz", fg='white', bg='#003f00', height=2, width=15,
                               command=lambda: self.storage.log_wrapper(self.add_lecturer))

        buttonConfirm.grid(row=8, column=1, padx=10, pady=5)

    def add_lecturer(self):
        lec = self.storage.add_lecturer(
            self.entryName.get(),
            self.entrySurname.get(),
            self.birthdayCal.get_date(),
            self.entryFaculty.get(),
            self.entryPesel.get(),
            self.employmentCal.get_date(),
            self.entryDepartment.get())

        self.viewController.to_menu()
        return "Lecturer: " + lec.get_full_name()
