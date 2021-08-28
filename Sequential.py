arr=[0]*20
ch=1
while(ch):
    start_index=int(input())
    length=int(input())
    
    if 1 not in arr[start_index:start_index+length+1]:
        arr[start_index:start_index+length+1] = [1]*length
        print("Inserted")
    
    else:
        print("nope")

    print("Continue...? if yes==1 no==0")
    ch = int(input())