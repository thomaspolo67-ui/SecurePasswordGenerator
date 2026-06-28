from password_generator import generate_password 
while True:
    length = int(input("Enter the desired password length: "))
    uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
    numbers = input("Include numbers? (y/n): ").lower() == 'y'
    symbols = input("Include symbols? (y/n): ").lower() == 'y'


    if length < 8: 
        print("password should be at least 8 characters long.") 
    else: 
      password = generate_password(length, uppercase, lowercase, numbers, symbols) 
    if password is None: 
         print("please select at least two character types.")  
    else:
        break
print("\nGenerated password: ") 
print(password) 

