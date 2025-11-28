# Calculates number of days until Christmas
# usage: python xmas.py

from datetime import date

today = date.today()

# use the features of datetime dates to calculate how many days to Christmas

print(f"Today is {today:%A, %d %B}")

xmas_day = date(2024, 12, 25)

interval = xmas_day - today
print(f"There are {interval.days} days until Christmas!")