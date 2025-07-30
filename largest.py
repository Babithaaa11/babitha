num1 = input("enter the num1")
num2 = input("enter the num2")
num3 = input("enter the num3")
if num1.isnumeric() == False:
    print("num1 is not a number")
elif num2.isnumeric() == False:
    print("num2 is not a number")
elif num3.isnumeric() == False:
    print("num3 is not a number")
else:
    res1=int(num1)
    res2=int(num2)
    res3=int(num3)
    print(str(res1))
    print(str(res2))
    print(str(res3))
try:
    if num1 >= num2 and num1 >= num3:
        print("num1 is largest")
    elif num2 >= num1 and num2 >= num3:
        print("num2 is largest")
    else:
        print("num3 is largest")
except Exception as e:
    print(e)