import numpy as np
n=int(input("Enter no.of processes"))
m=int(input("Enter no.of resources"))
Allocation=np.array([list(map(int,input("enter allocation matrix row {} ".format(i)).split()))[:m] for i in range(n)])
Max=np.array([list(map(int,input("enter max matrix row {} ".format(i)).split()))[:m] for i in range(n)]) 
Available=np.array(list(map(int,input("Enter available array ").split()))[:m])


need=Max-Allocation 


def compare(i):
    for j in range(m):
        if(need[i][j]>Available[j]):
            return False
    return True

safe_sequence=[]
flag=[0]*n 


for _ in range(n): 
    for i in range(n): 
        if(flag[i]==0 and compare(i)):
            #if(compare(i)):
            safe_sequence.append(i) 
            flag[i]=1
            for j in range(m):
                Available[j]+=Allocation[i][j]  


if(sum(flag)!=n):
    print("System is unsafe") 
else:
    print("System is safe for the safe sequence")
    print(safe_sequence)
    print("Need matrix is \n {}".format(need))


''' 0 0 1 2
    1 0 0 0
    1 3 5 4
    0 6 3 2
    0 0 1 4
    0 0 1 2
    1 7 5 0
    2 3 5 6
    0 6 5 2
    0 6 5 6
    1 5 2 0
'''