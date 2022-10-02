import numpy as np
import math

n = int(input("Number of table entries(n):\n"))
m = int(input("Number of flows(m):\n"))
k = int(input("Number of hashes(k):\n"))

print("The value of n, m and k are:",n, m, k)

# Hash Function:: Generates index number randomly based on flowid between 0 and n
def multiplication_hash(n, flowid, A=0.314):
    h = math.floor(n*((flowid*A)%1))
    return h

# Function to generate the list of size 'm' of random flowid's in the range of [0 and m]
def gen_flows(m):
    flows = np.random.randint(1, m+1, m)
    return flows

# This is to generate d random numbers to generate multiple hash function using XOR
randomnums = np.random.randint(1, m + 1, k)
hash_table = [(0, 0)] * n
flows = gen_flows(m)

"""
Function will check if the given flowid is present in the hash table, and in case if it is available it
will increase the counter by 1 otherwise call the insert() function.
"""
def receive(flowid):
    for i in range(k):
        h = multiplication_hash(n, flowid ^ randomnums[i])
        address = hash_table[h]
        if address[0] == flowid:
            hash_table[h] = (flowid, address[1] + 1)
            return True
    return insert(flowid)

"""
This will insert the new flowid into the hash table, and ignore the flow if the hash collision occurred.
"""
def insert(flowid):
    for i in range(k):
        h = multiplication_hash(n, flowid ^ randomnums[i])
        if hash_table[h][0] == 0:
            hash_table[h] = (flowid, 1)
            return True

    return False

for flowid in flows:
    receive(flowid)

print("The flowid of all the unique entries are: ",len([add[0] for add in hash_table if add[0] != 0]))
print("The flowid of all the unique entries are: ",[add[0] for add in hash_table])