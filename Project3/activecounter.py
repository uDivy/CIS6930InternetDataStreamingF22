import random

sourceFile = open('activecounteroutput.txt','w')

number = '{0:016b}'.format(0)
exponent = '{0:016b}'.format(0)
overflow = '{0:017b}'.format(65536)

# Iterating over 1000000 times, and using active counter algorithm
# to generate number using 16 bit number and 16 bit exponent binary number.
for i in range(1000000):
    let = random.uniform(0, 1)
    if let < (1/2**(int(exponent, 2))):
        number = '{0:016b}'.format(int(number,2)+1)
    if int(number, 2) == 65536:
        right_sh = int(number, 2) >> 1
        number = '{0:016b}'.format(right_sh)
        exponent = '{0:016b}'.format(int(exponent,2)+1)
print(int(number,2)*(2**int(exponent,2)),file=sourceFile)
sourceFile.close()