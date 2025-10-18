def main():
# prompt for greeting
    print("Give greeting to customer: ")
    
# Sanitize input
    greeting = sanitizeInput(input())

# if greeting = " hello" print 0
#  if greeting starts with "h" print 20 
#  if greeting not with h  print 100

    if greeting.find("hello")>=0:
        print("$0")
    elif greeting.startswith("h"):
        print("$20")
    else:
        print("$100")

def sanitizeInput(greeting:str):
    return greeting.lower().lstrip()


main()