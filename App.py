from tkinter import *
from Calculator import *
from tkinter import filedialog, messagebox
#3*2+(6-5)+2^2

class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.entryPhrase = StringVar()
        self.messageText = StringVar()
        self.calc = Calculator()
        self.phrase = ''
        self.master = master
        self.master.title = "Calculator"
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.messageText.set('')
        self.entry = Entry(self, text=self.entryPhrase, fg='black', bg='white', width=30, font=("Calibri", 16))
        self.entry.grid(row=0, column=0, columnspan=10)

        self.message = Label(self, textvariable=self.messageText, fg='red', width=30, font=("Calibri", 13))
        self.message.grid(row=1, column=0, columnspan=10)

        self.button1 = Button(self, text=' 1 ', fg='white', bg='black',
                              command=lambda: self.clickedButton(1), height=3, width=7)
        self.button1.grid(row=2, column=0)

        self.button2 = Button(self, text=' 2 ', fg='white', bg='black',
                              command=lambda: self.clickedButton(2), height=3, width=7)
        self.button2.grid(row=2, column=1)

        self.button3 = Button(self, text=' 3 ', fg='white', bg='black',
                              command=lambda: self.clickedButton(3), height=3, width=7)
        self.button3.grid(row=2, column=2)

        self.button4 = Button(self, text=' 4 ', fg='white', bg='black',
                              command=lambda: self.clickedButton(4), height=3, width=7)
        self.button4.grid(row=3, column=0)

        self.button5 = Button(self, text=' 5 ', fg='white', bg='black',
                              command=lambda: self.clickedButton(5), height=3, width=7)
        self.button5.grid(row=3, column=1)

        self.button6 = Button(self, text=' 6 ', fg='white', bg='black',
                              command=lambda: self.clickedButton(6), height=3, width=7)
        self.button6.grid(row=3, column=2)

        self.button7 = Button(self, text=' 7 ', fg='white', bg='black',
                              command=lambda: self.clickedButton(7), height=3, width=7)
        self.button7.grid(row=4, column=0)

        self.button8 = Button(self, text=' 8 ', fg='white', bg='black',
                              command=lambda: self.clickedButton(8), height=3, width=7)
        self.button8.grid(row=4, column=1)

        self.button9 = Button(self, text=' 9 ', fg='white', bg='black',
                              command=lambda: self.clickedButton(9), height=3, width=7)
        self.button9.grid(row=4, column=2)

        self.buttonAdd = Button(self, text=' + ', fg='white', bg='black',
                                command=lambda: self.clickedOperator('+'), height=3, width=7)
        self.buttonAdd.grid(row=2, column=3)

        self.buttonDiff = Button(self, text=' - ', fg='white', bg='black',
                                command=lambda: self.clickedOperator('-'), height=3, width=7)
        self.buttonDiff.grid(row=3, column=3)

        self.buttonMul = Button(self, text=' * ', fg='white', bg='black',
                                command=lambda: self.clickedOperator('*'), height=3, width=7)
        self.buttonMul.grid(row=4, column=3)

        self.buttonDiv = Button(self, text=' / ', fg='white', bg='black',
                                command=lambda: self.clickedOperator('/'), height=3, width=7)
        self.buttonDiv.grid(row=2, column=4)

        self.buttonLBracket = Button(self, text=' ( ', fg='white', bg='black',
                                command=lambda: self.clickedOperator('('), height=3, width=7)
        self.buttonLBracket.grid(row=3, column=4)

        self.buttonRBracket = Button(self, text=' ) ', fg='white', bg='black',
                                     command=lambda: self.clickedOperator(')'), height=3, width=7)
        self.buttonRBracket.grid(row=4, column=4)

        self.buttonSqrt = Button(self, text=' sqrt ', fg='white', bg='black',
                                command=lambda: self.clickedFunction('sqrt'), height=3, width=7)
        self.buttonSqrt.grid(row=2, column=5)

        self.buttonPow = Button(self, text=' ^ ', fg='white', bg='black',
                                  command=lambda: self.clickedOperator('^'), height=3, width=7)
        self.buttonPow.grid(row=3, column=5)

        self.buttonDot = Button(self, text=' . ', fg='white', bg='black',
                                command=lambda: self.clickedOperator('.'), height=3, width=7)
        self.buttonDot.grid(row=4, column=5)

        self.buttonSin = Button(self, text=' sin ', fg='white', bg='black',
                                command=lambda: self.clickedFunction('sin'), height=3, width=7)
        self.buttonSin.grid(row=5, column=0)

        self.buttonCos = Button(self, text=' cos ', fg='white', bg='black',
                                command=lambda: self.clickedFunction('cos'), height=3, width=7)
        self.buttonCos.grid(row=5, column=1)

        self.buttonLn = Button(self, text=' ln ', fg='white', bg='black',
                                command=lambda: self.clickedFunction('ln'), height=3, width=7)
        self.buttonLn.grid(row=5, column=2)

        self.buttonClear = Button(self, text=' C ', fg='white', bg='black',
                                  command=lambda: self.clear(), height=3, width=7)
        self.buttonClear.grid(row=5, column=3)

        self.buttonCount = Button(self, text=' = ', fg='white', bg='purple',
                                     command=lambda: self.count(), height=3, width=15)
        self.buttonCount.grid(row=5, column=4, columnspan=2)


        self.buttonNormDistr = Button(self, text=' Normal distribution  ', fg='white', bg='black',
                                     command=lambda: self.normaDistr(), height=3, width=48)
        self.buttonNormDistr.grid(row=6, column=0, columnspan=6)

    def clickedButton(self, number: int):
        phrase = self.entryPhrase.get() + str(number)
        self.entryPhrase.set(phrase)

    def clickedOperator(self, operator: str):
        phrase = self.entryPhrase.get() + str(operator)
        self.entryPhrase.set(phrase)

    def clickedFunction(self, function: str):
        res = self.calc.countFunction(self.entryPhrase.get(), function)
        self.phrase = res
        self.entryPhrase.set(self.phrase)

    def clear(self):
        phrase = ''
        self.entryPhrase.set(phrase)

    def count(self):
        try:
            res = self.calc.count(self.entryPhrase.get())
            self.phrase = res
            self.entryPhrase.set(self.phrase)
            self.messageText.set('')
        except Exception as e:
            self.messageText.set('Error: ' + str(e))

    def normaDistr(self):
        filename = filedialog.askopenfilename(initialdir="/",
                                              title="Select a File",
                                              filetypes=[("Text files", "*.txt")])
        if filename != '':
            dataFloat =[]
            file = open(filename, 'r')
            series = file.read()
            dataList = series.split()
            for i in dataList:
                dataFloat.append(float(i))
            (statics, pvalue) = self.calc.normaDistribution(dataFloat)
            print(pvalue)
            if pvalue < 0.05:
                resText = "It's not normal distribution"
            else:
                resText = "It is normal distribution"
            messagebox.showinfo(title="Normal distribution",
                                message="Statics (W): " + str(round(statics, 4)) + ", value (p): " + str(round(pvalue, 4)) + ". " + resText)

