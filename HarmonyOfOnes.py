import math

f = open('Harmony-of-Ones_InputForSubmission_1.txt', 'r')
n = f.readline()
#print(n)
input = f.read().splitlines()

for i in range(0, int(n)):
    numSame = 0
    numbers = input[i].split(',')
    a = int(numbers[0])
    b = int(numbers[1])
    binaryA = bin(a)
    binaryB = bin(b)
    #print(binaryA, binaryB)
    lenA = int(math.log(a, 2) + 1) + 1
    lenB = int(math.log(b, 2) + 1) + 1
    #print(lenA, lenB)
    minLen = min(lenA, lenB)
    j = 0

    while j < minLen:
        if binaryA[lenA - j] == '1' and binaryB[lenB - j] == '1':
            numSame+=1
        j+=1
    print(numSame)


f.close()