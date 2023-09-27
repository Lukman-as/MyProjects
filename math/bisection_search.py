print("Please think of a number between 0 and 100!")
max = 100
min = 0

while True:
    guess = int((max + min)/2)
    print("Is your secret number ", guess, "?")
    answer = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if answer == 'h':
        max = guess
    elif answer == 'l':
        min = guess
    elif answer == 'c':
        print("Game over. Your secret number was: 42")
        break
    else:
        print("Invalid input")





