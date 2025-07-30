num1 = input("enter the num1")
num2 = input("enter the num2")
if num1.isnumeric() == False:
    print("num1 is not number")
elif num2.isnumeric() == False:
    print("num2 is not number")
else:
    res = int(num1)+int(num2)
    print(str(res))