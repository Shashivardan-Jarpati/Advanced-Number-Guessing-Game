# Advanced_Number_Guessing_Game.py

import random

def get_difficulty():    
    # Prompt the player to choose a difficulty level or quit
    print("\nSelect difficulty level:")
    print("1 - Easy (prime odd numbers 1-50, 5 attempts)")
    print("2 - Medium (Prime numbers 1-40, 5 attempts)")
    print("3 - Hard (Integers 1-30, 5 attempts)")
    while True:
        choice = input("Enter difficulty (1/2/3) or 'q' to quit: ").strip().lower()
        if choice in ("1", "2", "3"):
            return int(choice)
        elif choice == 'q' 'r':
            return None
        print("Invalid choice, please enter 1, 2, 3 or 'q' to quit.")

def generate_prime_list(n):
    # Generate a list of prime numbers from 2 to n
    primes = []
    for num in range(2, n + 1):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

def get_range_and_attempts(difficulty):
    # Return the valid number list and max attempts based on difficulty level
    if difficulty == 1:
        return list(range(1, 51)), 5         # Easy: whole numbers 1 to 50
    elif difficulty == 2:
        return generate_prime_list(40), 5    # Medium: primes from 1 to 40
    else:
        return list(range(1, 31)), 5         # Hard: integers from -30 to 30

def proximity_hint(diff):
    # Provide a qualitative hint based on how far off the guess is
    if diff > 20:
        return "Ice cold"
    elif diff > 10:
        return "Cold"
    elif diff > 5:
        return "Warm"
    elif diff > 2:
        return "Hot"
    else:
        return "Very hot"

def play_round(difficulty):
    # Play one round of guessing with the chosen difficulty
    valid_numbers, max_attempts = get_range_and_attempts(difficulty)
    number_to_guess = random.choice(valid_numbers) # Select secret number from valid list
    attempts = 0

    print(f"\nI'm thinking of a number from the valid set. You have {max_attempts} attempts to guess it.")
    print(f"Valid numbers count: {len(valid_numbers)}")

     # Loop until player runs out of attempts
    while attempts < max_attempts:
        try:
            guess = int(input("Make a guess: "))

            # Check guess validity
            if guess not in valid_numbers:
                print("Your guess is not in the valid number set for this difficulty. Try again.")
                continue
            attempts += 1
            diff = abs(number_to_guess - guess)

            # Correct guess condition

            if guess == number_to_guess:
                print(f"Correct! You guessed it in {attempts} attempts.")

            # Calculate and return score: more points for fewer attempts and higher difficulty

                return max_attempts - attempts + difficulty * 5
            else:
                hint = proximity_hint(diff)
                print(f"Wrong. Hint: {hint}. Attempts left: {max_attempts - attempts}")

        except ValueError:
            # Handle invalid input (non-integers)
            print("Invalid input. Please enter an integer.")

    # After all attempts used, reveal the secret number

    print(f"Sorry, you ran out of attempts. The number was {number_to_guess}.")
    return 0

def main():
    print("Welcome to the Advanced Number Guessing Game!")
    total_score = 0

    # Main game loop continues until player chooses to quit

    while True:
        difficulty = get_difficulty()
        if difficulty is None:
            print("Thanks for playing! Goodbye.")
            break

        rounds = 3 # Number of rounds per session

        for r in range(1, rounds + 1):
            print(f"\n--- Round {r} ---")
            score = play_round(difficulty)
            total_score += score
            print(f"Round {r} score: {score}")

        print(f"\nGame over! Your total score is: {total_score}")
        total_score = 0      # Reset score for a new game
        
        again = input("Do you want to play again? (y/n): ").strip().lower()
        
        if again != 'y':
            print("Thanks for playing! Goodbye.")
            break           
if __name__ == "__main__":
    main()
