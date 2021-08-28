n=int(input("Enter Buffer Size"))
mutex=1  # Mutex can be either 1 or 0   0 indicates buffer can't be changed
full=0  #indicates filled spaces are initially zero
empty=n  #indicates all spaces are initially empty
item=0   # iem no 0

def wait(s):   #common variable for both consumer and producer "s"
    return s-1 
    
def signal(s):
    return s+1


def producer(): 
    global mutex,full,empty,item 
    empty=wait(empty) #decrement empty spaces to reserve one of them to keep new item
    mutex=wait(mutex) # decrement mutex indicating buffer is being used 
    item+=1  
    print("item no {} produced".format(item))
    mutex=signal(mutex) #now you can use buffer
    full=signal(full)  #increment filled spaces as we have produced an item


def consumer():
    global mutex,full,empty,item 
    full=wait(full) #decrement full indicating the item is being consumed
    mutex=wait(mutex) # decrement mutex indicating buffer is being used 
    print("item no {} consumed".format(item))
    item-=1  
    mutex=signal(mutex)  #now you can use buffer 
    empty=signal(empty)  #1 empty space created after consumption


while(1):
    print("1) produce item 2)consume item ")
    ch=int(input("Enter choice")) 
    if(ch==1):
        if(empty!=0 and mutex==1): #if empty spaces exists and mutex==1 produce item
            producer() 
        else:
            print("Buffer overflow occurred") 
    elif(ch==2):
        if(full!=0 and mutex==1): #if filled spaces exists and mutex==1 consume item
            consumer() 
        else:
            print("Buffer underflow occured") 
    else:
        break  