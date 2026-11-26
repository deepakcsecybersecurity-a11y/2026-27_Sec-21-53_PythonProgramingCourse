def simple_interest(p, t, r=5):
    si = (p * t * r) / 100
    return si

# Calling with default rate (5%)
print("Simple Interest with default rate:", simple_interest(10000, 2))

# Calling with explicit rate (10%)
print("Simple Interest with explicit rate:", simple_interest(10000, 2, 10))