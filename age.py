age = input("enter the age")
#data type of the variable
print(type(age))
#string to int
age_int = int(age)
print(type(age_int))
if age_int < 10:
    print("This is child")
else:
    print("Not child")