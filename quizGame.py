print("Welcome to my Computer Quiz!")

playing = input("Do you want ot play? ")
# print(playing)

if playing.lower() != "yes":  # True 
    quit()

print("Great! Let's get going :)")
score = 0

answer = input("What does CPU stand for? ").lower()

if answer == "central processing unit":
    print("Correct! :)")
    score += 1
else:
    print("Incorrect! :(")

answer = input("What does RAM stand for? ").lower()

if answer == "random access memory":
    print("Correct! :)")
    score += 1
else:
    print("Incorrect! :(")

answer = input("What does GPU stand for? ").lower()

if answer == "graphics processing unit":
    print("Correct! :)")
    score += 1
else:
    print("Incorrect! :(")

answer = input("What does PSU stand for? ").lower()

if answer == "power supply":
    print("Correct! :)")
    score += 1
else:
    print("Incorrect! :(")

print("You got " + str(score) + " questions correct!")
