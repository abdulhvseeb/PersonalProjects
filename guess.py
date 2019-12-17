import random
def Random():
    guess_input = int((input("Guess a number:")))
    r = random.randrange(1,20)
    if guess_input > r:
        print("you are too high")
    elif guess_input < r:
        print("You are too low")
    else:
        print("you got it right")
Random()
