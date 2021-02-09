"""A vaccination calculator."""

__author__ = "730316492"

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import datetime

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
from datetime import timedelta


# Begin your solution here...
population: int = int(input("Population: "))
doses: int = int(input("Doses administered: "))
doses_day: int = int(input("Doses per day: "))
percent: int = int(input("Target percent vaccinated: "))

new_percent = percent / 100

days: int = round((population * new_percent - doses / 2) * 2 / doses_day)
final_percent: int = new_percent * 100 
string_days = str(int(days))
string_percent = str(int(final_percent))

today: datetime = datetime.today()
days_delta = timedelta(days)
future: datetime = (today) + days_delta

print("We will reach " + string_percent + "% vaccination in " + string_days + " days, Which falls on " + future.strftime("%B %d, %Y"))