"""EX03 - avoid_fifth function."""

__author__: str = "730316492"


def main() -> None:
    """Entrypoint of the program."""
    print(avoid_fifth("hello"))
    print(avoid_fifth("The sentence we have here possesses E's galore!"))
 

def avoid_fifth(x: str) -> str:
    """No mor3 3s... 3v3r again."""
    i: int = 0
    answer: str = ""
    while i < len(x): 
        if x[i] != "e" and x[i] != "E":
            answer = answer + x[i]
        i += 1
    return answer
    

if __name__ == "__main__":
    main()