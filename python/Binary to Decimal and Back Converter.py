#!/usr/bin/python
import sys
binary = []

def ask():
    try:
        type_conv = sys.argv[1]
        num = int(sys.argv[2])
    except:
        type_conv = raw_input("Enter a type to convert [dec/bin]: ")
        num = int(raw_input("Enter a number: "))
    return type_conv, num

def main():
    type_conv, num = ask()
    if type_conv == 'bin':
        while True:
            res = num % 2
            binary.append(str(res))
            if num == 1:
                binary.reverse()
                print ''.join(binary)
                break
            else:
                num = num // 2
    elif type_conv == 'dec':
        num = str(num)[::-1]
        result = 0
        for k in range(len(num)):
            if int(num[k]) == 1:
                result += 2**int(k)
            elif int(num[k]) != 0:
                print "it is not a binary"
                return None
        print result

if __name__ == "__main__":
    main()
