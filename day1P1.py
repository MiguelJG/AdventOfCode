def calibration(changesFile):
    """Day 1: Chronal Calibration Part 1"""
    calibrationNum = 0
    with open(changesFile, 'r') as f:
        line = f.readline()
        while line:
            calibrationNum += int(line)
            line = f.readline()
    f.close()        
    return calibrationNum
    
def repitedFrequency(changesFile):
    """Day 1: Chronal Calibration Part 2"""
    setF = set()
    calibrationNum = 0
    while True:
        with open(changesFile, 'r') as f:
            line = f.readline()
            while line:
                calibrationNum += int(line)
                if calibrationNum in setF:
                    return calibrationNum
                else:
                    setF.add(calibrationNum)
                line = f.readline()
        f.close()

if __name__ == "__main__":
    print(calibration("frequencyChanges.txt"))
    print(repitedFrequency("frequencyChanges.txt"))