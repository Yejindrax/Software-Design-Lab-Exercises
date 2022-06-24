#You are going to create a python guessing game.
#Using your knowledge of relational operators,Boolean expressions and the powerful if else
#statement,you are going to create program,with the following requirements:
#First it asks the user, what's my favorite food?
#If the user enters the name of your favorite food, output,“Yep!So amazing!”
#If the user doesn't enter the name of your favorite food, output,“Yuck!That's not it!”
#Regardless of what the user enters, output,” Thanks for playing!"

guess_food = input("What's my favorite food?")

if guess_food == "chopsuey":
    print("Yep! So amazing!")
else:
    print("Yuck! That's not it!")

print("Thanks for playing!")