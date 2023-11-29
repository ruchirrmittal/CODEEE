class Employee:

    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    @classmethod
    def FromStr(cls,string):
        return cls(string.split("-")[0],string.split("-")[1])


e1=Employee("Ruchir","10000")
print(e1.name)
print(e1.salary)
e2=Employee.FromStr("Ruchirr-12000")
print(e2.name)
print(e2.salary)