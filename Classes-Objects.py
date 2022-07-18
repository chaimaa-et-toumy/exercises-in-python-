class Employee:
    def __init__(self , FirstName, lastName , cin , age , salary):
        self.FirstName = FirstName
        self.lastName = lastName
        self.cin = cin
        self.age = age
        self.salary = salary
    
    def myfunc(self):
        print("Hello my name is " + self.FirstName)

# Objet
Emp1 = Employee("mohamed" , "el-meghari" , "AB1343" , 21 , "3000")
Emp2 = Employee("rida" , "taoussi" , "AB2243" , 25 , "6000")

Emp1.myfunc() # Hello my name is mohamed

print(Emp1.FirstName , Emp1.lastName)