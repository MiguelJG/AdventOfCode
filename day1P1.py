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
    
if __name__ == "__main__":
    print(calibration("frequencyChanges.txt"))