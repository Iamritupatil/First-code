password = input("Enter your password: ")

if len(password) < 8:
    print("Password must be at least 8 characters long.")

    password = input("Enter your password again: ")

elif len(password) >= 8:
    print("Password length is just right.")


 
elif len(password) > 12: 
   print("Password is too long.")
    
password = input("Enter your password again : ")