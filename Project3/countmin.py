import random

k = int(input("Number of counter arrays(k):\n"))
w = int(input("Number of couclsnter in each array(w):\n"))

# print("The value of k and w are:",k, w)
sourceFile = open('countminoutput.txt', 'w')
# Reading the number of flows from the 'project3input.txt'
file = open('project3input.txt', 'r')
Lines = file.readlines()
n = Lines[0]
file.close()
# print("The number of flows are(n):",n)

# build k counter arrays
counter_arr = {}
for i in range(k):
    counter_arr["c" + str(i)] = [0] * w

# Generating random number arrays to facilitate multi-hashing
randomnums = random.sample(range(1, w), k)


# read the flows sequentially and record all the flows by hashing it to all k counters
def record():
    file = open('project3input.txt', 'r')
    Lines = file.readlines()
    for flows in Lines[1:]:
        flows_div = flows.split()
        flowid = flows_div[0]
        count = flows_div[1]
        j = 0
        for key, value in counter_arr.items():
            h = (hash(flowid) ^ randomnums[j]) % w
            counter_arr[key][h] = counter_arr[key][h] + int(count)
            j += 1
    file.close()


record()


# iterating over all counter value hashed to k counter arrays
# and storing the minimum in estimated_flow_size array
def query(estimated_flow_size):
    file = open('project3input.txt', 'r')
    Lines = file.readlines()
    i = 0
    for flows in Lines[1:]:
        flows_div = flows.split()
        flowid = flows_div[0]
        count = flows_div[1]
        small = 2147483647
        j = 0
        for key, value in counter_arr.items():
            h = (hash(flowid) ^ randomnums[j]) % w
            new_small = counter_arr[key][h]
            if new_small <= small:
                estimated_flow_size[i] = new_small
                small = new_small
            j += 1
        i += 1
    file.close()
    return estimated_flow_size


estimated_flow_size = query([0] * int(n))


# calculating the absolute error between estimated flow size
# and true flow size and printing the average error of all flows
def estimate_error(estimated_flow_size, stat):
    error = 0
    file = open('project3input.txt', 'r')
    Lines = file.readlines()
    i = 0
    for flows in Lines[1:]:
        flows_div = flows.split()
        flowid = flows_div[0]
        count = flows_div[1]
        #         print(f"The true flow size is {count} and estimated flow size is {estimated_flow_size[i]} for id: {flowid}")
        error += abs(estimated_flow_size[i] - int(count))
        stat.append([flowid, estimated_flow_size[i], int(count)])
        i += 1
    file.close()
    print("The average error is: ", error / int(n),file = sourceFile)
    stat.sort(key=lambda x: x[1], reverse=True)
    return stat


stat = estimate_error(estimated_flow_size, [])
for val in stat[:100]:
    print(f"Flow Id: {val[0]} Estimated Size: {val[1]} True Size: {val[2]}",file = sourceFile)

sourceFile.close()