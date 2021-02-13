"""Vaccine calculator exercise as a structured program."""

from datetime import datetime, timedelta

__author__ = "730316492"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    population: int = int(input("Population: "))
    doses: int = int(input("Doses administered: "))
    doses_per_day: int = int(input("Doses per day: "))
    target: int = int(input("Target percent vaccinated: "))
    # TODO 2: Call days_to_target and store result in a variable.
    x = days_to_target(population, doses, doses_per_day, target)
    # TODO 4: Call future_date and store result in a variable.
    y = future_date(x)
    # TODO 5: Print the expected output using the variables above.
    print("We will reach " + str(target) + "% vaccination in " + str(x) + " days, which falls on " + str(y))

# TODO 1: Define days_to_target function
def days_to_target(population: int, doses: int, doses_per_day: int, target: int) -> int:
    """Finds number of days."""
    new_target = target / 100
    days: int = round((population * new_target - doses / 2) * 2 / doses_per_day)
    return days 

# TODO 3: Define future_date function
def future_date(x: int) -> str:
    """Finds the future date."""
    today: datetime = datetime.today()
    days_delta = timedelta(x)
    future: datetime = (today) + days_delta
    return future.strftime("%B %d, %Y")

if __name__ == "__main__":
    main()
