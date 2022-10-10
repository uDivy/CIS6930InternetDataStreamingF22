import math
import random

n = int(input("Number of elements to be encodes(n):\n"))
m = int(input("Number of bits in the filter(m):\n"))
k = int(input("Number of hashes(k):\n"))

print("The value of n, m and k are:",n, m, k)

# Hash Function:: Generates index number randomly based on flowid between 0 and m
def multiplication_hash(m, flowid, A=0.314):
    h = math.floor(m*((flowid*A)%1))
    return h

# Function to generate the list of size 'n' of unique flowid's in the range of [start and end]
def gen_flows(start,end, set_size):
    flows = random.sample(range(start, end), set_size)
    return flows

# A and B are two sets of randomly generated elements of size n
A = gen_flows(1,m,n)
B = gen_flows(100*m,1000*m,n)

# This is to generate d random numbers to generate multiple hash function using XOR
randomnums = random.sample(range(1, m), k)
bit_map = [0]*m

# Function will encode all the elements of the array into the bit_map
def encode(array):
    for ele in array:
        for i in range(k):
            h = multiplication_hash(m, ele ^ randomnums[i])
            bit_map[h] = 1

# Function will help to search for all the elements whose bit corresponding to its ALL hashed locations are 1
def lookup(array):
    count = 0
    for ele in array:
        found = True
        for i in range(k):
            h = multiplication_hash(m, ele ^ randomnums[i])
            if bit_map[h] != 1:
                found = False
                break
        if found:
            count += 1
    return count

encode(A)
print("The number of elements found from Set A: ",lookup(A))
print("The number of elements found from Set B: ",lookup(B))