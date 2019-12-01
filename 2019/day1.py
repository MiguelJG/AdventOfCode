def fuelCalculator(mass):
    """
    This function calculates the mass of a single component based in its description
    """
    return int(mass / 3) - 2

def loadComponents(fileName):
    """
    This function loads a file containing the mass of all components and adds al the value together
    """
    finalMass = 0
    try:
        f = open(fileName,"r")
        for line in f.readlines():
            finalMass += fuelCalculator(int(line))
    except IOError as e:
        print ("I/O error({0}): {1}".format(e.errno, e.strerror))
    f.close()
    return finalMass
    

def recursiveFuelCalc(mass):
    """This function calculates recursively the amount of fuel needed for the fuel nneded for the fuel needed for the fuel...."""
    fuel = fuelCalculator(mass)
    if fuel <= 0:
        return 0
    else:
        fuel += recursiveFuelCalc(fuel)
        return fuel

def loadComponentsRecursive(fileName):
    """
    This function loads a file containing the mass of all components and adds al the value together plus the value of its needed fuel in a recursive way to have
    in account the fuel needed for the fuel
    """
    finalMass = 0
    try:
        f = open(fileName,"r")
        for line in f.readlines():
            finalMass += recursiveFuelCalc(int(line))
    except IOError as e:
        print ("I/O error({0}): {1}".format(e.errno, e.strerror))
    f.close()
    return finalMass

if __name__ == "__main__":
    INPUTFILE = "/home/miguel/Documentos/AdventOfCode/2019/inputday1.txt"
    print("Total fuel mass required by all the components --> ", loadComponents(INPUTFILE))
    print("The total of the fuel with the fuel for the fuel -->", loadComponentsRecursive(INPUTFILE))