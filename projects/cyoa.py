"""Adopt a computagotchi!"""


player: str = (input("What is your name? "))
points: int = 0

def main() -> None: 
    print("Welcome!")
    print(greet())
    global points
    what_pet: str = (input("Which pet would you like? dragon/hedgehog/earthworm - "))
    if what_pet == "dragon":
        print(f"\U0001F409 ! Uh oh... Unfortunately your pet breathed fire inside your computer and you are not able to take care of it. Your pet has {points} health. Goodbye! ")
    else: 
        if what_pet == "hedgehog": 
            print("\U0001F994 !")
            points = (hedgehog_next(points))
            # Get this checked 
            print (hedgehog_next(points))
            print (hoggame(points))

        else: 
            print("\U0001FAB1 !")
            print(earthworm_next(points))
            print(wormygame(points))
   
    print("Game over. We hope you enjoyed caring for your pet! If you have more than 3 points, your pet enjoyed having you too!")
    


def greet() -> str: 
    print(f"Thank you for choosing to adopt one of our very own computagotchis, {player} ! They make fabulous pets.")


def hedgehog_next(point: int) -> int: 
    print(f"What a wonderful choice, {player}!")
    feedyesno: str = input("Your pet is getting hungry! Would you like to feed it? yes/no -")
    if feedyesno == "yes":
        point += 3
        food: str = input("What would you like to feed it? carrot/bug/pizza -") 
        if food == "bug": 
            point += 2
            print(f"\U0001FAB2 Yay! Hedgehogs love bugs, {player}!")
        else: 
            if food == "pizza": 
                point += 1 
                print(f"\U0001F355 Good choice. Your pet thinks pizza is ok, {player}.")
            else:
                if food == "carrot": 
                    point -= 3 
                    print(f"\U0001F955\U0001F92E Bleh! Your pet hates vegetables, {player}. You should be a better pet parent!")
                    return point
            return point
    else:
        if feedyesno == "no":
            point -= 3 
            print(f"How cruel of you! Your pet has died from hunger AND a broken heart, {player}. Nice going.")
    return point

def hoggame(points:int) -> str: 
    sumalgo: str = input("Now your hedgehog wants to play a game. Input 3 numbers and your pet will give you the sum!")
    hoganswer: list[int] = [sumalgo]
    print(hoganswer)
# Do something else for the above and beyond this is stupid and hard 




def earthworm_next(point: int) -> str: 
    print(f"What a fantastic but boring choice, {player}...")
    global points
    feedworm: str = input("Your pet is getting hungry. What would you like to feed it? dirt/nothing - ")
    if feedworm == "dirt": 
        points += 1
        print(f"Yay! That is... er... probably what earthworms eat, {player}. ")
    else: 
        points -=1
        print(f"Not the best choice, {player}, but do earthworms even eat in the first place?")
    return (f"Your total points are {points}")

def wormygame(point:int) -> str: 
    global points
    from random import randint
    cointoss: str = input(f"Now your worm would like to play a game. Do you want to play coin toss? yes/no - ")
    if cointoss == "yes":
        points += 1
        toss: randint(1,2)
 # Input something from random library 
 
    else:
        points -= 3
        return(f"Your worm died. He got so bored because you didn't play with him so he decided to sunbathe. He is all shriveled up now, {player}, and you have {points} points.")

# named constants for emojis??? 

if __name__== "__main__":
    main()

