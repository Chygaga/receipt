print ("Welcome to Number Guessing Game!")
import random
j = (random.randrange(1,100))
#print (j)
guess =int (input ("enter your guess"))
print (guess)
count = 0
while j != guess:
    count = count + 1
    if guess  < j:
        print ("wrong, guess is too low")
    if guess > j:
        print ("wrong, guess is too high")
    guess =int (input ("enter your guess"))
print ("congrats, you are correct no of tries is", count)
        