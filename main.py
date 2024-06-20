
#imports / main code.
import random
import time
QUESTION_FORMAT = "{}\na.{}\nb.{}\nc.{}\nd.{}\n"

#words lists
easywords_list = ["wookie","lightspeed","lightsaber","force"]
mediumwords_list = ["deathstar","darth vader","x wing","kylo ren"]
hardwords_list = ["mace windu","plo koon","general grievous","tie fighter"]
extremewords_list = ["star fighter","starkiller base","midichlorians","general snoke"]

#welcoming the user
name = input("What is your name? ")
print ("Hello, " + name, "Time to play hangman!")

#diffuculty select.
question = "what diffuculty do you want the game to be"
a = "easy"
b = "medium"
c = "hard"
d = "extreme"
answer = input(QUESTION_FORMAT.format(question, a, b, c, d)).lower()
if answer == a or answer == "a":
    print ("easy mode easy win")
    word = random.choice(easywords_list)
elif answer == b or answer == "b":
    print ("medium challenge for most people")
    word = random.choice(mediumwords_list)
elif answer == c or answer == "c":
    print ("hard mode be ready")
    word = random.choice(hardwords_list)
elif answer == d or answer == "d":
    print ("extreme mode is nearly impossible be ready")
    word = random.choice(extremewords_list)
else:
    print ("medium mode auto selected")
    word = random.choice(mediumwords_list)
#select words. 
#guess letters
guess=""
while len(guess) !=1:
    guess= input("Guess a letter")


for i in range(len(word)):
    if word[i]==guess.lower():
