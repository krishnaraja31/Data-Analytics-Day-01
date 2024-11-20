# Function to calculate union probability using the addition law
#create one function the function name is addition_law_probabilty
#and pass the parmeters p_a,p_b,p_a_and_b
def addition_law_probability(P_A, P_B, P_A_and_B):
    #this addition_law_probabilty is function call that time return the P_A+P_B-P_A_and_B
    #P_A_and_B is the probability that both events A and B happen simultaneously (i.e., the intersection of A and B).
    return P_A + P_B - P_A_and_B

# Function to calculate intersection probability for independent events
#create one function that function name is multiplication_independent
#amd pass the parmeters p_a,p_b
def multiplication_independent(P_A, P_B):
    #this multiplication_independent is call function that time is return the P_A*P_B 
    return P_A * P_B

# Function to calculate intersection probability for dependent events
#Create one function thaat functiuon name is multiplication_dependent 
#and pass the parameters p_a,p_b_given_a
def multiplication_dependent(P_A, P_B_given_A):
    #this multiplication_dependent is call fuction that time return the P_A*P_B_given_A
    return P_A * P_B_given_A

# Example usage

# Probabilities for union
P_A = 0.5  # Probability of event A
P_B = 0.6  # Probability of event B
P_A_and_B = 0.2  # Probability of both A and B happening

# Calculate union probability
P_A_or_B = addition_law_probability(P_A, P_B, P_A_and_B)
print(f"The probability of A or B occurring is: {P_A_or_B}")

# Probabilities for intersection (independent events)
P_A_independent = 0.5  # Probability of event A
P_B_independent = 0.6  # Probability of event B

# Calculate intersection probability for independent events
P_A_and_B_independent = multiplication_independent(P_A_independent, P_B_independent)
print(f"The probability of both A and B occurring (independent events) is: {P_A_and_B_independent}")

# Probabilities for intersection (dependent events)
P_A_dependent = 0.5  # Probability of event A
P_B_given_A = 0.4  # Probability of B given A has occurred

# Calculate intersection probability for dependent events
P_A_and_B_dependent = multiplication_dependent(P_A_dependent, P_B_given_A)
print(f"The probability of both A and B occurring (dependent events) is: {P_A_and_B_dependent}")