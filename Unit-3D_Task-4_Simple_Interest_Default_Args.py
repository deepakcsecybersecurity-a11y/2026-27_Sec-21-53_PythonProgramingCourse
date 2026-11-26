def simple_interest(p, t, r=5):
    si = (p * t * r) / 100
    return si

# Calling with default rate
p = 10000
t = 2

print("Simple Interest with default rate:", simple_interest(p, t))

# Calling with explicit rate
r = 10

print("Simple Interest with explicit rate:", simple_interest(p, t, r))