import random

# List of suspects
suspects = ["Alice", "Bob", "Charlie"]

# Dictionary of clues
clues = {
    "Alice": "I was reading a book in the library.",
    "Bob": "I was fixing my car in the garage.",
    "Charlie": "I was taking a walk in the garden."
}

# Randomly choose the murderer
murderer = random.choice(suspects)


def show_suspects():
    print("\nSuspects:")
    for suspect in suspects:
        print("-", suspect)


def interrogate():
    name = input("\nWho would you like to interrogate? ")

    if name in clues:
        print(f"{name} says: {clues[name]}")
    else:
        print("That suspect does not exist.")


def accuse():
    guess = input("\nWho do you accuse of being the murderer? ")

    if guess == murderer:
        print("\n🎉 Correct! You solved the mystery!")
    else:
        print(f"\n❌ Wrong! The murderer was {murderer}.")
    
    print("Game Over.")
    return True


def main():
    print("=== MURDER MYSTERY GAME ===")
    print("A crime has been committed. Find the murderer!")

    game_over = False

    while not game_over:
        print("\nOptions:")
        print("1. View suspects")
        print("2. Interrogate suspect")
        print("3. Accuse suspect")

        choice = input("Choose an option: ")

        if choice == "1":
            show_suspects()

        elif choice == "2":
            interrogate()

        elif choice == "3":
            game_over = accuse()

        else:
            print("Invalid choice. Try again.")


# Start the game
main()
