from Employee import Employee


class Administration(Employee):
    def __init__(self, name, surname, birthdate, pesel, faculty, employment_date, office):
        self.office = office
        super().__init__(name, surname, birthdate, pesel, faculty, employment_date)

    def print_data(self):
        print("Administration")
        super(Administration, self).print_data()
        print("Office: ", self.office)

