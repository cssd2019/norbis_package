#!/usr/bin/env python3
""" 
Fizzbuzz module 
 
 
 Kim Brugger (13 Mar 2019), contact: kim@brugger.dk
"""

import sys
import pprint
pp = pprint.PrettyPrinter(indent=4)
import argparse
import fizzbuzz as fb



def main():

    parser = argparse.ArgumentParser(description='fizzbuzz: for that fizz and buzz ')

    parser.add_argument('-l', '--lower', default=1, help="Lower value to start from")
    parser.add_argument('-u', '--upper', default=15, help="Lower value to start from")

    args = parser.parse_args()
    lower = args.lower
    upper = args.upper
    
    
    fb.fizzbuzz(lower, upper)


if __name__ == '__main__':
    main()
