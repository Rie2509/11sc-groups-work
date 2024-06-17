
#imports / main code.
import random
import time
Score =+ 10
QUESTION_FORMAT = "{}\na.{}\nb.{}\nc.{}\nd.{}"
Play = "yes"
#words lists
easywords_list = ["wookie","lightspeed","lightsaber","force"]

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
if answer == b or answer == "b":
    print ("medium challenge for most people")
if answer == c or answer == "c":
    print ("hard mode be ready")
if answer == d or answer == "d":
    print ("extreme mode is nearly impossible be ready")

#select words. 
word = random.choice(easywords_list)
 
 # check number of question attempts
while True:
    try:
        tries = input("how many lives do you want")
        tries = int(tries)
        break
    except:
        print("thats not a number")
# start the quiz
while Play == "yes":

    question_attempts = tries
    while question_attempts > 0:
        #ask the use a question

        answer = input("are you a sigma")
        if answer == "yes":
            print("sigma")
            break
        elif answer == "":
            print("Write something")
        else:
            print("no you dumb")    
        
        question_attempts -= 1
        print("Try again")

