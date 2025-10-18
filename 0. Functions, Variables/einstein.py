def main():
    userInput:int = int(input("m: "))
    energy = calculateEnergy(userInput)
    print(f"E: {energy} Joules")
    
def calculateEnergy(mass):
    c = 300000000
    return mass * pow(c,2)

main()