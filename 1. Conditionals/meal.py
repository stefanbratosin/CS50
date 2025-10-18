def main():
    time = input("What time is it? ")
    result = convert(time)
    is_mealtime(result)
    

def convert(time:str):
    hour, minutes = time.split(":")
    minutes = int(minutes)/60
    hour = int(hour)
    return float("{:.1f}".format(minutes + hour))

def is_mealtime(time:float):
    if time >= 7.0 and time <= 8.0:
        print("breakfast time")
    elif time >= 12.0 and time <= 13.0:
        print("lunch time")
    elif time >= 18.0 and time <= 19.0:
        print("dinner time")

    
if __name__ == "__main__":
    main()