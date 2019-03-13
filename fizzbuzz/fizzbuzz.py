#!/usr/bin/env python3
""" 
Fizzbuzz module 
 
 
 Kim Brugger (13 Mar 2019), contact: kim@brugger.dk
"""

import sys
import pprint
pp = pprint.PrettyPrinter(indent=4)

def fizzbuzz( lower:int=0, upper:int=10):
    '''implementation of fizzbuzz code:
 
      A program that prints the numbers from lower to upper. For
      multiples of three print “Fizz” instead of the number and for
      the multiples of five print “Buzz”. For numbers which are
      multiples of both three and five print “FizzBuzz”.

    '''

    for i in range( lower, upper + 1):
        if ( i % 3 == 0 and i % 5 == 0):
            print( "FizzBuzz" )
        elif ( i % 3 == 0):
            print( "Fizz" )
        elif ( i % 5 == 0):
            print( "Buzz" )
        else:
            print( i )



#fizzbuzz(1,15)
