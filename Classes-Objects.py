class Employee:
    def __init__(self , FirstName, lastName , cin , age , salary , rating):
        self.FirstName = FirstName
        self.lastName = lastName
        self.cin = cin
        self.age = age
        self.salary = salary
        self.rating = rating
    
    def myfunc(self):
        print("Hello my name is " + self.FirstName)

    def is_excellent(self):
        if self.rating > 5:
            print("good")
        else: 
            print("bad")

    def Bonnus(self):
        if self.age >= 50:
            self.salary += 100
            print("salary increased to " + str(self.salary))
        else:
            print("no bonus added , salary is still " + str(self.salary))
# Objet
Emp1 = Employee("mohamed" , "el-meghari" , "AB1343" , 21 , 3000 , 6)
Emp2 = Employee("rida" , "taoussi" , "AB2243" , 50 , 6000 , 3)

Emp1.is_excellent() # -> good
Emp2.is_excellent() # -> bad

Emp1.myfunc() # Hello my name is mohamed

Emp2.Bonnus()
