n=int(input())
for i in range(n):
    for j in range(n):
        if(i==(n-1)):
            print('*',end='')
        elif(j==0):
            print('*',end='')
        elif(i==j):
            print('*',end='')
        else:
            print(' ',end='')
    print()
