import math
import random

g = int(input("Number of sets(g):\n"))
n = int(input("Number of elements in each set(n):\n"))
f = int(input("Number of filters(f):\n"))
b = int(input("Number of bits in each filter(b):\n"))
k = int(input("Number of hashes(k):\n"))

# Hash Function:: Generates index number randomly based on flowid between 0 and m
def multiplication_hash(m, flowid, A=0.314):
    h = math.floor(m*((flowid*A)%1))
    return h

# Function to generate the list of size 'n' of unique flowid's in the range of [start and end]
def gen_flows(start, end, set_size):
    flows = random.sample(range(start, end), set_size)
    return flows

# g_set is the dictionary whose keys are of type "001", binary value corresponding to its location
# in the dictionary, and its values are list of n unique values for given range [start, end]
start = 1
end = n
base = str(int(math.ceil(math.log2(g + 1))))
keys = [format((i + 1), "0" + base + "b") for i in range(g)]
g_set = {}
for i in range(g):
    g_set[keys[i]] = gen_flows(start, end+1, n)
    start = 1000*end + 1
    end = 1000*end + n

# b_set is the dictionary whose keye are in the range [1, f]
# and its values is the list of 0's of given bit size eg. 30000
ids = [i for i in range(1, f + 1)]
b_set = {}
for i in range(f):
    b_set[ids[i]] = [0] * b

# This is to generate d random numbers to generate multiple hash function using XOR
randomnums = random.sample(range(1, n), k)

# Function will endode all the list element of g_set to b_set considering the key  value of g_set
# for eg. for the key value of "011", the elements will be encoded in the list available at location
# b_set["2"] and b_set["3"]
def encode_codbf(g_set, b_set):
    for key, value in g_set.items():
        for flowid in value:
            for index,bit in enumerate(key):
                if bit == "1":
                    for i in range(k):
                        h = multiplication_hash(b, flowid ^ randomnums[i])
                        b_set[index+1][h] = 1
encode_codbf(g_set, b_set)

# Function will help to search for all the elements whose bit
# corresponding to its ALL hashed locations are 1
def lookup_codbf(array, flowid):
    found = True
    for i in range(k):
        h = multiplication_hash(b, flowid ^ randomnums[i])
        if array[h] != 1:
            found = False
            break
    return found

# This will generate a passcode i.e it will turn the bit to 1, if it found the element
# in corresponding bit_map, once the passcode is generated, it will look for the element in the
# corresponding list whose key value in g_set resembles passcode.
count = 0
for key, value in g_set.items():
        for flowid in value:
            passcode = ['0']*int(base)
            for index,_ in enumerate(key):
                if lookup_codbf(b_set[index+1], flowid):
                    passcode[index] = '1'
            loc = str(''.join(passcode))
            if loc in g_set.keys() and flowid in g_set[loc]:
                count += 1

print("The number of elements found from all set are: ",count)