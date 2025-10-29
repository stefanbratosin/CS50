def main():
    camel_variable = input("camelCase:")
    print(transform_to_snake_case(camel_variable))
    
def transform_to_snake_case(camel_variable:str):
    length_of_word = len(camel_variable)
    snake_variable = ""
    
    for i in range(length_of_word):
        if camel_variable[i].isupper():
            snake_variable += "_"
        snake_variable += camel_variable[i].lower()
        
    return snake_variable
    
main()