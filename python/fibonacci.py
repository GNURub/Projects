#!/usr/bin/python
import sys
def ask():
    try:
        return int(raw_input("f(x): "))
    except:
        main()
    
def main():
    if len(sys.argv) >= 2 and sys.argv[1].isdigit():
        num_suce = int(sys.argv[1])
    else:
        num_suce = ask()

    a,b = 0,1
    if num_suce == 0:
        print a
    else:
        print "%i\n%i" %(a,b)
        for k in range(num_suce -1):
            c = a + b
            print "%i" % c
            a = b
            b = c

if __name__ == "__main__":
    main()
