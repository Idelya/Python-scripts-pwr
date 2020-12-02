from tkinter import *
import os
from PIL import ImageTk, Image
from tkinter import filedialog, simpledialog

from View.AddMenuView import AddMenuView

class MenuView(Frame):

    def __init__(self, root, viewController, storage):
        Frame.__init__(self, root)
        self.storage = storage
        self.viewController = viewController
        self.pwr_list = Listbox(self, height=8, width=50, border=0)
        self.pwr_list.grid(row=6, column=0, columnspan=2, rowspan=6, pady=20, padx=20)
        self.addBackground()
        self.create_widgets()


    def addBackground(self):
        script_dir = os.path.dirname(__file__)
        rel_path = "../assets/logo_pwr.png"
        abs_file_path = os.path.join(script_dir, rel_path)
        logo = Image.open(abs_file_path)
        img = logo.resize((400, 100), Image.ANTIALIAS)
        logo_bg = ImageTk.PhotoImage(img)
        self.background_label = Label(self, image=logo_bg, bg='white')
        self.background_label.image = logo_bg
        self.background_label.grid(row=0, column=0, columnspan=3)

    def create_widgets(self):
        self.buttonAdd = Button(self, text=' Dodaj ', fg='white', bg='#003f00',
                                command=lambda: self.viewController.show_frame(AddMenuView), height=2, width=15)
        self.buttonAdd.grid(row=1, column=0)

        self.buttonSortAge = Button(self, text=' Sortuj po wieku ', fg='white', bg='#003f00',
                                command=lambda: self.storage.sort_by_age(), height=2, width=15)
        self.buttonSortAge.grid(row=1, column=1)

        self.buttonSortSurname = Button(self, text=' Sortuj po nazwisku ', fg='white', bg='#003f00',
                                    command=lambda: self.storage.sort_by_surname(), height=2, width=15)
        self.buttonSortSurname.grid(row=2, column=0)

        self.buttonDelete = Button(self, text=' Usuń ', fg='white', bg='#003f00',
                                        command=lambda: self.remove(), height=2, width=15)
        self.buttonDelete.grid(row=2, column=1)

        self.buttonCopy = Button(self, text=' Kopiuj ', fg='white', bg='#003f00',
                                        command=lambda: self.copyByAge(), height=2, width=15)
        self.buttonCopy.grid(row=3, column=0)

        self.buttonSave = Button(self, text=' Zapisz ', fg='white', bg='#003f00',
                                 command=lambda: self.save_list(), height=2, width=15)
        self.buttonSave.grid(row=3, column=1)

        self.buttonImport = Button(self, text=' Import ', fg='white', bg='#003f00',
                                 command=lambda: self.import_list(), height=2, width=15)
        self.buttonImport.grid(row=4, column=0)

        self.buttonRefresh = Button(self, text=' Odswiez ', fg='white', bg='#003f00',
                                   command=lambda: self.refresh(), height=2, width=15)
        self.buttonRefresh.grid(row=4, column=1)


        self.scrollbar = Scrollbar(self)
        self.scrollbar.grid(row=6, column=2)

        self.pwr_list.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.configure(command=self.pwr_list.yview)

        self.list_update()

    def list_update(self):
        for i in range(0, len(self.storage.pwr_list)):
            print(self.storage.pwr_list[i].name)
            p = self.storage.pwr_list[i]
            self.pwr_list.insert(END, str(i+1) +" " + p.print_data() +" - " +type(p).__name__)

    def refresh(self):
        self.pwr_list.delete(0, END)
        self.list_update()

    def save_list(self):
        filename = filedialog.asksaveasfilename(filetypes=[("Plik", "*.p")])

        self.storage.save_list(filename)

    def import_list(self):
        filename = filedialog.askopenfilename(title="Wybierz plik",
                                              filetypes=[("", "*.p")])

        self.storage.fetch_data(filename)
        self.list_update()

    def remove(self):
        pesel = simpledialog.askstring('Usun', "Podaj pesel:")

        self.storage.remove_by_pesel(pesel)

    def copyByAge(self):
        age = simpledialog.askfloat('Usun', "Podaj maks. wiek:")

        self.storage.copy_by_age(age)

