import random
import numpy as np
import matplotlib.pyplot as plt

m = int(input("Number of bits in the physical array(m):\n"))
l = int(input("Number of bits in the virtual bitmap for each flow(l):\n"))

# Reading the number of flows from the 'project3input.txt'
file = open('project5input.txt', 'r')
Lines = file.readlines()
n = Lines[0]
file.close()

bit_map = [0]*m
R = random.sample(range(0, (2**32)-1), l)

element_matrix = []
true_flow = []
def record():
    file = open('project5input.txt', 'r')
    Lines = file.readlines()
    for flows in Lines[1:]:
        flows_div = flows.split()
        flowid = flows_div[0]
        flowspread = int(flows_div[1])
        element_row = [0]*flowspread
        true_flow.append(flowspread)
        i = 0
        for element in range(flowspread):
            rnd_num = random.randrange(0, 2**32)
            r = hash(rnd_num)%l
            element_row[i] = r
            h = hash(hash(flowid)^R[r])%m
            bit_map[h] = 1
            i += 1
        element_matrix.append(element_row)
    file.close()
record()
count_zero_in_bitmap = bit_map.count(0)

count_zero_in_bitmap = bit_map.count(0)
Vb = count_zero_in_bitmap/m
estimated_flow = []
def query():
    file = open('project5input.txt', 'r')
    Lines = file.readlines()
    for flows in Lines[1:]:
        flows_div = flows.split()
        flowid = flows_div[0]
        count_zero_in_virtual = 0
        for i in R:
            h = hash(hash(flowid)^i)%m
            if bit_map[h] == 0:
                count_zero_in_virtual += 1
        if count_zero_in_virtual == 0:
            count_zero_in_virtual = 1
        Vf = count_zero_in_virtual/l
        estimated_flow.append(l*np.log(Vb)-l*np.log(Vf))
query()
plt.xlim(0,500)
plt.ylim(0,700)
plt.xlabel("actual spread")
plt.ylabel("estimated spread")
plt.plot(true_flow, estimated_flow, 'b+')
x = np.arange(0,l)
y = np.arange(0,l)
plt.plot(x,y, 'r-', )
plt.savefig("virtualBitmap.pdf", format="pdf", bbox_inches="tight")
plt.show()