
#imports / main code.
import random
import time
QUESTION_FORMAT = "{}\na.{}\nb.{}\nc.{}\nd.{}\n"

#words lists
easywords_list = ["wookie","lightspeed","lightsaber","force"]
mediumwords_list = ["deathstar","darth vader","x wing","tie fighter"]
hardwords_list = ["place holder","place holder","place holder","place holder"]
extremewords_list = ["place holder","place holder","place holder","place holder"]

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

