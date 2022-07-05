n1 = float(input("enter the A number : "))
op = input("please enter the operator (+,-,*,/,%) : ")
n2 = float(input("enter the B number : "))

result1 = n1+n2
result2 = n1-n2
result3 = n1*n2
result4 = n1/n2
result5 = n1%n2

if op == "+":
    print(result1)
elif op == "-":
    print(result2)
elif op == "*":
    print(result3)
elif op == "/":
    print (result4)
elif op == "%":
    print(result5)
else:
    print("wrong operator please try again")