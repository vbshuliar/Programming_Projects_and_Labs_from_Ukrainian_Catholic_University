import math

def sales_prediction():
    sales = float(input())
    print(sales * 1.19)




def yard_to_meter():
    y = float(input())
    print(y*914)
    print(y*0.914)
    print(y*0.000914)




def cashier():
    a = float(input())
    b = float(input())
    c = float(input())
    d = float(input())
    e = float(input())
    print(a+b+c+d+e)
    print((a+b+c+d+e)*0.14)
    print((a+b+c+d+e)-(a+b+c+d+e)*0.14)




def odometer():
    v = float(input())
    a = float(input())
    t1 = float(input())
    t2 = float(input())
    print(v*t+((a*t**2)/2))  




def payment_instalments():
    price = float(input())
    term = float(input())
    print(price*1.05)
    print(price*1.05/term)




def miles_per_galon():
    distance = float(input())
    fuel = float(input())
    print(distance/fuel)




def cookie():
    sugar = 1.5/48
    butter = 1/48
    flour = 2.75/48
    cookies = int(input())
    print(cookies*sugar)
    print(cookies*butter)
    print(cookies*flour)




def vineyard():
    r = float(input())
    e = float(input())
    s = float(input())
    print(int((r - 2*e)/s))




def compound_interest():
    p = float(input())
    r = float(input())
    n = float(input())
    t = float(input())
    print(p*(1+r/100/n)**(n*t))




if __name__ == "__main__":
    eval(input() + "()")
