from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
from tkinter import filedialog, messagebox, scrolledtext
from TextLib import *


class MainView(Frame):

    def __init__(self, root, viewController):
        Frame.__init__(self, root)
        self.viewController = viewController
        self.text = ''
        self.text_area = scrolledtext .ScrolledText(self, width=75, height=20, font=("Times New Roman", 15))

        self.text_area.grid(row=1, column=0, columnspan=10, rowspan=10, pady=20, padx=20)
        self.text_area.configure(state='disabled')
        self.entryEmail = StringVar()
        self.create_widgets()

    def create_widgets(self):
        self.buttonImport = Button(self, text='Importuj plik ', fg='white', bg='#003f00',
                                command=lambda: self.import_text(), height=2, width=15)
        self.buttonImport.grid(row=0, column=0)

        self.buttonAnalysis = Button(self, text='Analysis', fg='white', bg='#003f00',
                                   command=lambda: analysis(self.text), height=2, width=15)
        self.buttonAnalysis.grid(row=0, column=1)

        self.buttonChart = Button(self, text='Wykres', fg='white', bg='#003f00',
                                   command=lambda: self.drawChart(), height=2, width=15)
        self.buttonChart.grid(row=0, column=2)

        self.labelEmail = Label(self, text="Email: ")
        self.labelEmail.grid(row=0, column=6)

        self.entryEmail = Entry(self, text=self.entryEmail, fg='black', bg='white', width=30, font=("Times New Roman", 15))
        self.entryEmail.grid(row=0, column=7, columnspan="2")

        self.buttonFind = Button(self, text='Find mail', fg='white', bg='#003f00',
                                   command=lambda: self.find_mail(), height=2, width=15)
        self.buttonFind.grid(row=0, column=9)



    def import_text(self):
        filename = filedialog.askopenfilename(title="Wybierz plik",
                                              filetypes=[("", "*.txt")])

        self.text = open_file(filename)
        self.text_area.configure(state="normal")
        self.text_area.delete("1.0", END)
        self.text_area.insert(INSERT, self.text)
        self.text_area.configure(state='disabled')


    def find_mail(self):
        mail = self.entryEmail.get()
        if len(self.text) == 0:
            messagebox.showerror(title="Error", message="Zaimportuj plik!")
            return

        if len(mail) == 0 or not isMail(mail):
            messagebox.showerror(title="Error", message="Mail jest nie prawidłowy")
            return
        isInText = find_word(mail, self.text)
        if isInText:
            messagebox.showinfo(title="Szukaj", message="Znaleziono mail " + mail + "w tekscie")
        else:
            messagebox.showinfo(title="Szukaj", message="Mail " + mail + "nie znaleziony")

    def drawChart(self):
        bars = ('oznajmiające', 'pytające', 'rozkazujące')
        counted = count_sentences(self.text)
        y_pos = np.arange(len(counted))

        plt.figure(figsize=(10, 5))

        plt.bar(y_pos, counted, color='#003f00')

        plt.xticks(y_pos, bars)

        plt.xlabel('Rodzaj', fontsize=12, color='#323232')
        plt.ylabel('Ilość', fontsize=12, color='#323232')
        plt.title('Zdania w tekście', fontsize=16, color='#323232')

        plt.show()


