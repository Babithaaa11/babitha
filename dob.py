#def calculateAge(dob):
     

#dob = input("enter dob dd-mm-yyyy")
#calculateAge(dob)

from datetime import datetime

def calculate_age(birthdate_str):
    birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d").date()

    today = datetime.today().date()
    
    age = today.year - birthdate.year

    if (today.month, today.day) < (birthdate.month, birthdate.day):
        age -= 1

    print("Your age is:", age)
calculate_age("2004-03-10")