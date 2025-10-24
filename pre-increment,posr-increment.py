# Demonstrating pre-increment and post-increment behavior in Python

# Initial value
a = 5
b = 5

print("Original values: a =", a, ", b =", b)

# Simulating post-increment: value is used first, then increment
post_increment = a
a += 1
print("Post-increment simulation: value used =", post_increment, ", a after increment =", a)

# Simulating pre-increment: increment first, then value is used
b += 1
pre_increment = b
print("Pre-increment simulation: value used =", pre_increment, ", b after increment =", b)
