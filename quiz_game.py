print("Wellcome to my computer quiz!")

playing = input("Do you want to play the game? ")

print(playing)

if playing.lower() != "yes":
    #  i converte the value enter by the user in lower case by using .lower() function
    # and we also use the .upper()case function 
    quit()

print("Okay Let's play :)")

score = 0

answer = input("What does ML stand for in artifitial intelligence: ").lower()

if answer == "machine learning":
    print(f"yes is true it mean {answer}")
    score += 1

else:
    print("you are wrongth ")

answer = input("What does DL stand for in artifitial intelligence: ").lower()

if answer == "deep learning":
    print(f"yes is true it mean {answer}")
    score += 1

else:
    print("you are wrongth ")


answer = input("What does AI stand for in : ").lower()

if answer == "artifitial intelligence":
    print(f"yes is true it mean {answer}")
    score += 1

else:
    print("you are wrongth ")
answer = input("What does ALU stand for in computer architecture: ").lower()

if answer == "arithmetic logic unit":
    print(f"yes is true it mean {answer}")
    score += 1

else:
    print("you are wrongth ")


print("you score " + str(score) + " question correct!")
print("you score " + str((score / 4) * 100 ) + "%.")

