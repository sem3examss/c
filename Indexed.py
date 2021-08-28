arr=[0]*20
ch=1
l1 = []

while(ch):
    index=int(input())
    
    if index not in l1:
        l1.append(index)
        n=int(input("enni indexes")) 
        l=list(map(int,input().split()))

        if set(l).intersection(set(l1))==set():
            l1+=l
            print('aindi le')
        
        else:
            print("already undi")

    else:
        print("pani avadhu")
    print("continue..?")
    ch = int(input())