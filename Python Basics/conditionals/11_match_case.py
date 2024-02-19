# Write a python script to implement Match-Case (switch case in other Pro. languages)

day = int(input("Enter any number from 1 to 7 to print Weekday: "))

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Enter valid number")