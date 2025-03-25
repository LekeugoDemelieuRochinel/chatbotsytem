import random 

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        quit()
        print("Please Enter a Number Lager Than 0 Next Time.")
else: 
    print("Pease type a number next time.")
    quit()
    
random_number = random.randint(0, top_of_range)
print(top_of_range)

guesses = 0

while True:

    guesses += 1

    user_guess = input("Make a guess :")

    if user_guess.isdigit():
        user_guess = int(user_guess)

    else:
        print("Please type number next time")
        continue

    if user_guess == random_number:
        print("you got it !")
        break

    elif user_guess > random_number:

        print("You were above the number")

    else:
       print("You were below the number")
      
print("you got it in ", guesses, " guesses")






 
