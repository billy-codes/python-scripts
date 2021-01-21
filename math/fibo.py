# A simple script that outputs Fibonacci sequence 

import argparse

parser = argparse.ArgumentParser(
	description="Generate Fibonacci Sequence with given number of terms",
	usage = "fibo.py -t 5",
	epilog = "Author: Billy Khaled, billy.codes@gmail.com")

parser.add_argument("-t", "--terms", metavar='', required=True, help="Enter number of terms")
args, unknown = parser.parse_known_args()

fibo_out = []
def fibo(terms):
	first = 0
	second = 1
	fibo_out.append(first)
	fibo_out.append(second)
	for _ in range(0, terms):
		# the underscore is declared as "discarded" identifier/variable
		total = first + second
		fibo_out.append(total)
		first = second
		second = total
	print(''.join(x for x in str(fibo_out)))

fibo(int(args.terms))