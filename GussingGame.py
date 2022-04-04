import random

number = random.randint(1, 9)

# chances for the user - usually 5 
chances = 0.



# Subtitle
print('Guess a number (between 1 and 9): ')

# while loop to count number of chances
while chances < 5:

     # User promt to enter his/her guess
     print()
     guess = int(input("Enter your guess:- "))

     # Compare the user entered number with the number to be guessed
     if guess == number:
          # if number entered by user is same as the generated
          # number by randint function then break from loop using loop
          # control statement "break"
          print("Congratulations!! YOU WIN ")
          print()
          break

     # Check if the user entered number is smaller than the generated number
     elif guess < number:
          print("Your guess was too low: Guess a number higher than ", guess)

    # The user entered number is greater than the generated number
     else:
         print("Your guess was too high: Guess a number lower than", guess)

     # Increase the value of chance by 1
     chances = chances + 1

# Check whether the user guessed the correct number
if not chances < 5:
     print()
     print("YOU LOSE !!! The number is ", number)      
     print()
     