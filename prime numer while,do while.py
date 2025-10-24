# Using for loop
print("Using for loop:")
for i in range(1, 101):
    print(i, end=" ")
print("\n")

# Using while loop
print("Using while loop:")
i = 1
while i <= 100:
    print(i, end=" ")
    i += 1
print("\n")

# Simulating do-while loop
print("Using simulated do-while loop:")
i = 1
while True:
    print(i, end=" ")
    i += 1
    if i > 100:
        break
