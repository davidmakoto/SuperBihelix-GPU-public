#!/home/exec/anaconda3/bin
#!/bin/python2.7

import argparse
# import pycuda

# import pycuda.driver as cuda

# from pycuda import driver, compiler, gpuarray, tools
# import pycuda.autoinit

parser = argparse.ArgumentParser()
parser.add_argument("fact", type=int,
                    help="display a factorial of a given number. Format: <factorial> [options]")
parser.add_argument("-v", "--verbosity", type=int, choices=[0, 1, 2],
                    help="increase output verbosity")
args = parser.parse_args()


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

answer = factorial(args.fact)


if args.verbosity == 2:
    print("the factorial of {} equals {}".format(args.fact, answer))
elif args.verbosity == 1:
    print("{}! = {}".format(args.fact, answer))
else:
    print(answer)



