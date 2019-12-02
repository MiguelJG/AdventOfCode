computer = {
    "memory" : [], #program memory
    "OUTPUT" : -1, #program output
    "PC" : 0      #program counter
}

def opcode1(param1,param2,param3):
    computer["memory"][param3] = computer["memory"][param1] + computer["memory"][param2]
    computer["OUTPUT"] = param3
    computer["PC"] += 4

def opcode2(param1,param2,param3):
    computer["memory"][param3] = computer["memory"][param1] * computer["memory"][param2]
    computer["OUTPUT"] = param3
    computer["PC"] += 4

def opcode99():
    if computer["PC"] < len(computer["memory"]):
        computer["OUTPUT"] = computer["memory"][computer["OUTPUT"]]

instructions = {
    1: opcode1,
    2: opcode2,
    99: opcode99
}

def loadmem(fileName):
    try:
        f = open(fileName,"r")
        computer["memory"] = f.read().split(",")
        for i in range(len(computer["memory"])):
            computer["memory"][i] = int(computer["memory"][i])
    except IOError as e:
        print ("I/O error({0}): {1}".format(e.errno, e.strerror))
    f.close()

def programAlarm1202():
    computer["memory"][1] = 12
    computer["memory"][2] = 2

def compute(fileName):
    loadmem(fileName)
    programAlarm1202()
    while computer["memory"][computer["PC"]] != 99:
        instructions[computer["memory"][computer["PC"]]](computer["memory"][computer["PC"] + 1],computer["memory"][computer["PC"] + 2],computer["memory"][computer["PC"] + 3])
    instructions[computer["memory"][computer["PC"]]]()
    print("Program output: ", computer["OUTPUT"])

def bruteForce(fileName, num):
    for i in range(0,100):
        for j in range(0,100):
            computer["memory"] = []
            computer["OUTPUT"] = -1
            computer["PC"] = 0
            loadmem(fileName)
            computer["memory"][1] = i
            computer["memory"][2] = j
            while computer["memory"][computer["PC"]] != 99:
                instructions[computer["memory"][computer["PC"]]](computer["memory"][computer["PC"] + 1],computer["memory"][computer["PC"] + 2],computer["memory"][computer["PC"] + 3])
            instructions[computer["memory"][computer["PC"]]]()
            #print(computer["OUTPUT"] ,"---", num)
            if computer["OUTPUT"] == num:
                return str(computer["memory"][1]) + str(computer["memory"][2])

if __name__ == "__main__":
    compute("./inputday2.txt")
    print(bruteForce("./inputday2.txt", 19690720))
    