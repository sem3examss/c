total_mem = int(input("Total memory: "))
p_size = int(input("Page size: "))
total_pages = int(input("No. of pages available: ")) 
np = int(input("No. of processes: "))
# sum1 = 0
npages = 0
l = []

for i in range(np):
    print("No. of pages for P ", i+1, ": ")
    npages += int(input())

    if npages>total_pages:
        print("Mem full")
        break

    l +=[list(map(int, input("Pages enter chey: ").split()))]


print("Enter logical address to find phy address")
pro_no = int(input("process no: "))
p_no = int(input("page no: "))
offset = int(input("process no: "))


print("physical address: ", p_no*p_size+offset)
