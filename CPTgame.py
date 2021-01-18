
# Welcome the user
print ("<<<<<Welcome to ______!>>>>")

# Initalize future variables
total_score = 0
score_1 = 0
score_2 = 0
score_3 = 0
score_4 = 0
score_5 = 0

# Initalize while loop (boolean) variables
level_11 = False
level_12 = False

# Asking user for their name so the game can adress the user by their name
name = input(("\nTo start, what is your name soilder? "))
print ("When answering questions, type the answer with each of the words starting with a captital letter. Example: True, or Yes, or Security Software")

# First bit of user input telling them to advance; instructions for the user; storyline
start_game = input("\nYou are now on the loading screen. Type start to continue to the instructions. ")
if start_game == "Start":  
    print ("\nColonel: The president has been held hostage by an unidentified group. It is your job to rescue him. We will be dropping you off on the back side of their base. Sources have confirmed there are at least 5 guards in your path, including the guard with the president. In order to save the president, answer at least 8/11 questions correctly. ")
    print ("\nColonel: Good luck " + name)

    # Ask the user if they are ready to enter the first level, so that I can cut off some of the extra text below
    first_level_ready = input("Are you ready to enter the base(Yes/No)? ")
    while first_level_ready != "Yes":
        print("Its O.K " + name + " take a breather.")
        first_level_ready =  input("Type Yes when you are ready: ")  

    # Introduction to the first level
    print ("\n<<<<LEVEL 1>>>>")
    print ("You have entered the unidentified groups territory. To get past the first guard, correctly answer 2/2 questions. You have unlimited tries for the first level. ")
    
    # Using while loops to ask questions as they have unlimited tries for the first level
    while level_11 == False:
        first_question = input("\n1. How much informaiton is stored in a byte? ")
        if first_question == "8 Bits":
            print ("Excellent! You got the first question right. ")
            score_1 = score_1 + 1
            total_score = total_score + 1
            level_11 = True
        elif first_question == "8 bits":
            print ("Remember, you must answer with each of your words in capital (8 Bits). Try again.")
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
    
    # Printing user score and asking if they are ready to advance (Should be 2/2 as they have unlimited tries)
    print ("\nYour score is " + str(score_1) + "/2. " + "Your total score is" + str(total_score) + "/2. You may advance to the next level.")
    second_level_ready = input ("Are you ready to move onto the next level? (Yes/No)")
    while second_level_ready != "Yes":
        print("Its O.K " + name + " take a breather.")
        second_level_ready =  input("Type Yes when you are ready: ")  
    
    # Introduction to level 2
    print ("\n<<<<LEVEL 2>>>>")
    print("Congratulations you have cleared the first level.")
    print("Now entering second level. Gear up " + name + ". You have 1 try to answer the first question, and three for the second question. Good luck.")
   
    # Questions for level 2 using if statments and for loops
    third_question = input("\n1. (True/False) The CPU is essentially the brain of the computer. ")
    if third_question == "True":
        print ("Excellent! You got the first question right.")
        score_2 = score_2 + 1
        total_score = total_score + 1
    else:
        print ("You got the question wrong. Next question.")
    for i in range (3):
        print ("\nA. Provides internet to your household\nB. Protects your network from malicious users and malware\nC. Wirelessly  transmits data\nD. Protects you from fire")
        fourth_question = input("2. What is the function of a firewall? (Write in caps ex. C) ")
        if fourth_question == "B":
            print ("Excellent! You got the second question right.")
            score_2 = score_2 + 1
            total_score = total_score + 1
            break
        else:
            print("Wrong answer. Please try again")
    # Printing user score and asking if they are ready
    print ("\nYour score is " + str(score_2) + "/2 and your total score is " + str(total_score) + "/4.")
    third_level_ready = input ("Are you ready to move onto the next level? (Yes/No)")
    while third_level_ready != "Yes":
        third_level_ready =  input("Type Yes when you are ready: ")  
    
    # Introduction to level 3
    print("\n<<<<LEVEL 3>>>>")
    print("You are now on level three, and getting closer to the president. The group has identifed that you are in the base, and have sent reinforcments. Questions will get harder. ")
    print ("\nYou have 2 tries to answer the first question, and 1 try to answer the second question. Good luck.")
    
    # Asking questions through for loops and if statments
    for i in range (2):
        fifth_question = input("\nMega/Gigabytes per second measures how much data can be _____? ")
        if fifth_question == "transferred" or "Transferred":
            print("Excellent, you got the first question correct.")
            score_3 = score_3 + 1
            total_score = total_score + 1
            break
        else:
            print ("You got it wrong.")
    sixth_question = input("\nBecause of the development of computers, has there been a negative environmental impact? (Yes/No) ")
    if sixth_question == "Yes":
        print ("Excellent, you got the second question correct.")
        score_3 = score_3 + 1
        total_score = total_score + 1
    else:
        print ("You got the question wrong.")
    # Printing user score and asking if they want to move on
    print ("\nYour score for this level is " + str(score_3) + "/2 and your total score is " + str(total_score) + "/6.")
    fourth_level_ready = input ("Are you ready to move onto the next level? (Yes/No)")
    while fourth_level_ready != "Yes":
        print("Take a breather.")
        fourth_level_ready =  input("Type Yes when you are ready: ")  
    
    # Checking up on the users progress
    if total_score >= 4:
        print ("\nYou are doing very good so far " + name)
    elif total_score == 3:
        print ("\nYou are doing decent. You need to answer the next 4 questions correctly in order to save the president. ")
    else:
        print ("\nYou are not doing good. Do not worry, keep going. ")
    
    # Introduction to level 4
    print("\n<<<<LEVEL 4>>>>")
    print ("Now entering level 4. Take some time to rest and restock. Guards are now heavily armed.")
    print ("You only have 1 chance to answer each of the questions.")
    questions_four_ready = input ("\nAre you ready to move onto the next level? (Yes/No)")
    while questions_four_ready != "Yes":
        questions_four_ready =  input("Type Yes when you are ready: ")  
    
    # Asking questions through if statments
    seventh_question = input("\nHas there been an increasing amount of mental illnesses (especially within teens) due to the prolonged use of technology? (Yes/No)")
    if seventh_question == "Yes":
        print ("Great, you got the first question correct.")
        score_4 = score_4 + 1
        total_score = total_score + 1
    else:
        print ("You got it wrong. Yes, there has been an increasing amount of mental illness associated with the use of technology due to social media. ")
    eight_question = input("\nAre hackers considered to be malware? (Yes/No) ")
    if eight_question == "No":
        print ("Good job, you got it correct.")
        score_4 = score_4 + 1
        total_score = total_score + 1
    else:
        print("You got it wrong.")
    
    # Printing user score
    print ("\nYour score for this level is " + str(score_4) + "/2 and your total score is " + str(total_score) + "/8.")
    fifth_level_ready = input ("Are you ready to move onto the next level? (Yes/No)")
    while fifth_level_ready != "Yes":
        fifth_level_ready =  input("Type Yes when you are ready: ")  
    
    # Introduction to Level 5
    print ("\n<<<<LEVEL 5>>>>")
    print ("President: Oh thank god you're here " + name + ". I've been trapped here for so long. Quick, untie me and let's get out before Brutus catches us!")
    print("*Unties President*")
    print ("\nBrutus: Not so fast soilder. I never said you could take the president. ")
    print ("FINAL FACEOFF AGAINST BRUTUS! You have three questions, with 3 tries for the first question, 1 try for the second question and 3 tries for the last question")
    
    # Asking if they are ready in order to cut off some text (Makes it easier for them to read)
    questions_fifth_ready = input ("\nAre you ready to move onto the next level? (Yes/No)")
    while questions_fifth_ready != "Yes":
        questions_fifth_ready =  input("Type Yes when you are ready to start: ")  
    
    # Asking final questions
    ninth_question = input("\nWhat type of malware records everything you type on your computer?")
    for i in range (3):
        if ninth_question == "Keyloggers":
            print ("Great, you got the first question right")
            score_5 = score_5 + 1
            total_score = total_score + 1
            break
        else:
            print ("You got it wrong. Do not worry. ")
    tenth_question = input("\n(True/False) You can apply to medical school with a computer science degree ")
    if tenth_question == "True":
        print("Excellent, you got it right.")
        score_5 = score_5 + 1
        total_score = total_score + 1
    else:
        print ("You got it wrong. ")
    eleventh_question = input ("\nList 1 type of malware (Apart from keyloggers): ")
    for i in range (3):
        if eleventh_question == "Adware" or "Spyware" or "Virus" or "Worm" or "Trojan" or "Rootkit" or "Backdoors" or "Rouge Security Software" or  "Ransomware" or "Browser Hijacker":
            print ("Excellent, you got it correct!")
            score_5 = score_5 + 1
            total_score = total_score + 1
            break
        else:
            print ("You got it wrong")
    
    # Seeing if the user won or not
    print ("\nComputer: Alright soilder. Let's see if you saved the president or not.")
    print ("Your final score was" + str(total_score) + "/11.")

    final_statement_ready = input ("\nAre you ready to move on? (Yes/No)")
    while second_level_ready != "Yes":
        second_level_ready =  input("Type Yes when you are ready to hear the results: ") 

    if total_score >= 8:
        print ("\n<<<<CONGRATULATIONS, YOU SAVED THE PRESIDENT>>>>")
        print ("You made it out of the base unharmed with the president. Once you made it back home, you were treated for your injuries, then was awarded the Medal of Honor from the president himself.")
        print ("You are now appointed as the president's personal bodyguard. ")
    else:
        print ("\nSorry, " + name + " you did not save the president. Although you made it out fine, the president is still stuck at the base. The S.W.A.T team has taken over the rescue.")
    
    # Closing statment
    print ("\n<<<<THANK YOU FOR PLAYING>>>>")
