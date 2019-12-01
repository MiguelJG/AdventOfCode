import numpy as np

def getFabricClaims(claimsFile):
    """Day 3: No Matter How You Slice It. Part 1"""
    fabric = np.full((1000, 1000), 0)
    with open(claimsFile, 'r') as f:
        line = f.readline()
        while line:
            pos =  list(map(int, line.replace(':', '').split()[2].split(",")))
            tam =   list(map(int, line.split()[3].split("x")))
            for i in range  (pos[0], tam[0] + pos[0]):
                for j in range  (pos[1], tam[1] + pos[1]):
                    fabric[i][j] += 1
            line = f.readline()
    f.close()
    counter = 0
    for i in range(1000):
        for j in range(1000):
            if fabric[i][j] > 1:
                counter += 1
    return counter
    
def getID(claimsFile):
    """Day 3: No Matter How You Slice It. Part 2"""
    fabric = np.full((1000, 1000), 0)
    claims = []
    with open(claimsFile, 'r') as f:
        line = f.readline()
        while line:
            pos =  list(map(int, line.replace(':', '').split()[2].split(",")))
            tam =   list(map(int, line.split()[3].split("x")))
            temp = []; temp.append(line.split()[0]); temp.append(pos); temp.append(tam); claims.append(temp)
            for i in range  (pos[0], tam[0] + pos[0]):
                for j in range  (pos[1], tam[1] + pos[1]):
                    fabric[i][j] += 1
            line = f.readline()
    f.close()
    for claim in claims:
        unica = True
        for i in range  (claim[1][0], claim[2][0] + claim[1][0]):
            for j in range  (claim[1][1], claim[2][1] + claim[1][1]):
                if not fabric[i][j] == 1:
                    unica = False
        if unica:
            return claim[0]
    
if __name__ == "__main__":
    print(getFabricClaims("fabricClaims.txt"))
    print(getID("fabricClaims.txt"))