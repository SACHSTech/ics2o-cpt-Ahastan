
# Welcome the user
print ("<<<<<WELCOME TO OPERATION: PRESIDENT DOWN!>>>>")

# Initalize future variables
total_score = 0
score_1 = 0
score_2 = 0
score_3 = 0
score_4 = 0
score_5 = 0

# Initalize while loop (boolean) variables
guess_1 = False
guess_2 = False

# Asking user for their name so the game can adress the user by their name
name = input(("\nTo start, what is your name soilder? "))
print ("When answering questions, type the answer with each of the words starting with a captital letter. Example: True, or Yes, or Security Software")

# First bit of user input telling them to advance; instructions for the user; storyline
start_game = input("\nYou are now on the loading screen. Type Start to continue to the instructions. ")
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
    print ("You have entered the unidentified groups territory. There is the first guard! Gear up before you go soldier.")
    print(" To get past the first guard, correctly answer 2/2 questions. The first level is a practice round, so you have unlimited tries for the first level. ")
    
    # Using while loops to ask questions as they have unlimited tries for the first level
    while guess_1 == False:
        first_question = input("\n1. How much informaiton is stored in a byte? ")
        if first_question == "8 Bits":
            print ("Excellent! You got the first question right. ")
            score_1 = score_1 + 1
            total_score = total_score + 1
            guess_1 = True
        elif first_question == "8 bits":
            print ("Remember, you must answer with each of your words in capital (8 Bits). Try again.")
        else:
            print ("You guessed it wrong")

    print("\nAssess the following informaiton:\nA. Process\nB. Input\nC. Storage\nD. Output")
    while guess_2 == False:
        second_question = input("2. List the information processing Cycle in order (Use commas to separate, ex. C, D, A, B): ")
        if second_question == "B, A, D, C":
            print("Excellent! You got the second question right. ")
            score_1 = score_1 + 1
            total_score = total_score + 1
            guess_2 = True
        else:
            print("You guessed it wrong")
    
    # Printing user score and asking if they are ready to advance (Should be 2/2 as they have unlimited tries)
    print ("\nYour score is " + str(score_1) + "/2. " + "Your total score is " + str(total_score) + "/2. You may advance to the next level.")
    second_level_ready = input ("Are you ready to move onto the next level? (Yes/No) ")
    while second_level_ready != "Yes":
        print("Its O.K " + name + " take a breather.")
        second_level_ready =  input("Type Yes when you are ready: ")  
    
    # Introduction to level 2
    print ("\n<<<<LEVEL 2>>>>")
    print("Congratulations you have cleared the first level.")
    print("You are now entering the second level. The guards still don't know you're here so keep quiet " + name + ". You have 1 try to answer the first question, and three for the second question. Good luck.")
   
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
    third_level_ready = input ("Are you ready to move onto the next level? (Yes/No) ")
    while third_level_ready != "Yes":
        third_level_ready =  input("Type Yes when you are ready: ")  
    
    # Introduction to level 3
    print("\n<<<<LEVEL 3>>>>")
    print("You are now on level three, and getting closer to the president. The group has identifed that you are in the base, and have sent reinforcments. Questions will get harder. ")
    print ("\nYou have 2 tries to answer the first question, and 1 try to answer the second question. Good luck.")
    
    # Asking questions through for loops and if statments
    for i in range (2):
        fifth_question = input("\nMega/Gigabytes per second measures how much data can be _____? ")
        if fifth_question == "Transferred":
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
    progress_ready = input ("You will now be notified of your progress. Are you ready? (Yes/No) ")
    while progress_ready != "Yes":
        print("Take a breather.")
        progress_ready =  input("Type Yes when you are ready: ")  
    
    # Checking up on the users progress
    if total_score >= 4:
        print ("\nYou are doing very good so far " + name)
    elif total_score == 3:
        print ("\nYou are doing decent. You need to answer the next 4 questions correctly in order to save the president. ")
    else:
        print ("\nYou are not doing good. Do not worry, keep going. ")

    minigame_introduction = input ("Are you ready to move on? (Yes/No) ")
    while minigame_introduction != "Yes":
        print("Take a breather.")
        minigame_introduction =  input("Type Yes when you are ready: ")  

    # Introduction to plot twist in the game
    print("\nOh no! It has been found out that the president is no longer at the base you are in. Get to the control room quick!")
    print("You are approaching the contorl room, however the door is locked. In order to unlock the door, choose a game you want to play.")

    minigame_ready = False
    while minigame_ready == False:
        game = input("\nWould you like to play Number Guessing (1) or Code Guessing(2)? (Choose 1 or 2): ") 
        if game == "1":
            my_number = 6
            guess = int(input("\nEnter a number from 1-10: "))
            while guess != my_number:
                print ("You got it wrong. Try again. ")
                guess = int(input("Enter a number from 1-10: "))
            print ("Good, you got it correct. You may advance. ")
            minigame_ready = True
        
        elif game == "2":
            my_code = 1432
            second_guess = int(input("\nGuess my 4-digit code (Numbers range from 1-4): "))
            while second_guess != my_code:
                print ("You got it wrong. Try again. ")
                guess_2 = int(input("Guess my code from 1-4: "))
            print ("Good, you got it correct.")
            minigame_ready = True
        else:
            print ("\nPlease enter an option.")
            game = input("Would you like to play Number Guessing (1) or Code Guessing(2)? (Choose 1 or 2): ")


    # Getting ready for fourth level
    fourth_level_ready = input ("Are you ready to move on? (Yes/No) ")
    while fourth_level_ready != "Yes":
        print("Take a breather.")
        fourth_level_ready =  input("Type Yes when you are ready: ") 

    # Introduction to level 4
    print("\n<<<<LEVEL 4>>>>")
    print ("Now entering level 4. You have taken your jeep, and now approaching the fleet of cars with the president. There are three cars in total. Take out the two on either side of you, and resuce the president in the last one. ")
    print ("You only have 1 chance to answer each of the questions.")

    # Asking questions through if statments
    seventh_question = input("\nThere been an increasing amount of mental illnesses (especially within teens) due to the prolonged use of technology. (True/False) ")
    if seventh_question == "True":
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
    fifth_level_ready = input ("Are you ready to move onto the next level? (Yes/No) ")
    while fifth_level_ready != "Yes":
        fifth_level_ready =  input("Type Yes when you are ready: ")  
    
    # Introduction to Level 5
    print ("\n<<<<LEVEL 5>>>>")
    print ("Excellent, you shot down the tires on each of the cars. You are coming side by side from the last car.")
    print ("President: Oh thank god you're here " + name + ". I've been trapped here for so long. Quick, untie me and let's get out before Brutus catches us!")
    print("*Unties President*")


    print ("\nBrutus: Not so fast soldier. I never said you could take the president. ")
    print ("FINAL FACEOFF AGAINST BRUTUS! You have three questions, with 3 tries for the first question, 1 try for the second question and 3 tries for the last question")
    
    # Asking if they are ready in order to cut off some text (Makes it easier for them to read)
    questions_fifth_ready = input ("\nReady to face-off against Brutus? (Yes/No) ")
    while questions_fifth_ready != "Yes":
        questions_fifth_ready =  input("Type Yes when you are ready to start: ")  
    
    # Asking final questions
    ninth_question = input("\nWhat type of malware records everything you type on your computer? ")
    for i in range (3):
        if ninth_question == "Keyloggers":
            print ("Great, you got the first question right")
            score_5 = score_5 + 1
            total_score = total_score + 1
            break
        else:
            print ("You got it wrong. Do not worry. ")
    tenth_question = input("\n(True/False) You can apply to medical school with a computer science degree: ")
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
    print ("\nAlright soldier. Let's see if you saved the president or not.")
    print ("Your final score was " + str(total_score) + "/11.")

    final_statement_ready = input ("\nAre you ready to move on? (Yes/No) ")
    while second_level_ready != "Yes":
        second_level_ready =  input("Type Yes when you are ready to hear the results: ") 

    if total_score >= 8:
        print ("\n<<<<CONGRATULATIONS, YOU SAVED THE PRESIDENT>>>>")
        print ("You blew up the other car and took the president with you. Brutus was destroyed. Once you made it back home, you were treated for your injuries, then was awarded the Medal of Honor from the president himself.")
        print ("You are now appointed as the president's personal bodyguard. ")
    else:
        print ("\nSorry, " + name + " you did not save the president. Although you made it out fine, the president has been moved to an unknown base. The S.W.A.T team has taken over the rescue.")
    
    # Closing statment
    print ("\n<<<<THANK YOU FOR PLAYING>>>>")
