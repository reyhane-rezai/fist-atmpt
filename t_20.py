def dif (x):
    total=1
    for i in range(1,x+1):
        total=i*total
    print(total)

x=int(input())
dif(x)