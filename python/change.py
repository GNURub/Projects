#!/usr/bin/python
import math

def ask():
    price = float(raw_input('Precio del producto: '))
    money = float(raw_input('Dinero que lleva: '))
    return round(price, 2), round(money,2)

def main():
    price, money = ask()
    if money < price:
        print "you cant buy that!!"
        return
    euros = -(price - money)
    cents = (euros - int(euros)) *100
    print "Change %i euros and %i cents" % (euros, cents)
    
    
if __name__ == "__main__":
    main()
