"""First i am create function that function name is Function1
and two parameter is pass in this function .First paramter is
favoribleoutcomes and secound parameter is totaloutcomes.

"""
def Function1(favoribleoutcomes,totaloutcomes):

    """This is the function that calculate the probabity of the event
    """

    return favoribleoutcomes/totaloutcomes

# Example: Probability of rolling a 3 on a six-sided die

favoribleoutcomes=int(input("Enter the Number of favorible outcomes:"))# Rolling a 3 is the favorable outcome

totaloutcomes=int(input("Eneter the number of total out comes:"))# Possible outcomes are 1, 2, 3, 4, 5, 6

#Creating the object of the function

object=Function1(favoribleoutcomes,totaloutcomes)

print(f"The probability of rolling a 3 is: {object}")
