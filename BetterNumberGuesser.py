import random #imports randomness into the number generator

number = random.randint(1,10) #randomly chooses number from 0-10
attempts = 0 #starting number of attemps

print("Guess a number from 1-10... You have 3 attempts.")

while attempts != 3:  # keep looping until the user has made 3 attempts
    guess = int(input("Make your guess: "))  # ask the user to enter their guess and convert it to an integer

    if guess > number:  # if the guess is too high
        print("--------------------")
        print("Wrong, the number is lower than this, try again!")
        attempts = attempts + 1  # increment the number of attempts
    elif guess < number:  # if the guess is too low
        print("--------------------")
        print("Wrong, the number is higher than this, try again!")
        attempts = attempts + 1  # increment the number of attempts
    else:  # if the guess is correct
        print("Booyah! You guessed correctly.")
        exit()  # end the program

print(f"The number is {number}")  # if the user has made 3 attempts without guessing correctly, print the correct number