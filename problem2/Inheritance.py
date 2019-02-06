class Cls1:
    def add(self, op1, op2):
        print(op1+op2)


class Cls2(Cls1):
    @staticmethod
    def mul(op1, op2):
        return op1*op2

    def add(self, op1, op2):
        print(op1-op2)

    def task(self, a, b):
        super().add(self.mul(a, a), self.mul(b, b))
        self.add(self.mul(a, a), self.mul(b, b))


A = Cls2()
A.task(1, 2)
