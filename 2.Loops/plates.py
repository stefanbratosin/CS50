"""  Purpose : prompt the user for a licence plate and validate it., return valid or invalid based on the result
     Requirements:
        - start with at least 2 letters
        - maximum of 6 characters(letters or numbers), and a minimum of 2 characters
        - Numbers can only be used at the end of the licence plate
        - first number can't be 0
        - no periods, spaces or punctuation marks are allowed.
"""

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s:str):
    is_plate_valid = True
    # check for special characters
    if not s.isalnum():
        is_plate_valid = False
    # check for maximum and minimum length
    if len(s) < 2 or len(s) > 6:
        is_plate_valid = False
    # check that is starts with at least two letters
    if not s[:2].isalpha():
        is_plate_valid = False

    # iterate through the string untill you get the first number (can't be 0), continue parsing, if you find a letter the False, else true
    found_number = False
    for i in range(len(s)):
        if s[i].isdigit():
            if found_number == False:
                if s[i] == "0":
                    is_plate_valid = False
                else:
                    found_number = True
        if s[i].isalpha():
            if found_number:
                is_plate_valid = False
        
    return is_plate_valid

main()