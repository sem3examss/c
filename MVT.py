total_mem = int(input("Total memory: "))
mem_req = list(map(int, input("Mem reqs: ").split()))
sum = 0

for i in range(len(mem_req)):
    sum+=mem_req[i]

    if sum>total_mem:
        sum-=mem_req[i]
        print(i, "\tCan`t fit")
    
    else:
        print(i,"\t", mem_req[i])
    
    if sum>=total_mem:
        print("mem aipoindi")
        break

print("total use: ", sum)
print("External frag: ", total_mem-sum) 