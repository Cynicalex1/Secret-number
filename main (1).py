#Problem 3.1.1 - Copy and paste the link to canvas once you are complete.
import random

secret_number =  random.randint(1,10)
guess = int(input("Guess a number from 1 - 10:  "))
while guess != secret_number:
   if guess < secret_number  :
    guess= int(input("You number is too low, please try again:   "))
   elif guess > secret_number:
    guess = int(input("You number is too high, please try again:  "))
  
print("You are correct!","The secret number was", secret_number)
            