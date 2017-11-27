from math import*
def main():
    x = eval(input("Please input a number x less than 15: "))

    if (x >= 15):
        quit()
    else:
        
        A = 1 + x + (x**2/2) + (x**3/6)
    print("e^x = ",A)

    y = radians(x)

    B = 1 + (((-1)*(y**2))/2) + ((y**4)/24) + (((-1)*(y**6))/720)
    print("cosine(x) = ",B)


main()
