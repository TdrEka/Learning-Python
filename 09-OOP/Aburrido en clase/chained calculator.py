# Claude told me to do this

class Calculator:
    def __init__(self, number = 0):
        self.number = number

    def sum(self, number):
        self.number += number
        return self

    def sub(self, number):
        self.number -= number
        return self

    def mult(self, number):
        self.number *= number
        return self

    def div(self, number):
        self.number /= number
        return self

    def result(self):
        return self.number

