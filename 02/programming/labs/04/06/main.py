import game


def main(dead=False):
    """The main function."""
    lvl_4 = game.Python("Karpenko")
    lvl_3 = game.Teacher("Myru")
    lvl_2 = game.Dealer("Yunosti")
    lvl_1 = game.Mathematician("Drahomanova")
    lvl_1.link(lvl_2)
    lvl_2.link(lvl_3)
    lvl_3.link(lvl_4)
    current = lvl_1
    print(
        """
Welcome to the game!
Enter your name:"""
    )
    player = input(">>> ")
    while True:
        current.describe()
        result = current.play()
        if result == False:
            return print(f"Sorry {player}, you lost.")
            break
        else:
            print("\nGood job! Let's go to the next street.")
            current = current.forward()
            if current == None:
                break
    return print(f"Congratulations, {player}! You completed the game!")


if __name__ == "__main__":
    main()
