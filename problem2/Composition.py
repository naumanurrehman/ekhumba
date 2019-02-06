class Salary:
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus

    def annual_salary(self):
        return (self.pay+self.bonus)*12


class Employee:
    def __init__(self, name, age, pay, bonus):
        self.name = name
        self.age = age
        self.obj_salary = Salary(pay, bonus)

    def calculate_salary(self):
        return self.obj_salary.annual_salary()


emp = Employee("Shakir", 23, 45000, 5000)
print(emp.calculate_salary())
