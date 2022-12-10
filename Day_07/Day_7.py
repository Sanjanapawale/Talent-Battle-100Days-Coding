from re import match
month, year = map(int, (input("Enter Month and Year: ")).split())
def check_days(month):
    match month:
        case 1:
            print("January has 31 days")
        case 2:
            if year % 4 == 0:
                print("February has 29 days")
            else:
                print("February has 28 days")
        case 3:
            print("March has 31 days")
        case 4:
            print("April has 30 days")
        case 5:
            print("May has 31 days")
        case 6:
            print("June has 30 days")
        case 7:
            print("July has 31 days")
        case 8:
            print("August has 31 days")
        case 9:
            print("September has 30 days")
        case 10:
            print("October has 31 days")
        case 11:
            print("November has 30 days")
        case 12:
            print("December has 31 days")
        case default:
            print("Invalid input. \n Enter the value between 1 to 12.")

check_days(month)
