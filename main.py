# Global score variables
player_wins = 0
cpu_wins = 0
ties = 0
# Add import for random
import random
# Function to choose a random throw
def random_throw():
    return random.choice(["rock", "paper", "scissors"])

# Function to normalize user input
def normalize_throw(throw):
    throw = throw.strip().lower()
    if throw in ["rock", "r"]:
        return "rock"
    elif throw in ["paper", "p"]:
        return "paper"
    elif throw in ["scissors", "s"]:
        return "scissors"
    else:
        return None

# Logic for determining the winner
def rps_logic(throw1, throw2):
    t1 = normalize_throw(throw1)
    t2 = normalize_throw(throw2)
    if t1 is None or t2 is None:
        return "Invalid input! Please choose rock, paper, or scissors."
    if t1 == t2:
        return "It's a tie!"
    elif t1 == "rock":
        if t2 == "scissors":
            return "Rock crushes scissors! Player 1 wins!"
        if t2 == "paper":
            return "Paper covers rock! CPU wins!"
    elif t1 == "paper":
        if t2 == "rock":
            return "Paper covers rock! Player 1 wins!"
        if t2 == "scissors":
            return "Scissors cut paper! CPU wins!"
    elif t1 == "scissors":
        if t2 == "paper":
            return "Scissors cut paper! Player 1 wins!"
        if t2 == "rock":
            return "Rock crushes scissors! CPU wins!"
    # Should not reach here
    return "Invalid input! Please choose rock, paper, or scissors."



def main():
    global player_wins, cpu_wins, ties
    print("Welcome to Rock Paper Scissors!")
    print(f"Score: Player Wins: {player_wins}, CPU Wins: {cpu_wins}, Ties: {ties}")
    while True:
        user_input = input("Enter your throw (rock, paper, scissors or r/p/s), or 'q' to quit: ")
        if user_input.strip().lower() in ["q", "quit", "exit"]:
            print("Thanks for playing!")
            print(f"Final Score: Player Wins: {player_wins}, CPU Wins: {cpu_wins}, Ties: {ties}")
            break
        computer_throw = random_throw()
        print(f"Computer chose: {computer_throw}")
        result = rps_logic(user_input, computer_throw)
        print(result)
        # Update scores
        t1 = normalize_throw(user_input)
        t2 = normalize_throw(computer_throw)
        if t1 is None:
            continue
        if t1 == t2:
            ties += 1
        elif (t1 == "rock" and t2 == "scissors") or (t1 == "paper" and t2 == "rock") or (t1 == "scissors" and t2 == "paper"):
            player_wins += 1
        else:
            cpu_wins += 1
        print(f"Score: Player Wins: {player_wins}, CPU Wins: {cpu_wins}, Ties: {ties}")

if __name__ == "__main__":
    main()
