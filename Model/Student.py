from Model.Person import Person


class Student(Person):

    def __init__(self, name, surname, birthdate, pesel, faculty, index):
        self.index = index
        super().__init__(name, surname, birthdate, pesel, faculty)

    def print_data(self):
        print("Student")
        data = super(Student, self).print_data()
        print("index:", str(self.index))
        return data