# First fit
# p_Size = [212, 417, 112, 426] 

''' n=int(input("Enter no.of processes")) 
p_size=list(map(int,input().split()))[:n]
#B_available=[50,150,300,350,600,200,175] 
B_available=[100, 500, 200, 300, 600]
allotement=[0]*n
b=len(B_available)
for i in range(n):
    c=0
    for j in range(b):
        if(p_size[i]<=B_available[j]):
            c+=1
            B_available[j]-=p_size[i] 
            allotement[i]=j+1
            break 
    if(c==0):
        allotement[i]="Space not sufficient"

print("process no  process_size  allocated_index")
for i in range(n):
    print("     {}         {}            {}".format(i+1,p_size[i],allotement[i]))
print("available memory after allocation int fragmentation ",B_available) '''


#Best fit
''' n=int(input("Enter no.of processes")) 
p_size=list(map(int,input().split()))[:n]
#B_available=[50,150,300,350,600,200,175] 
B_available=[10,15,5,9,3]
allotement=[0]*n 
b=len(B_available)
for i in range(n):
    c=0
    min=9999
    for j in range(b):
        check = B_available[j]-p_size[i]
        if(p_size[i]<=B_available[j] and min>check and check>0):
            c+=1
            min=B_available[j]-p_size[i] 
            index=j 
    if(c==0):
        allotement[i]="Space not sufficient"
    else:  
        allotement[i]=index+1
        B_available[index]-=p_size[i] 
print("process no  process_size  allocated_index")
for i in range(n):
    print("     {}         {}            {}".format(i+1,p_size[i],allotement[i]))
print("available memory after allocation ",B_available) '''
#worst fit
n=int(input("Enter no.of processes")) 
p_size=list(map(int,input().split()))[:n]
#B_available=[50,150,300,350,600,200,175] 
B_available=[100, 500, 200, 300, 600] 
B_available=[5,8,4,10]
allotement=[0]*n 
b=len(B_available)
for i in range(n):
    c=0
    max=-1
    for j in range(b):
        if(p_size[i]<=B_available[j] and max<(B_available[j]-p_size[i])):
            c+=1
            max=B_available[j]-p_size[i] 
            index=j 
    if(c==0):
        allotement[i]="Space not sufficient"
    else:  
        allotement[i]=index+1
        B_available[index]-=p_size[i] 
print("process no  process_size  allocated_index") 
for i in range(n):
    print("     {}         {}            {}".format(i+1,p_size[i],allotement[i]))
print("available memory after allocation ",B_available) 