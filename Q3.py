# Write code that will print out the anagrams (words that use the same
# letters) from a paragraph of text.

# Method 1

string = ["tod", "salt", "dot", "last", "mood", "doom"]
my_dict = {}
index = 0
for i in range(0, len(string)):
    orginal = string[index]
    first = ''.join(sorted(orginal))
    for j in range(index+1, len(string)):
        second = ''.join(sorted(string[j]))
        if first == second:
            my_dict.update({orginal: string[j]})
    index += 1
print("The anagrams are: ", my_dict)
print('\n')


# Method 2

string = ["tod", "salt", "dot", "last", "mood", "doom"]
for i in string:
    for j in string:
        if len(i) == len(j) and i != j:
            for item in range(len(i)):
                for items in range(len(j)):
                    if i[item] == j[items]:
                        result = j
    print("The anagram of {} is:".format(i), result)



