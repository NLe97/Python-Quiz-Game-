print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's Play :) ")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score +=1
    #same as score = score + 1
else: 
    print("Incorrect!")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphic processing unit":
    print("Correct!")
    score +=1
else: 
    print("Incorrect!")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score +=1
else: 
    print("Incorrect!")

answer = input("what does PSU stand for? ")
if answer.lower() == "power supply unit":
    print("Correct!")
    score +=1
else: 
    print("Incorrect!")
#str method to convert passed in variable to string 
# combining strings below
print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%.")