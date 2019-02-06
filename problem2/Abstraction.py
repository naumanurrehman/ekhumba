from abc import ABC, abstractmethod


class Base(ABC):
    def __init__(self, fn, ln, ad):
        self.first_name = fn
        self.last_name = ln
        self.address = ad

    @abstractmethod
    def calculate_salary(self):
        pass


class FullTimeEmployee(Base):
    def __init__(self, fn, ln, ad, ms):
        self.monthly_salary = ms
        super().__init__(fn, ln, ad)

    def calculate_salary(self):
        return self.monthly_salary*12


class ContractBasedEmployee(Base):
    def __init__(self, fn, ln, ad, hw, hs):
        self.hours_worked = hw
        self.hourly_salary = hs
        super().__init__(fn, ln, ad)

    def calculate_salary(self):
        return self.hourly_salary*self.hours_worked*22*12


Shakir = FullTimeEmployee("SHAKIR", "MAHMOOD", "Dhoke Paracha", 60000)
Nomi = ContractBasedEmployee("NOMI", "TOMMY", "Dhoke Hasu", 2, 100)
print(Shakir.first_name, Shakir.last_name, "salary :", Shakir.calculate_salary())
print(Nomi.first_name, Nomi.last_name, "salary :", Nomi.calculate_salary())

