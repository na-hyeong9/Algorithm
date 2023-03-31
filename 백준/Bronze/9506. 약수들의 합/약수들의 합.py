while True:
    lst=[]
    n=int(input())
    if n == -1:
        break
        
        
    for i in range(1,n):
        if n%i==0:
            lst.append(i)
            
    if sum(lst) != n:
        print('{} is NOT perfect.'.format(n),end='')
    else:
        print(n,"= ",end='')
        
        for j in lst:
            if j == max(lst):
                print('{}'.format(j),end='')
            else:   
                print('{} +'.format(j),end=' ')
    print()