try:
    result=10/0
    value = int(input("enter your age : "))
    print(value)
except ZeroDivisionError as err1:
    print(err1)
except ValueError as err2:
    print(err2)