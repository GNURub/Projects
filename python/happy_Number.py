#!/usr/bin/python

def ask():
    return int(raw_input("Introduce un numero: "))

def main():
    num = ask()
    sub = 0
    while num != 1:
        for k in str(num):
            sub += int(k) ** 2
        num = sub
        sub = 0
    print "It is a happy number"
        
        

if __name__ == "__main__":
    main()
