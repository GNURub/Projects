#!/usr/bin/python

def ask():
    return int(raw_input('Enter a number: '))

def esPrimo(num):
    for k in range(2, num):
        if num % k == 0:
            return False
    return True

def main(num):
    while True:
        num += 1
        if esPrimo(num):
            print "The next prime number is: %i" % num
            break

if __name__ == "__main__":
    main(ask())
