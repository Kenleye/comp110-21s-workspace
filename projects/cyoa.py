"""Adopt a computagotchi!"""
from random import randint

player: str = ""
points: int = 0
a: str = ""
b: str = ""
DRAGON: str = "\U0001F409"
HEDGEHOG: str = "\U0001F994"
WORM_EMOJI: str = "\U0001FAB1"
BUG: str = "\U0001FAB2"
PIZZA: str = "\U0001F355"
CARROT: str = "\U0001F955"
THROW_UP: str = "\U0001F92E"
COIN_TOSS: str = "\U0001FA99"

def main() -> None: 
    """Main function."""
    greet()
    global points
    what_pet: str =  input(f"Which pet would you like {player}? dragon/hedgehog/earthworm - ")
    if what_pet == "dragon":
        print(f"{DRAGON}! Uh oh. Your pet ate your computer's insides. You are unable to take care of it.")
    else: 
        if what_pet == "hedgehog": 
            print(f"{HEDGEHOG}!")
            points = (hedgehog_next(points))
            print(f"You have {points} points.")
            print(hoggame(a, b))

        else: 
            print(f"{WORM_EMOJI} !")
            print(earthworm_next(points))
            print(wormygame(points))
   
    print("Game over. We hope you enjoyed caring for your pet! If you have >2 points, your pet enjoyed you too!")
    print(f"Your total points are {points}")
    while input("Would you like to adopt again? yes/no - ") == "yes":
        return main()

def greet() -> None:
    """Saying hello.""" 
    print(f"Welcome! Thank you for choosing to adopt one of our computagotchis! They make fabulous pets.")
    global player
    player = input("What is your name? ")
    return None
    

def hedgehog_next(point: int) -> int: 
    """When you choose to adopt a hedgehog."""
    print(f"What a wonderful choice, {player}!")
    feedyesno: str = input("Your pet is getting hungry! Would you like to feed it? yes/no -")
    if feedyesno == "yes":
        point += 3
        food: str = input("What would you like to feed it? carrot/bug/pizza -") 
        if food == "bug": 
            point += 2
            print(f"{BUG} Yay! Hedgehogs love bugs, {player}!")
            return point
        else: 
            if food == "pizza": 
                point += 1 
                print(f"{PIZZA} Good choice. Your pet thinks pizza is ok, {player}.")
                return point
            else:
                point -= 3 
                print(f"{THROW_UP}{CARROT}Bleh! Your pet hates veggies, {player}. You should be a better pet parent!")
                return point
    else:
        point -= 3 
        print(f"How cruel of you! Your pet is hungry AND has a broken heart, {player}. Nice going.")
        return point


def hoggame(a: str, b: str) -> str: 
    """Above and beyong additional interactions."""
    print("Your pet wants to play! Input two numbers one at a time and your pet will tell you which is the largest!")
    a = input("Value a - ")
    b = input("Value b - ")
    if a >= b:
        return a

    return b


def earthworm_next(point: int) -> str: 
    """When you chose to adopt an earthworm."""
    print(f"What a fantastic but boring choice, {player}...")
    global points
    feedworm: str = input("Your pet is getting hungry. What would you like to feed it? dirt/nothing - ")
    if feedworm == "dirt": 
        points += 1
        print(f"Yay! That is... er... probably what earthworms eat, {player}. ")
    else: 
        points -= 1
        print(f"Not the best choice, {player}, but do earthworms even eat in the first place?")
    return (f"You have {points} points")


def wormygame(point: int) -> str: 
    """Incorporates elements of randomness from the random library."""
    global points
    cointoss: str = input(f"Now your worm would like to play coin toss. Do you want to play?{COIN_TOSS}  yes/no - ")
    if cointoss == "yes":
        points += 3
        print(f"Yay, {player}! If the toss is a '1' you get a point! If the toss is a '2' you get -1 point.")
        toss: int = randint(1, 2)
        if toss == 1: 
            points += 1
            print("The toss was a 1! Yay!")
            return (f"You have {points} points.")
        else:
            points -= 1
            print("The toss was a 2. Boo!")
            return (f" You have {points} points.")
    else:
        points -= 3
        print(f"Your worm got bored he decided to sunbathe. He is shriveled up now and dead, {player}.")
        return (f"You have {points} points.")


if __name__ == "__main__":
    main()