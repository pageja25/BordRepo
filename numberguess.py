import random
import math

lower = int(input("Enter lower bound: "))
upper = int(input("Enter higher bound: "))
maxguess = round(math.log(upper - lower + 1, 2))
num = random.randint(lower, upper)
count = 0
while count < maxguess:
    count += 1

    guess = int(input("Guess a number: "))
    if guess == num:
        print("Good job!")
        break
    elif guess > num:
        print("Your guess is too high!")
    elif guess < num:
        print("Your guess is too low!")
    print ("You only have", maxguess - count, "guesses left")

if(count < maxguess):
    print("You guessed", num, "in", count, "tries.")
else:
    print("The answer was", num, ". You donkey!")
    print("Better luck next time!")