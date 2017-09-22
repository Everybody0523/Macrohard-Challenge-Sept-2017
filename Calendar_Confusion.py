def findDelimitor(inputString):
    for c in inputString:
        if not( c.isdigit() or c.isalpha()):
            return c

    return ""


def findThingy(time, arrayDate, arrayFormat):
    for i in range(0, 3):
        if time == arrayFormat[i]:
            return arrayDate[i]
    return ""


def convert(inputString):
    L = inputString.split()
    delimitorOrg = findDelimitor(L[0])
    delimitorDes = findDelimitor(L[2])

    # year goes first, then month, then day

    arrayActual = L[1].split(delimitorOrg) #Actual format


    arrayDesired = L[2].split(delimitorDes)  # Desired format


    actualDate = L[0].split(delimitorOrg)

    final = ["", "", ""]

    output = ""
    for i in arrayDesired:
        output += findThingy(i, actualDate, arrayActual)
        output += delimitorDes



    l = output.__len__()
    return output[0:l-1]







if __name__ == "__main__":

    f = open("output.txt", "w")
    with open("Calendar-confusion_InputForSubmission_2.txt") as f:
        for line in f:
            print((convert(line)))

