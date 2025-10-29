#  Purpose: program that prompts the user  to input a fruit (case insensitive) and outputs the number of calories in one portion of fruit
#  Assume users will input the name of the fruit correctly. Ignore any input that is  not a fruit.
"""
Solutions: 
1. Create a dictionary and store the fruits and calories there, when checking the fruits just compare to the dictionary and if found return the calories.
2. 2 array of strings of the same length, 1 with fruits and the second with calories, match to the fruit array and return the calories from the second array
3. create a list of variables (each a fruit) and assign a calorie value to them, then check the input vs the variable name and then output the value assigned to the variable.

Will go with solution 1 as it is the easier one to implement.
"""
fda_list = {"apple": "130", "avocado": "50", "banana": "110", "cantaloupe": "50", "grapefruit": "60", "grapes": "90", "honeydew melon": "50", "kiwifruit": "90"}

def main():
    
    fruit = input("Item: ").lower()
    get_calories(fruit)
    
def get_calories(fruit:str):
    
    if fruit in fda_list:
        print(f"Calories: {fda_list[fruit]}")
    
main()