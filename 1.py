def EOReplace(l):
    l=input("enter a list of numbers:")
    print("Original list: ",l)
    for i in range(len(l)):
        if l[i]%2==0:
            l[i]+=1
        else:
            l[i]-=1
    return l            

