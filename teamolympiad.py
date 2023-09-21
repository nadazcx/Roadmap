numbe = int(input())
thenumbers = input().split()  # Split the input string into a list of strings
thenumbers = [int(x) for x in thenumbers]  # Convert the list of strings to a list of integers

# Initialize counts for digits 1, 2, and 3
count_1 = thenumbers.count(1)
count_2 = thenumbers.count(2)
count_3 = thenumbers.count(3)

# Calculate the minimum count among the three digits
min_count = min(count_1, count_2, count_3)

if min_count == 0:
    print(0)
else:
    print(min_count)

    for i in range(min_count):
        # Find the indices of the first occurrence of each digit
        idx_1 = thenumbers.index(1) + 1
        idx_2 = thenumbers.index(2) + 1
        idx_3 = thenumbers.index(3) + 1

        # Print the indices
        print(f"{idx_1} {idx_2} {idx_3}")

        # Set the used digits to 0 to avoid reusing them
        thenumbers[thenumbers.index(1)] = 0
        thenumbers[thenumbers.index(2)] = 0
        thenumbers[thenumbers.index(3)] = 0
