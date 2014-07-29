#!/usr/bin/python
def ask():
    cost = float(raw_input("Cost por m^2: "))
    width = float(raw_input("meters of the width: "))
    height = float(raw_input("meters of the height: "))
    return cost, width, height


def main():
    a,b,c = ask()
    print "The cost is: %.2f $" % (float(a * b * c))

if __name__ == "__main__":
    main()
