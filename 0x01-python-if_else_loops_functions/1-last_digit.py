#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastDigit = number % 10
if lastDigit != 0 && lastDigit < 6:
	print(f"Last digit of {number} is {lastDigit} and less than 6 and not 0")
elif lastDigit == 0:
	print(f"Last digit of {number} is {lastDigit} and is 0")
elif lastDigit > 5:
	print(f"Last digit {number} is {lastDigit} and is greater than 5")
