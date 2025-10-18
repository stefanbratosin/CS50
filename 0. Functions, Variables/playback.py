def main():
    userInput = input()
    playback(userInput)
    
def playback(text:str):
    playbackText= text.replace(" ","...")
    print(playbackText)
    
main()