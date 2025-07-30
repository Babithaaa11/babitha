user_input=input("enter text:")
date=input("date")
time=input("time")
with open("sample.txt",'w') as file:
    file.write("some text")
    file.write(f"User_input:{formatted_user_input}\n")
    file.write(f"date:{formatted_date}\n")
    file.write(f"time:{formatted_time}\n")+