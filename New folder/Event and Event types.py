"""Random Module is a one type of module in python whiuch is used in generated random numbers make
random choices"""
import random

#Define outcomes

cards=["red","black","green"]#cards
dies_faces=[1,2,3,4,5,6]#Dies faces

#die_roll is one varible which is used to store the random choice of dies_faces
#random.choice is a function in python is method from the random module.random.choice() function is used to select a random element from a list 

die_roll=random.choice(dies_faces)
#This is one type of event which is called single event
#if the condtion is true then it is called single event
if die_roll==2:
     print("Single Event: You rolled a 2!")
else:
     print("Not a single event:you rolled a number other than 2")

#this is one type of event which is called compound event
#Compound event is a combination of two or more single events
#card_draw is one varbile which is used to store the random choice of cards.random.choice is a function in python is method from the random module. random.choice() is use the to take the random is pick one value.

card_draw = random.choice(cards)
#die_roll is one varible which is used to store the random choice of dies_faces. random.choice is afunction in python.this function helps to pick the random value.

die_roll = random.choice(dies_faces)
#in the condtion if the card_draw is red and die_roll is even number that condtion is true then it is stored is collection of outcomes.
if card_draw == 'red' and die_roll % 2 == 0:
    print("Compound Event: Red card and even number rolled!")
    #whenever the first condtiion is false then the second condtiom is checked.
else:
     print("No special event occurred")

# Impossible Event: Rolling a 7 on a 6-sided die
impossible_roll = 7 in dies_faces
print(f"Impossible Event: Can we roll a 7? {'Yes' if impossible_roll else 'No'}")

# Certain Event: Rolling a number between 1 and 6
certain_event = die_roll in dies_faces
print(f"Certain Event: Rolled a number between 1 and 6? {'Yes' if certain_event else 'No'}")