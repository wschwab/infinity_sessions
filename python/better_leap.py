#!/usr/bin/python3m

import sys

year = int(sys.argv[1])

def leap_checker(_year):
	if _year % 100 == 0 and _year % 400 != 0 or _year % 4 == 0:
	    print("LEAP YEAR BRO!!!!")
	else:
	    print("Not a leap year, bro.")

leap_checker(year)
