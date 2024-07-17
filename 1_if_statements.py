# If statements

# syntax
# if (condition):
#       indent for code block

weather = "rainy"

assertion = (weather == 'sunny')
print(assertion)

#-----------------------------#

if weather == 'sunny': # if statements are always looking for a True condition/assertion
    print("Let's have a picnic!")

torch_lit = True

if torch_lit:
    print("My path is clear")

print("="*50)

# user_input = input("Would you like to go down the spooky path or the cave")

# if user_input == "spooky path":
#     print("oooooo this path goes into a scary forest")
# elif user_input == "cave":
#     print("Down into a dark cave you go!")
# else:
#     print("Enter a Valid Option")

print("="*50)

# COMPOUND CONDITIONAL STATEMENTS using 'and' or 'or' logical operators
# --- and : requires both conditions are True in order to execite the indented code block

gold_coins = 10
silver_coins = 50

if (gold_coins >= 5) and (silver_coins >= 30):
    print("You have enough to purchase!!")

# or : Requires at least one condition needs to be True in order for our code block to run

day = 'Monday'

if (day == 'Saturday') or (day == 'Sunday'): # if day == 'Saturday' or 'Sunday' wont work cause Sunday is always true in bool casting
    print("Yaaaay it's the weekend!!")

#------------------------------------------#

# Using 'and' and 'or' together

caffeinated =True
prepared_level = 5
confidence = 70

if (caffeinated and prepared_level > 6) or (confidence > 80):
    print("I'm ready!")
else: 
    print('Oh no I\'m not ready!')

dressed = True
weather = 'sunny'
num_of_friends = 4

if (dressed and num_of_friends > 3) or (weather == 'sunny'):
    print('Beach time!')

#---- using the 'not' operator

# By incorporating 'not' our if statements can now check for False conditions

busy = False

if not busy:
    print('Nice! time to relax!')

# if False:
#   run code

