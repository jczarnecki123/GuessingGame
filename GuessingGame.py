import random
print("The game is about to start. If you want to leave, type 'exit' at any time.")

def randomNumber():
    numberOfGuesses = 0
    randNumber = random.randint(1, 9)
    print("Number has been generated")
    print("number is", randNumber)

    while(True):
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

    tryAgain = input("Do you want to play again? [Yes \ No] \n")
    if tryAgain.lower() == "yes":
        randomNumber()
    else:
        quit()
randomNumber()