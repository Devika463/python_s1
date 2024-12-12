class Employee:
    company_name="ABCD"
    location="Calicut"
    def __init__(self,id,name,salary):
        self.emp_id=id
        self.emp_name=name
        self.emp_salary=salary
    def details(self):
        print(self.emp_id,self.emp_name,self.emp_salary)
emp1=Employee(101,"Harsha",50000)
emp2=Employee(102,"Adwik",25000)
emp1.details()
emp2.details()
