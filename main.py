
import random

number = random.randrange(1,100)

guess = int(input("Guess a number between 1 and 100: "))

while guess != number:

  if guess < number:
    if (number - guess) <  2:

      print("\nDo you understand how close you are. You are very close. You just need to go slightly higher.")  
    elif (number - guess) < 5:

        print("\nWow, you are very close. A little higher.")
    elif (number - guess) < 10:

      print("\nYour guess isn't too terribly off. You need to go higher still ")
    elif (number - guess) < 20:
      
      print("\nYou are still very off. You have to go a lot higher. ")
    elif (number - guess) < 40:
       
       print("\nAlthough you are very very far keep trying. You need to go much much higher. ")
    else:

      print("\nI'm sorry but you luck is not very good. You need to go sooooo much higher")
  
  if guess > number:

    if (number - guess) < 2:

      print("\nDo you understand how close you are. You are very close. You just need to go slightly lower.")
    elif (number - guess) < 5:

      print("\nWow, you are very close. A little lower.")
    elif (number - guess) < 10:

      print("\nYour guess isn't too terribly off. You need to go lower still")
    elif (number - guess) < 20:

       print("\nYou are still very off. You have to go a lot lower. ")
    elif (number - guess) < 40:

      print("\nAlthough you are very very far keep trying. You need to go much much lower.")
    else:
      
       print("\nI'm sorry but you luck is not very good. You need to go sooooo much lower.")
  
  guess = int(input("\nGuess a number between 1 and 100: "))
print("\nYou guessed the number correctly! You Win!")
  
