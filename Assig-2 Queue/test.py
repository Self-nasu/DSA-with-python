# Input a number from the user
num = int(input("Enter a number: "))

# Initialize a variable to store the sum of digits
digit_sum = 0

# Convert the number to a string to iterate through its digits
num_str = str(num)

# Iterate through each digit and add it to digit_sum
for digit in num_str:
    digit_sum += int(digit)

# Print the sum of digits
print("Sum of digits:", digit_sum)
