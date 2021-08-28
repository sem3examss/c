total_mem = int(input("Total memory: "))
b_size = int(input("Block size: ")) 
np = int(input("No.of processes: "))
mem_req = list(map(int, input("Mem reqs: ").split()))
b_avail = int(input("blocks available: "))
int_frag = 0
ext_frag = total_mem-b_size*b_avail

for i in range(np):

    if mem_req[i]<b_size:
        print(i, "\t", mem_req[i], '\tyes\t', b_size-mem_req[i])
        int_frag += b_size-mem_req[i]
        b_avail-=1
    else:
        print(i, "\t", mem_req[i], '\tno\t-----')

    
    if b_avail==0:
        break

print("Internal frag: ", int_frag)
print("External frag: ", ext_frag)