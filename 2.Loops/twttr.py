#  need to remove al vowels from a text. - purpose
#  how? -> solution 1: parsing the string and copying every letter to another string except the vowels 
#  soolution 2: -> replace the vowels with a chart and the format the string and remove the char then
#  solution 3: print the string as we parse it and just don't print the vowels
#  let's go with solution 3

def main():
    twttr_message = input("Input: ")
    remove_vowels(twttr_message)
    
def remove_vowels(twttr_message:str):
    print("Output: ", end="")
    for letter in twttr_message:
        if letter.lower() not in ["a", "e", "i", "o", "u"]:
            print(letter, end="")
    print()

 
main()