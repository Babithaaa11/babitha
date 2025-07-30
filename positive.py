num = input("enter the number")
print("it is a number")
try:
    if num > 0:
        print("it is a positive number")
    elif num < 0:
        print("it is a negative number")
    else:
        print("it is zero")
except Exception as e:
    print(e)
