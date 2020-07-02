# Create a list. Append the names of your colleagues and friends to it.
# Has the id of the list changed? Sort the list. What is the first item on
# the list? What is the second item on the list?


my_list = []
print(id(my_list))
my_list.extend(['cece', 'phoebe', 'amelia'])
print(my_list)
print(id(my_list))
print(id(my_list[2]))

# the id of my_list remains the same before and after appending but changes in each run.

sorted_list = sorted(my_list)
print(sorted_list)  # sorted list
print(sorted_list[0: 2])  # prints first and second item on the list
