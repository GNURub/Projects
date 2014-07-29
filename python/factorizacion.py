#!/usr/bin/python

factors = []

def ask():
    return int(raw_input('Enter a number: '))

def is_prime(num):
    for k in range(2, num):
        if num % k == 0:
            return False
    return True

def main(num_fact):
    for k in range(2, num_fact + 1):
        if is_prime(k) and num_fact % k == 0:
            factors.append(k)
            return main(num_fact / k)
    return "Factors: "+str(factors)
            
        

if __name__ == "__main__":
    print main(ask())
