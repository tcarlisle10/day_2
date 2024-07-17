# Nested if statements

# We can have nested if's, or if statements inside of an if statement

# Activity of the day

weather = 'sunny'
friend = 3

if weather == 'sunny':
    if friend >= 6:
        print("let's play volleyball")
    elif friend == 5:
        print("Let's play frisbee")
    else:
        if friend == 1:
            print("play golf")
        elif friend < 5:
            print("the", friend, "of us should play golf")
else:
    print("Let's go to the movies")