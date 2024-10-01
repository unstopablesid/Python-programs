class employee:
    def __init__(self,name):
        self.name= name
    def Showdetails(self):
        print(f"The name of an employee:{self.name}")

emp1=employee("harry")
emp1.Showdetails()
# employee.Showdetails(emp1)
emp2=employee("mayur")
emp2.Showdetails()