## bSkt(HLL)
import numpy as np
import random

outFile = open('bSkt_Hll.txt', 'w')

m = int(input("total number of HLL estimators(m):\n"))
l = int(input("number of five-bit registers in each estimator(l):\n"))
k = int(input("number of estimators each flow is hashed to(k):\n"))

# Reading the number of flows from the 'project3input.txt'
file = open('project5input.txt', 'r')
Lines = file.readlines()
n = Lines[0]
file.close()

A = [[0 for i in range(l)] for j in range(m)]
randomnums = random.sample(range(1, m), k)

flow_id = []
def record():
    file = open('project5input.txt', 'r')
    Lines = file.readlines()
    for flows in Lines[1:]:
        flows_div = flows.split()
        flowid = flows_div[0]
        flowspread = int(flows_div[1])
        flow_id.append(flowid)
        for _ in range(flowspread):
            rnd_num = random.randrange(0, 2**32)
            random_hash = hash(rnd_num)
            thirtytwo_bit_rep = '{:032b}'.format(random_hash)
            g_e = (len(thirtytwo_bit_rep) - len(thirtytwo_bit_rep.lstrip('0')))+1
            h2 = random_hash%l
            for i in range(k):
                h1 = hash(hash(flowid) ^ randomnums[i])%m
                A[h1][h2] = max(A[h1][h2],g_e)
    file.close()
    return A

A = record()

def lookup(array):
    data = [1/(2**array[i]) for i in range(l)]
    query = ((0.7213/(1 + (1.079/l)))*(l**2)*(1/sum(data)))
    return query
output = []
for t_f in flow_id:
    estimated_flows = []
    for i in range(k):
        h1 = hash(hash(t_f) ^ randomnums[i])%m
        estimated_flows.append(lookup(A[h1]))
    output.append(min(estimated_flows))
arr = np.array(output)
sorted_index_array = np.argsort(arr)
rslt = sorted_index_array[::-1][:25]

for ind in rslt:
    print(f"Flow ID: {flow_id[ind]} and Estimated Flow Spread: {output[ind]}",file = outFile)
outFile.close()