limit=20
ch=1
already_alloc=list(map(int,input("give already allocated indices").split()))  
while(ch):
    start=int(input())
    length=int(input())
    i=start 
    while(length>0 and i<=limit):
        if(i not in already_alloc): 
            already_alloc.append(i) 
            print("index {}".format(i))
            length-=1
        i+=1
    if(len(already_alloc)>=20):
        print("anni kalilu aiepoyay")
        break
    ch=int(input("continue...? yes==1 no==0"))
    ch=int(input())