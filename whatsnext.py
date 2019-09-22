while(1):
    a,b,c=map(int,input().split())
    if a==b==c==0:
        break
    if b-a==c-b:
        print ('AP', int(c+(b-a)))
    else:
        print ('GP', int(c*(b/a)))
