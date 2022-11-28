import random
NumOfFlows = 4
outFile = open('HyperLogLog.txt', 'w')

m = int(input("Number of registers(m):\n"))

def encode(array, tf):
    for _ in range(tf):
        rnd_num = random.randrange(0, 2**32)
        random_hash = hash(rnd_num)
        thirtytwo_bit_rep = '{:032b}'.format(random_hash)
        g_e = (len(thirtytwo_bit_rep) - len(thirtytwo_bit_rep.lstrip('0')))+1
        h = random_hash%m
        array[h] = max(array[h],g_e)
    return array

def lookup(array):
    data = [1/(2**array[i]) for i in range(m)]
    query = ((0.7213/(1 + (1.079/m)))*(m**2)*(1/sum(data)))
    return query

for i in range(NumOfFlows):
    tf = int(input("ENTER the flow spread:\n"))
#     print("The value of tf are:",tf)
    reg_group = [0]*m
    reg_group = encode(reg_group, tf)
    print(f"The True flow spread is {tf} and expected flow spread is {lookup(reg_group)}",file = outFile)
outFile.close()