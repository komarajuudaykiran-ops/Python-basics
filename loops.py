
n=6
for i in range(1,n+1):
    for j in range(i-1):
        print(" ",end="")
    for k in range(1,n-i+2):
        print("*",end="")
    print()