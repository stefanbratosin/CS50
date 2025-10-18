def main():
    userInput = input()
    faces(userInput)
    
def faces(text:str):
    # First replace funny faces
    funnyReplace= text.replace(":)","🙂")
    # Then replace sad faces for the result
    result= funnyReplace.replace(":(","🙁")
    print(result)
    
main()