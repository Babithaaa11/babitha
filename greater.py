num = input("enter the number")
num_int = int(num)
print(type(num_int))
try:
    if int(num) > 100:
        print("it is error")
    else:
        print("it is not error")
except Exception as e:
    print(e)