#This is the random varible
# importing random module
import random

#creating the function that is used to roll the die
def roll_die():
    #using the random.randint function to generate the random number between 1 and 6
    
    return random.randint(1, 6)

# Simulate rolling the die 10 times
outcomes = [roll_die() for _ in range(10)]

print("Outcomes of rolling a die 10 times:", outcomes)

#This is the Continuous Random
#importing the random  module
import random

# Simulating a continuous random variable
#creating the function that funcation is name train_arrival_time
def train_arrival_time():
    
    return random.uniform(1, 10)  # Generates a random float between 1 and 10

# Simulate train arrival times
times = [train_arrival_time() for _ in range(5)]
print("Simulated train arrival times:", times)
