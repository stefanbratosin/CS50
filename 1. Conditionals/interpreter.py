def main():
    math_expression = input("Expression:").split(" ")
    x = float(math_expression[0])
    operation = math_expression[1]
    y = float(math_expression[2])
    
    do_math(x, operation, y)
    

def do_math(x:float, operation, y:float):
    match operation:
        case "+":
           preety_print(x + y)
        case "-":
           preety_print(x - y)
        case "*":
           preety_print(x * y)
        case "/":
           preety_print(x / y)
        case _:
            print("Invalid operation")
            
def preety_print(result:float):
    print(f"{result:.1f}")
    
main()