import random

secretnumber = random.randint(1,20)
print('Guess the number, Range is 1 to 20')
guessTaken = 1

while guessTaken < 7:
    guess = int(input("Your Guess? "))
    if guess > secretnumber:
        print('Your Guess is High.')
    elif guess < secretnumber:
        print('Your Guess is Low.')
    else:
        break
    guessTaken += 1

if guessTaken < 7:
    print('Good Job!! You guess the number in',guessTaken,'guesses!')
else:
    print('Nope!! The number is',secretnumber)
