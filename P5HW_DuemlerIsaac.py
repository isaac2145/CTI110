#Isaac Duemler
#07/19/2025
#P5HW
#number game




import random

def initialize_game_settings(lower_bound, upper_bound):
    game_data = {
        "secret_number": random.randint(lower_bound, upper_bound),
        "lower_bound": lower_bound,
        "upper_bound": upper_bound,
        "attempts": 0,
        "game_over": False,
        "emoji": "🔢"
    }
    return game_data

def get_player_guess(game_settings):
    while True:
        try:
            guess_str = input(f"Guess a number between {game_settings['lower_bound']} and {game_settings['upper_bound']}: ")
            guess = int(guess_str)
            if game_settings['lower_bound'] <= guess <= game_settings['upper_bound']:
                return guess
            else:
                print(f"🚫 Please enter a number within the range!")
        except ValueError:
            print("❌ Invalid input. Please enter a whole number.")

def provide_feedback(guess, secret_number):
    if guess < secret_number:
        return "Too low! Try higher.⬆️"
    elif guess > secret_number:
        return "Too high! Try lower.⬇️"
    else:
        return "That's it! You guessed the number! 🎉"

def main():
    print("Welcome to the Number Guessing Game! " + initialize_game_settings(1,100)['emoji'])
    print("I'm thinking of a number between 1 and 100.")

    game_settings = initialize_game_settings(1, 100)
    secret_number = game_settings["secret_number"]


    while not game_settings["game_over"]: 
        player_guess = get_player_guess(game_settings)

        if player_guess is not None:
            game_settings["attempts"] += 1
            feedback = provide_feedback(player_guess, secret_number)
            print(feedback)

            if player_guess == secret_number:
                game_settings["game_over"] = True
                print(f"You guessed it in {game_settings['attempts']} attempts! Great job! ✅")

                play_again = input("Do you want to play again? (yes/no): ").lower().strip()
                if play_again == 'yes':
                    main()
                else:
                    print("Thanks for playing! Goodbye. 👋")
                return
if __name__ == "__main__":
    main()
