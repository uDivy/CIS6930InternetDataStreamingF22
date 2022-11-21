import math
import random

NumOfFlows = 5
outFile = open('Bitmap.txt', 'w')

m = int(input("Number of bits in the filter(m):\n"))
print("The value of m is:", m)


def encode(array, tf):
    i = 0
    for i in range(tf):
        rnd_num = random.randrange(0, 2 ** 32)
        h = hash(rnd_num) % m
        array[h] = 1
    return array


def lookup(array):
    u = 1
    u = array.count(0)
    if u == 0:
        u = 1
    v = u / m
    return -1 * m * math.log(v)


for i in range(NumOfFlows):
    tf = int(input("ENTER the flow spread:\n"))
    #     print("The value of tf are:",tf)
    bit_map = [0] * m
    bit_map = encode(bit_map, tf)
    print(f"The True flow spread is {tf} and expected flow spread is {lookup(bit_map)}", file=outFile)

outFile.close()