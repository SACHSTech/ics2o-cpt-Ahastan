
# Welcome the user
print ("<<<<<Welcome to ______!>>>>")

# Initalize future variables
score_1 = 0
"""
# Asking user for their name so the game can adress the user by their name
name = input(("To start, what is your name soilder? "))

# First bit of user input telling them to advance; instructions for the user; storyline
start_game = input("You are now on the loading screen. Type start to continue to the instructions. ")
if start_game == "start":  
    print ("Colnel: The president has been held hostage by an unidentified group. It is your job to rescue him. We will be dropping you off on the back side of their base. Sources have confirmed there are at least 5 guards in your path, including the guard with the president. ")
    print ("Colnel: Good luck " + name)

# Ask the user if they are ready to enter the first level, so that I can cut off some of the extra text below
first_level_ready = input("Are you ready to enter the base(Yes/No)? ")
if first_level_ready == "Yes":
    print ("<<<<LEVEL 1>>>>")
    print ("You have entered the unidentified groups territory. To get past the first guard, correctly answer 2/2 questions. You have unlimited tries for the first level. ")
"""
# Initalize while loop (boolean) variables
level_11 = False
level_12 = False

# Ask questions through while looops since they get unlimited tries.
while level_11 == False:
    first_question = input("1. How much informaiton is stored in a byte? ")
    if first_question == "8 bits":
        print ("Excellent! You got the first question right. ")
        score_1 = score_1 + 1
        level_11 = True
    else:
        print ("You guessed it wrong")

print("\nA. Process\nB. Input\nC. Storage\nD. Output")

while level_12 == False:
    second_question = input("List the information processing Cycle in order (Use commas to separate, ex. C, D, A, B) ")
    if second_question == "B, A, D, C":
        print("Excellent! You got the second question right. ")
        score_1 = score_1 + 1
        level_12 = True
    else:
        print("You guessed it wrong")

print ("Your score is " + str(score_1) + "/2. You may advance to the next level.")