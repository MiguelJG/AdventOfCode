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
    print(IDsDifferences("IDs.txt"))
