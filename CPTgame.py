print ("<<<<<Welcome to ______!>>>>")

# Asking user for their name so the game can adress the user by their name
name = input(("To start, what is your name soilder? "))
# First bit of user input telling them to advance; instructions for the user; storyline
start_game = input("You are now on the loading screen. Type start to continue to the instructions. ")
if start_game == "start":
    print ("Colnel: The president has been held hostage by an unidentified group. It is your job to rescue the president. In order to do so, you must complete each level answering 2/2 questions. There are 5 levels in total. ")
    print ("Colnel: Good luck " + name)