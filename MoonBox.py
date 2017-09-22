machines = []
matches = []
dict = {}

#f = open('Moon-Box_InputForSubmission_1.txt', 'r')
f = open('Moon-Box_InputForSubmission_2.txt', 'r')

for i in range(0, 5):
    machines.append(f.readline())

for i in range(0, 5):
    match = 1
    for j in range(0, 5):
        if machines[i] == machines[j]:
            match += 1
    matches.append(match)

# for i in range(0, 5):
#     if matches[i] in dict:
#         dict[matches[i]] += 1
#     else:
#         dict[matches[i]] = 1
#
orig = []
for i in range(0, 5):
    orig.append(matches[i])

matches.sort()

numCorrect = matches[4]
for i in range(0, 5):
    if orig[i] == numCorrect:
        correctMsg = machines[i]

print(correctMsg)
print(numCorrect)