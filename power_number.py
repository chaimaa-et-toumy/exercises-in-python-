# *************The method 1 : simple  *************
x= int(input("enter la premier number : "))
y= int(input("enter la deuxieme number : "))
z = pow(x,y)
print("the number power is : " + str(z))


# *************The method 2 : function *************
def calcule_p(x,y):
        z = pow(int(x),int(y))
        return z
print(calcule_p(2,6))

# *************The method 3 : for loop *************
from unittest import result

def calcule_p(x,y):
        result = 1
        for z in range(y):
                result *= x
        return result
print(calcule_p(3,3))