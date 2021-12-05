def is_leap(years):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return False
    else:
        return False


def days_in_month(years, months):
    """
    Big Butts like I
    :param years: int 4 digit
    :param months: int 1 -2 digits
    :return: returns the value of the month in days
    """
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(years):
        month_days[1] = 31
    days_i_m = month_days[months -1]
    return days_i_m


# 🚨 Do NOT change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))


days = days_in_month(year, month)
print(days)
