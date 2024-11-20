#Take user input as a string of digits
a = input("Enter the number a: ")
b = input("Enter the number b: ")

# Convert the input to sets of digits (this automatically removes duplicates)
set_a = set(a)
set_b = set(b)

# union_a_b is one varible that varible is store the set_a.union(set_b)
#union is a method that is used to combine the two sets and return the new set

union_a_b=set_a.union(set_b)
#the new set is stored in union_a_b
print("Union of a and b:",union_a_b)
#intersection_a_b is one varbile that varible is store the set_a.intersection(set_b)
#intersection is a method that is used to find the common element to given two set.and stored in new set

intersection_a_b=set_a.intersection(set_b)
print("intersection of a and b:",intersection_a_b)

#complement_b is one varible that varible is store the set_a-set_b
#complement is a method that is used to find the elements that are in set_a but not in set_b

complement_b_in_a = set_a - set_b

# Print the result
print("Complement of b in a:", complement_b_in_a)
