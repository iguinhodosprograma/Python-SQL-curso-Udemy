number = 7
userInput = input("Enter 'y' if you like to play: ").lower()

if userInput == "y":
    userNumber = int(input("Guess our number: "))
    
    if userNumber == number:
        print("You guessed correctly!")
    elif abs(number - userNumber) == 1:
        print("You were off by one.")
    else:
        print("Sorry, it's wrong!")
    