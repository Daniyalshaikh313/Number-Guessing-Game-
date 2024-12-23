import random
guessnumber = random.randint(1,100)
while True:
    try:
        guess = int(input("Enter guess number 1 to 100: "))
        if guess > guessnumber:
            print('To High')
        elif guess < guessnumber:
            print("To Low")
        else:
            print("You Win the Game !!")
    except ValueError:
        print("Invalid Input")                