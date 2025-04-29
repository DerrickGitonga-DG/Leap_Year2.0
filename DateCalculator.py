from calendar import month


class DateCalculator:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def calculate_day_of_week(self):
        if self.month == 1 or self.month == 2:
            adjusted_month = self.month + 12
            adjusted_year = self.year - 1
        else:
            adjusted_month = self.month
            adjusted_year = self.year

        q = self.day
        m = adjusted_month
        k = adjusted_year % 100
        j = adjusted_month // 100

        #zeller's formula
        h = (q + (13* (m+1)) // 5 + k + (k // 4) + (j // 4) + (5 * j)) % 7

        days_of_week = ["Saturday","Sunday","Monday","Tuesday","Wednesday","Thursday","Friday"]

        return days_of_week[h]

try:
    year = int(input("Enter year : "))
    month = int(input("Enter month : "))
    day = int(input("Enter day (1-31) : "))

    calculator = DateCalculator(year, month, day)
    day_of_week = calculator.calculate_day_of_week()
    print(f"The day of the week is : {day_of_week}")

except ValueError:
    print("Invalid input!!! Please enter numbers only .")
