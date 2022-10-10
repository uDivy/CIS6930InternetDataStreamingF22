import math
import random

n = int(input("Number of elements to be encoded initially(n):\n"))
r = int(input("Number of elements to be removed(r):\n"))
a = int(input("Number of elements to be added(a):\n"))
m = int(input("Number of counters in the filter(m):\n"))
k = int(input("Number of hashes(k):\n"))

# Hash Function:: Generates index number randomly based on flowid between 0 and m
def multiplication_hash(m, flowid, A=0.314):
    h = math.floor(m*((flowid*A)%1))
    return h

# Function to generate the list of size 'n' of unique flowid's in the range of [start and end]
def gen_flows(start,end, set_size):
    flows = random.sample(range(start, end), set_size)
    return flows

# This is to generate d random numbers to generate multiple hash function using XOR
randomnums = random.sample(range(100, 1000*m), k)
bit_map = [0]*m

# Function will encode all the elements of the array into the bit_map
def encode_cntbf(array):
    for ele in array:
        for i in range(k):
            h = multiplication_hash(m, ele ^ randomnums[i])
            bit_map[h] = bit_map[h] + 1

# Function will delete the r number of array elements from the bit_map
def remove_cntbf(array, r):
    for ele in array[:r]:
        for i in range(k):
            h = multiplication_hash(m, ele ^ randomnums[i])
            bit_map[h] = bit_map[h] - 1

# Function will help to search for all the elements whose bit
# corresponding to its ALL hashed locations are greater than 1
def lookup_cntbf(array):
    count = 0
    for ele in array:
        found = True
        for i in range(k):
            h = multiplication_hash(m, ele ^ randomnums[i])
            if bit_map[h] < 1:
                found = False
                break
        if found:
            count += 1
    return count

A = gen_flows(1,m,n)
encode_cntbf(A)
remove_cntbf(A, r)
B = gen_flows(1000*m,10000*m,a)
encode_cntbf(B)
print("The number of elements found from Set A: ",lookup_cntbf(A))