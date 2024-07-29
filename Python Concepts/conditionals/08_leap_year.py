# Check whether a given year is leap year or not
# Leap Year: a year divisible by 4 but not by 100 until also divisible by 400
# https://www.kumon.com/resources/wp-content/uploads/2020/02/LeapYearMath-1.png


year = int(input("Enter a year like 2022: "))
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

print("Leap" if is_leap(year) else "Non Leap")