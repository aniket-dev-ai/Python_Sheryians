import random

# Simple Guess the Number Game using while loop


# Generate a random number between 1 and 10
secret_number = random.randint(1, 10)

# Initialize the number of attempts
attempts = 0

# Game loop starts here
while True:
    # Ask user to guess the number
    guess = int(input("Guess a number between 1 and 10: "))
    attempts += 1  # Increment attempts

    # Check if the guess is correct
    if guess == secret_number:
        print(f"Congratulations! You guessed the number in {attempts} attempts.")
        break  # Exit the loop if guessed correctly
    elif guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")

# Game ends here


# 1. Separate each digit of a number and print it on a new line
num = int(input("Enter a number to separate its digits: "))
print("Digits separated:")
while num > 0:
    digit = num % 10
    print(digit)
    num = num // 10 

# 2. Accept a number and print its reverse
num2 = int(input("Enter a number to reverse: "))
reverse_num2 = 0
while num2 > 0:
    digit = num2 % 10
    reverse_num2 = reverse_num2 * 10 + digit
    num2 = num2 // 10
print(f"Reversed number: {reverse_num2}")

# 3. Accept a number and check if it is a palindromic number
num3 = int(input("Enter a number to check if it's palindromic: "))
original_num3 = num3
reversed_num3 = 0
temp = num3
while temp > 0:
    digit = temp % 10
    reversed_num3 = reversed_num3 * 10 + digit
    temp = temp // 10

if original_num3 == reversed_num3:
    print(f"{original_num3} is a palindromic number.")
else:
    print(f"{original_num3} is not a palindromic number.")