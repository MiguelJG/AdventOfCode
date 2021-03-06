def IDsCheckSum(changesFile):
    """Day 2: Inventory Management System Part 1"""
    arrayNumReapeted = [0, 0] #array that represents the number of words with any leatter reapiting 2 or 3 times
    with open(changesFile, 'r') as f:
        line = f.readline()
        while line:
            flag2 = 0
            flag3 = 0
            for i, char in enumerate(line):
                count = 0
                j = 0
                while(j < len(line)):
                    if line[j] == char:
                        count += 1
                    j += 1
                if count == 2:
                    flag2 += 1
                elif count == 3:
                    flag3 += 1
            if flag2 != 0:
                arrayNumReapeted[0] +=1
            if flag3 != 0:
                arrayNumReapeted[1] +=1
            line = f.readline()            
    f.close()
    return arrayNumReapeted[0] * arrayNumReapeted[1]

def IDsDifferences(changesFile):
    """Day 2: Inventory Management System Part 1"""
    arrayIDs = []
    with open(changesFile, 'r') as f:
        line = f.readline()
        while line:
            arrayIDs.append(line)
            line = f.readline()            
    f.close()
    correctBox = ""
    for i in arrayIDs:
        for j in arrayIDs:
            if sum(1 for a, b in zip(i, j) if a != b) == 1:
                for a, b in zip(i, j):
                    if a == b:
                        correctBox += a
    return correctBox
    
if __name__ == "__main__":
    print(IDsCheckSum("IDs.txt"))
    print(IDsDifferences("IDs.txt"))