
#imports / main code.
import random
import time
Score =+ 10
QUESTION_FORMAT = "{}\na.{}\nb.{}\nc.{}\nd.{}"
play = "yes"
#words lists
easywords_list = ["wookie","lightspeed","lightsaber","force"]
mediumwords_list = ["deathstar","darth vader","x wing","kylo ren"]
hardwords_list = ["mace windu","plo koon","general grievous","tie fighter"]
extremewords_list = ["star fighter","starkiller base","midichlorians","general snoke"]

#welcoming the user
name = input("What is your name? ")
print ("Hello, " + name, "Time to play hangman!")

#tries code
while play == "yes": 
 # check number of question attempts
 while True:
    try:
        tries = input("how many lives do you want\n")
        tries = int(tries)
        break
    except:
        print("thats not a number")
# start the quiz


    question_attempts = tries
    while question_attempts > 0:
        #ask the use a question

        answer = input("")
        if answer == "yes":
            print("sigma")
            break
        elif answer == "":
            print("Write something")
        else:
            print("no you dumb")    
        
        question_attempts -= 1
        print("Try again") 


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
<<<<<<< HEAD
#select words. 
word = random.choice(easywords_list)
 
#End the quiz
    #Replay
play = input ("do you want to try again").lower()
=======
#select words.
while not letter .isalpha
    input("Make sure your guess is a letter")
blanks=""
for letter in word: 
    if letter == (" "):
        blanks += (" ") 
    else : blanks += ("_")
print(blanks)
#guess letters
guess=""
while len(guess) !=1:
    guess= input("Guess a letter")


for i in range(len(word)):
    if word[i]==guess.lower():
        pass

#ending / restart (Taiwhakaea)
>>>>>>> 7107d71574827eb90fcbd34d58b8f6d35dc3b49d
