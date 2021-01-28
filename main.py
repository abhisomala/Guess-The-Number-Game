
import random

number = random.randrange(1,100)
print(number)
guess = int(input("Guess a number between 1 and 100: "))

while guess != number:
  
  if guess < number:
    if (number - guess) < 2:
      print("\nI am very very sad. Do you understand how close you are.You just need to go slightly higher.")  
    elif (number - guess) < 5:
        print("\nWow, you are very close. A little higher.")
    elif (number - guess) < 10:
      print("\nYour guess isn't too terribly off. You need to go higher still ")
    elif (number - guess) < 20:
      print("\nYou are still very off. You have to go a lot higher. ")
    elif (number - guess) < 40:
       
       print("\nWhat are you even doing?? You need to go higher. ")
    else:
      print("\nPlease, never play a guessing game ever. You are soooooo off. You need to go sooooo much higher")
  elif guess > number:
    print("\nYou need to guess lower.")
  else:
    print("\nMy dude where are you? ")
  guess = int(input("\nGuess a number between 1 and 100: "))
print("\nYou guessed the number correctly! You Win!")
  
