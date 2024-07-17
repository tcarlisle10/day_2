# If statement is our original condition
# elif allows us to chain additional conditions, with their own corresponding code blocks

# the flow of the if/elif chain reads from top down, and as soon as a conditional statement evaluates to True, that code
# block and the rest of the conditions are skipped

money = 15

if money >= 50:
    print("We can have a steak dinner")
elif money >= 20:
    print("Italian")
elif money >= 10:
    print("Chipotle")

#------------------------------#

# Else statements are essentially a default option
# They don't have a specific condition to their own, if none of the other conditions evaluate to True, the the else block will run it's code

money = 15

if money >= 50:
    print("We can have a steak dinner")
elif money >= 20:
    print("Italian")
elif money >= 10:
    print("Chipotle")
else:
    print("cook at home")

