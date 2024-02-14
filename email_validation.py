import re
email_validation="^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
user_email=input("Enter Your Email id :")

if re.search(email_validation,user_email):
   print("Right Email") 
else:
    print("Wrong Email")    