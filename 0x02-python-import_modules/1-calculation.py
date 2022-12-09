#!/usr/bin/python3
# 1_calculator
# brook

if __name__ == "__main__":
	"""print the sum div mult and submissio"""
	from calculator_1 import add, sub, mul, div

	a = 10
	b = 5

	print("{} + {} = {}".format(a, b, add(a,b)))
	print("{} - {} = {}".format(a, b, sub(a,b)))
	print("{} * {} = {}".format(a, b, mul(a,b)))
	print("{} / {} = {}".format(a, b, div(a,b)))
