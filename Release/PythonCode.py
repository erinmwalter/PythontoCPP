import re
import string


def printsomething():
    print("Hello from python!")

def PrintMe(v):
    print("You sent me: " + v)
    return 100;

def SquareValue(v):
    return v * v

#function to calculate and print out multiplication table from 1-10 given 
#user input value v
def MultiplicationTable(v):
    for n in range(1,11): 
        {
            print(v, " X ", n, " = ", (v * n))
        }
    return 0

#function to double input value v
def DoubleValue(v):
    return 2 * v

    
