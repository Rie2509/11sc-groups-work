
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
tries = ''
#welcoming the user
name = input("What is your name? ")
print ("Hello, " + name, "Time to play hangman!")

#tries code
while play == "yes": 
 # check number of question attempts
 while True:
    while True:
        tries = input("how many lives do you want\n")
            
        if tries.isalpha():
            print("thats not a number")
            
        else:
           break
            
    
 


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

    print(word)
 
    # start the quiz


    question_attempts = int(tries)
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





# #select words.
# while not letter:
#     input("Make sure your guess is a letter")
# blanks=""
# for letter in word: 
#     if letter == (" "):
#         blanks += (" ") 
#     else : blanks += ("_")
# print(blanks)
# #guess letters
# guess=""
# while len(guess) !=1:
#     guess= input("Guess a letter")


# for i in range(len(word)):
#     if word[i]==guess.lower():
#         pass




            # .   while (attempts != 0 and "-" in word_guessed):
            #         print(("\nYou have {} attempts remaining").format(attempts))
            #         joined_word = "".join(word_guessed)
            #         print(joined_word)

            #         try:
            #             player_guess = str(input("\nPlease select a letter between A-Z" + "\n> ")).lower()
            #         except: # check valid input
            #             print("That is not valid input. Please try again.")
            #             continue                
            #         else: 
            #             if not player_guess.isalpha(): # check the input is a letter. Also checks an input has been made.
            #                 print("That is not a letter. Please try again.")
            #                 continue
            #             elif len(player_guess) > 1: # check the input is only one letter
            #                 print("That is more than one letter. Please try again.")
            #                 continue
            #             elif player_guess in guessed_letters: # check it letter hasn't been guessed already
            #                 print("You have already guessed that letter. Please try again.")
            #                 continue
            #             else:
            #                 pass


# #ending / restart (Taiwhakaea)
# play = input ("do you want to play again?")   
