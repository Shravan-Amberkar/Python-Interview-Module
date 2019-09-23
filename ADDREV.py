for tc in range(int(input())):
    x=input().split() 
    y=int(x[0][::-1]) + int(x[1][::-1])
    y=str(y)
    y=y.rstrip('0') #strips trailing zeros
    print(y[::-1])
