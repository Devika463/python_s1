class Employee:
    Basic=0
    TA=0
    DA=0
    def salary(self):
        print("Salary",self.Basic+self.TA+self.DA)
emp1=Employee()
emp1.Basic=20000
emp1.TA=500
emp1.DA=1000
emp1.salary()
