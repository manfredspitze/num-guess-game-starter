# Programmer: 
# Date: 
# Number Guess Game 


# 1. Import Python's random and time modules




fname = input("Hello! What is your first name?\n")

# 2. Use the randint( ) method to generate a random 
# number between 1 and 50

# https://www.w3schools.com/python/ref_random_randint.asp

# 3. Use two variables to specify the range (from 1 up to and including 50)

rand_number = # Add missing code here...



# 4. Greet user and display username in title case
time.sleep(2)
print(f"Greetings, {fname}! I'm thinking of a number between 1 and 50...")




guesses_made = 0
max_guesses # 5. Set the maximum number of guesses allowed to 5


# Set up the WHILE loop
while guesses_made < max_guesses:

		guess = input("Enter your guess:\n")
		
		if guess.isdigit() is not True:
			print('Please enter only numbers!')
			continue
		else:
			guess = int(guess)
			
		# 5. Check that user's guess is between 1 and 50; use
		# variables in the conditional statement to perform this check
		# if missing_code and missing_code:
		
		
			guesses_made = guesses_made + 1
			
			# 6. Write an IF statement that checks if the guess matches
			# the randomly generated mystery number
			
			# if missing_code:
			
			
				print(f"Congratulations, {fname.title()}!")
				print(f"You guessed the mystery number -- {rand_number} -- in {guesses_made} tries!")
				break # Stop looping immediately
				
			elif guess < rand_number and guesses_made < 5:
				print("Too low! Try again!")
				print(f"Guesses remaining: {max_guesses - guesses_made}")
				
			elif guess > rand_number and guesses_made < 5:
				print("No, too high!")
				print(f"Guesses remaining: {max_guesses - guesses_made}")
				
			elif guesses_made == max_guesses:
				print('Sorry! You used up all your guesses!')
				print(f'The mystery number was: {rand_number}')
				
				
		else:
			print("Invalid input! Please enter a number from 1 to 50!")
			


		


