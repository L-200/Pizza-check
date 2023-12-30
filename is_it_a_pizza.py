print("Hello, this wil help you indentify wether your food is a pizza")
print("Are you eating a pizza?(please say yes or no)")
awnser = input() # user input 
if awnser == "yes" or awnser =="Yes" or awnser =="YES":  #check if awnser says yes
    print("You are eating a pizza, congratulations :)")

elif awnser == "no" or awnser=="No" or awnser =="NO": #check if awnser says no
    print("You are not eating a pizza, sorry :(")

else:
    print("I don't know how to read what you said")
import time
time.sleep(4.5)