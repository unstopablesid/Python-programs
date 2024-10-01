class employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    @classmethod
    def fromstr(cls, string):
        return cls(string.split("-")[0].strip(), string.split("-")[1].strip())

a = employee("Mayur", 150000)
print(a.name)
print(a.salary)

string = "drone-10000"
a2 = employee.fromstr(string)
print(a2.name)
print(a2.salary)

string = "manish-5000"
a3 = employee.fromstr(string)
print(a3.name)
print(a3.salary)

string = "Bhavesh-5000"
a4 = employee.fromstr(string)
print(a4.name)
print(a4.salary)

string = "Neeraj-25000"
a5 = employee.fromstr(string)
print(a5.name)
print(a5.salary)
