import random,array
passL=int(input("Enter number of letters that you want:"))
passN=int(input("enter how many numbers you'd like:"))
passS=int(input("enter number of special symbols that you'd like:"))
letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '1234567890'
symbols = '''"!@#$%^&*()_~`{[}]|\'.<?,>'''
password = ''
for i in range(passL):
    password+=random.choice(letters)
for i in range(passN):
    password+=random.choice(numbers)
for i in range(passS):
    password+=random.choice(symbols) 
Gen = ''.join(random.sample(password,len(password)))  
print("The generated password made for you is: %s ",Gen)

