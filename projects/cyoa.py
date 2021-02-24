"""Adopt a computagotchi!"""


def main() -> None: 
    print("Welcome!")
    print(greet())
    points: int = 0
    what_pet: str = (input("Which pet would you like? dragon/hedgehog/earthworm - "))
    if what_pet == "dragon":
        print(f"\U0001F409 ! Uh oh... Unfortunately your pet breathed fire inside your computer and you are not able to take care of it. Your pet has {points} health. Goodbye! ")
    else: 
        if what_pet == "hedgehog": 
            print("\U0001F994 !")
            (hedgehog_next(points))
        else: 
            print("\U0001FAB1 !")
            print(earthworm_next)
            

def greet() -> str: 
    print(f"Thank you for choosing to adopt one of our very own computagotchis, {player} ! They make fabulous pets.")


def hedgehog_next(points) -> str: 
    print(f"What a wonderful choice, {player}!")
    feedyesno: str = input("Your pet is getting hungry! Would you like to feed it? yes/no -")
    if feedyesno == "yes":
        points += 1 
        food: str = input("What would you like to feed it? carrot/bug/pizza -") 
        if food == "bug": 
            points += 2
            print(f"\U0001FAB2 Yay! Hedgehogs love bugs, {player}!")
        else: 
            if food == "pizza": 
                points += 1 
                print(f"\U0001F355 Good choice. Your pet thinks pizza is ok, {player}.")
            else:
                if food == "carrot": 
                    points -= 3 
                    print(f"\U0001F955\U0001F92E Bleh! Your pet hates vegetables, {player}. You should be a better pet parent!")
    else:
        if feedyesno == "no":
            points -= 3 
            print(f"How cruel of you! Maybe your pet will learn to be just as evil, {player}.")

def earthworm_next() -> int: 
    print("y")



player: str = (input("What is your name? "))
points: int = 0

if __name__== "__main__":
    main()

