n1 = input("enter the A number : ")
n2 = input("enter the B number : ")

op = input("enter calcule (+,-,*,/,%) : ")

result1 = float(n1)+float(n2)
result2 = float(n1)-float(n2)
result3 = float(n1)*float(n2)
result4 = float(n1)/float(n2)
result5 = float(n1)%float(n2)


if op == "+":
    print(result1)
if op == "-":
    print(result2)
if op == "*":
    print(result3)
if op == "/":
    print (result4)
if op == "%":
    print(result5)
else:
    print("Sorry it's not a operate")