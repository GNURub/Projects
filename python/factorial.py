#!/usr/bin/python
def ask():
    return int(raw_input("Give me a number: "))

def main():
    num = ask()
    result = 1
    for k in range(1, num +1):
        result *= k
    print k

if __name__ == "__main__":
    main()
