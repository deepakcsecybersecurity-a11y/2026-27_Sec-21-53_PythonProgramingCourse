set1 = {10, 20, 30, 40, 50}

print("Original Set:", set1)

# Membership testing
print("Is 20 present?", 20 in set1)
print("Is 60 present?", 60 in set1)

# Add an element
set1.add(60)
print("After adding 60:", set1)

# Remove an element
set1.remove(30)
print("After removing 30:", set1)

# Discard an element
set1.discard(40)
print("After discarding 40:", set1)