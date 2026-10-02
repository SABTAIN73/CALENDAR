import calendar
try:
    year = int(input("Enter year:"))
except ValueError:
    print("ENTER VALID YEAR")
    exit()
try:
    month = int(input("Enter month:"))
except ValueError:    
    print("PLEASE ENTER A VALID MONTH")
    exit()

if month <1 or month > 12:
    print("ENTER VALID MONTH")
    exit()
else:
    print (calendar.month(year, month))
