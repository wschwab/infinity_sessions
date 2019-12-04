import sys

year = int(sys.argv[1])

if year % 4 == 0:
    if year % 100 != 0:
        print("LEAP YEAR BRO!!!")
    else:
        if year % 400 == 0:
            print("LEAP YEAR BRO!!!")
        else:
            print("Not a leap year, bro.")
else:
    print("Not a leap year, bro.")
