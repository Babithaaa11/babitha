num1 = input("enter the num1")
num2 = input("enter the num2")
action = input("enter the action")
add = int(num1 + num2)
add_int = int(add)
try:
   if action is add:
     print(str(add))
   else:
      print("action is false")
except Exception as e:
    print(e)