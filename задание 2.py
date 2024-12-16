def check_date(year, month, day):
    days_in_month = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    if not all(isinstance(i, int) and i > 0 for i in [year, month, day]):
        return False
    if month not in days_in_month:
        return False

    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        days_in_month[2] = 29

    if day > days_in_month[month] or day <= 0:
        return False
    return True

print(check_date(day=22, month=10, year=2000))
