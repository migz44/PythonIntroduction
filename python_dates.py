# python_dates
from datetime import date, timedelta

today = date.today()
print(today)

f_day = today.strftime("%a %B-%Y")
print(f_day)


date_after_65_days = today + timedelta(days=65)
print(date_after_65_days)


# 2025-01-15 1995-09-06
diff = date(2025, 1, 15) - date(1995, 9, 6)
print(diff.days)
