import random
print("The game is about to start. If you want to leave, type 'exit' at any time.")

def generate_Number():
    global randNumber
    randNumber = random.randint(1, 9)
    print("Number has been generated")
    print("number is", randNumber)
    return randNumber

def random_Number():
    numberOfGuesses = 0
    while True:
        numberOfGuesses += 1
        try:
            userGuess = input("Guess the number! ")
            if userGuess == "exit":
                quit()
            userGuess = int(userGuess)
        except ValueError:
            print("Error. You have to type in a number")
            continue
        
        if userGuess < randNumber:
            print("Your number is lower than original number. Keep trying!")
        elif userGuess > randNumber:
            print("Your number is higher than generated number. Keep trying!")
        else:
            print("Congratulations, you've guessed the number correctly! \nYour number of tries:", numberOfGuesses)
            break

def play_Again():
    try_Again = input("Do you want to play again? [Yes \ No] \n")
    if try_Again.lower() == "yes":
        main()
    elif try_Again.lower() == "no":
        quit()
    else:
        print("Error! You have to type in {} or {}".format("Yes","No"))
        play_Again()

def main():
    generate_Number()
    random_Number()
    play_Again()

main()
