#importing the time module
import random
import time
Words_list = ["wookie","lightspeed","lightsaber","force"]
#welcoming the user
name = input("What is your name? ")

print ("Hello, " + name, "Time to play hangman!")

#here we set the secret. You can select any word to play with. 
word = random.choice(Words_list)
