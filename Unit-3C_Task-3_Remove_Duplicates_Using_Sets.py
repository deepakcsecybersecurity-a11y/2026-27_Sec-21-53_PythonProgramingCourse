list1 = [10, 20, 30, 20, 40, 10, 50, 30]

print("Original List:", list1)

# Convert list into set
set1 = set(list1)

# Convert set back into list
list2 = list(set1)

print("List after removing duplicates:", list2)