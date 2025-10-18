def main():
    print("What is the answer to the Great Question of Life, the Universe, and Everything?")
    answer = input().lower()
    if isNumber(answer):
        if int(answer) == 42:
            print("Yes")
        else:
            print("No")
    elif answer == "forty-two" or answer == "forty two":
        print("Yes")
    else:
        print("No")
        
def isNumber(value):
    return value.isnumeric()
    

main()
