import math
import random

NumOfFlows = 5
outFile = open('Probabilistic_Bitmap.txt', 'w')

m = int(input("Number of bits in the filter(m):\n"))
p = float(input("Sampling Probability(p):\n"))
print("The value of m, p are:", m, p)


def encode(array, tf):
    #     i = 0
    for _ in range(tf):
        rnd_num = random.randrange(0, 2 ** 32)
        random_hash = hash(rnd_num)
        if random_hash < p * (2 ** 32):
            rnd_num_2 = random.randrange(0, 2 ** 32)
            h = hash(rnd_num_2) % m
            array[h] = 1
    return array


def lookup(array):
    u = 1
    u = array.count(0)
    if u == 0:
        u = 1
    v = u / m
    return (-m * math.log(v)) / p


for i in range(NumOfFlows):
    tf = int(input("ENTER the flow spread:\n"))
    #     print("The value of tf are:",tf)
    bit_map = [0] * m
    bit_map = encode(bit_map, tf)
    print(f"The True flow spread is {tf} and expected flow spread is {lookup(bit_map)}", file=outFile)

outFile.close()