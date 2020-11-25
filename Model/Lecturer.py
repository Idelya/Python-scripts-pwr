from Model.Employee import Employee


class Lecturer(Employee):

    def __init__(self, name, surname, birthdate, pesel, faculty, employment_date, department):
        self.department = department
        super().__init__(name, surname, birthdate, pesel, faculty, employment_date)

    def print_data(self):
        print("Lecturer")
        data = super(Lecturer, self).print_data()
        print("Department:", self.department)

        return data