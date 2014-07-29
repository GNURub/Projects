#!/usr/bin/python
import math
PI = (4 * (44 * math.atan(1.0/57.0) + 7 * math.atan(1.0/239.0) - 12* math.atan(1.0/682.0) + 24 * math.atan(1.0/12943.0)))

def ask():
    decimales = raw_input("Number of decimal : ")
    return decimales

def main():
    num_dec = ask()
    while (num_dec == None):
        num_dec = ask()
    else:
        print "%.*f" % (int(num_dec), PI)
        
if __name__ == "__main__":
    main()
