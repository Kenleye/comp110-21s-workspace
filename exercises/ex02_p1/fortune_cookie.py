"""Fortune cookie exercise redux as a structured program."""

from random import randint

__author__ = "730316492"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    print("Your fortune cookie says...")
    # TODO 2 
    print(fortune_cookie())
    print("Now, go spread positive vibes!")


# TODO 1: Define your fortune_cookie function here.
def fortune_cookie() -> str: 
    """Program to tell you a fortune."""
    magic_number: int = randint(1, 11)
    if magic_number == 2: 
        return("you will get an A in COMP110")
    else: 
        if magic_number == 4:
            return("you will fail COMP110")
        else:
            if magic_number == 6:
                return("you are amazing and your COMP110 grade doesn't define you")
            else: 
                if magic_number == 8:
                    return("you are so good at COMP110 you will be the next Kris Jordan")
                else:
                    return("you should stick to being a psych major")


if __name__ == "__main__":
    main()