
# Welcome the user
print ("<<<<<Welcome to ______!>>>>")

# Initalize future variables
total_score = 0
score_1 = 0
score_2 = 0
score_3 = 0
score_4 = 0

# Initalize while loop (boolean) variables
level_11 = False
level_12 = False

# Asking user for their name so the game can adress the user by their name
name = input(("To start, what is your name soilder? "))

# First bit of user input telling them to advance; instructions for the user; storyline
start_game = input("You are now on the loading screen. Type start to continue to the instructions. ")
if start_game == "start":  
    print ("Colnel: The president has been held hostage by an unidentified group. It is your job to rescue him. We will be dropping you off on the back side of their base. Sources have confirmed there are at least 5 guards in your path, including the guard with the president. In order to save the president, answer at least 8/11 questions correctly. ")
    print ("Colnel: Good luck " + name)
    # Ask the user if they are ready to enter the first level, so that I can cut off some of the extra text below
    first_level_ready = input("Are you ready to enter the base(Yes/No)? ")
    while first_level_ready != "Yes":
        print("Its O.K " + name + " take a breather.")
        first_level_ready =  input("Type Yes when you are ready: ")  
    # Introduction to the first level
    print ("<<<<LEVEL 1>>>>")
    print ("You have entered the unidentified groups territory. To get past the first guard, correctly answer 2/2 questions. You have unlimited tries for the first level. ")
    # Using while loops to ask questions as they have unlimited tries for the first level
    while level_11 == False:
        first_question = input("1. How much informaiton is stored in a byte? ")
        if first_question == "8 bits":
            print ("Excellent! You got the first question right. ")
            score_1 = score_1 + 1
            total_score = total_score + 1
            level_11 = True
        else:
            print ("You guessed it wrong")
    print("\nA. Process\nB. Input\nC. Storage\nD. Output")
    while level_12 == False:
        second_question = input("2. List the information processing Cycle in order (Use commas to separate, ex. C, D, A, B) ")
        if second_question == "B, A, D, C":
            print("Excellent! You got the second question right. ")
            score_1 = score_1 + 1
            total_score = total_score + 1
            level_12 = True
        else:
            print("You guessed it wrong")
    # Printing user score (Should be 2/2 as they have unlimited tries)
    print ("Your score is " + str(score_1) + "/2. " + "Your total score is" + str(total_score) + "/2. You may advance to the next level.")
    # Introduction to level 2
    print ("<<<<LEVEL 2>>>>")
    print("Congratulations you have cleared the first level.")
    print("Now entering second level. Gear up " + name + ". You have 1 try to answer the first question, and three for the second question. Good luck.")
    # Questions for level 2 using if statments and for loops
    third_question = input("(True/False) The CPU is essentially the brain of the computer. ")
    if third_question == "True":
        print ("Excellent! You got the first question right.")
        score_2 = score_2 + 1
        total_score = total_score + 1
    else:
        print ("You got the question wrong. Next question.")
    for i in range (3):
        print ("\nA. Provides internet to your household\nB. Protects your network from malicious users and malware\nC. Wirelessly  transmits data\nD. Protects you from fire")
        fourth_question = input("What is the function of a firewall? (Write in caps ex. C) ")
        if fourth_question == "B":
            print ("Excellent! You got the second question right.")
            score_2 = score_2 + 1
            total_score = total_score + 1
            break
        else:
            print("Wrong answer. Please try again")
    print ("Your score is " + str(score_2) + "/2 and your total score is " + str(total_score) + "/4.")
    # Introduction to level 3
    print("<<<<LEVEL 3>>>>")
    print("You are now on level three, and getting closer to the president. The group has identifed that you are in the base, and have sent reinforcments. Questions will get harder. ")
    print ("You have 2 tries to answer the first question, and 1 try to answer the second question. Good luck.")
    # Asking questions through for loops and if statments
    for i in range (2):
        fifth_question = input("Mega/Gigabytes per second measures how much data can be _____?")
        if fifth_question == "transferred" or "Transferred":
            print("Excellent, you got the first question correct.")
            score_3 = score_3 + 1
            total_score = total_score + 1
            break
        else:
            print ("You got it wrong.")
    sixth_question = input("Because of the development of computers, has there been a negative environmental impact? (Yes/No)")
    if sixth_question == "Yes" or "yes":
        print ("Excellent, you got the second question correct.")
        score_3 = score_3 + 1
        total_score = total_score + 1
    else:
        print ("You got the question wrong.")
    print ("Your score for this level is " + str(score_3) + "/2 and your total score is " + str(total_score) + "/6.")
    # Checking up on the users progress
    if total_score >= 4:
        print ("You are doing very good so far " + name)
    elif total_score == 3:
        print ("You are doing decent. You need to answer the next 4 questions correctly in order to save the president. ")
    else:
        print ("You are not doing good. Do not worry, keep going. ")
    # Introduction to level 4
    print("<<<<LEVEL 4>>>>")
    print ("Now entering level 4. Take some time to rest and restock. Guards are now heavily armed.")
    print ("You only ahve 1 chance to answer each of the questions.")
    # Asking questions through if statments
    seventh_question = input("Has there been an increasing amount of mental illnesses (especially within teens) due to the prolonged use of technology? (Yes/No)")
    if seventh_question == "Yes" or "yes":
        print ("Great, you got the first question correct.")
        score_4 = score_4 + 1
        total_score = total_score + 1
    else:
        print ("You got it wrong. Yes, there has been an increasing amount of mental illness associated with the use of technology due to social media. ")
    eight_question = input("Are hackers considered to be malware? (Yes/No)")
    if eight_question == "No" or "no":
        print ("Good job, you got it correct.")
        score_4 = score_4 + 1
        total_score = total_score + 1
    else:
        print("You got it wrong.")