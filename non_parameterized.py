class Employee:
    def __init__(self):
        self.id = 123
        self.name = 'arun'

    def display(self):
        print(self.id,self.name)


emp1 = Employee()
emp1.display()
print(emp1.name)
