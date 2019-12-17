import random
while(1):
    Guess = random.choice(['R','P','S'])
    user_guess = str(input("Enter the First Initial Of Rock, Paper or Scissor:"))
    if Guess=='R' and user_guess=='P':
        print("User Won")


    elif Guess=='P' and user_guess=='R':
        print("Computer won")

    elif Guess=='R' and user_guess=='S':
        print("Computer won")
        

    elif Guess=='S' and user_guess=='R':
        print("User Won")


    elif Guess=='P' and user_guess=='S':
        print("Computer won")

    elif Guess=='S' and user_guess=='P':
        print("User Won")
    else:
        print("It's a tie!")