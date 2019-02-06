class Salary:
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus

    def annual_salary(self):
        return (self.pay+self.bonus)*12


class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def calculate_salary(self):
        return self.salary.annual_salary()


salary = Salary(45000, 5000)
emp = Employee("Shakir", 23, salary)
print(emp.calculate_salary())
