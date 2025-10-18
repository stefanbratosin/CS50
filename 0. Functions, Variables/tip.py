def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d:str):
    # remove the dollar sign and convert to float
    dollarVallue= float(d.replace("$",""))
    return dollarVallue



def percent_to_float(p:str):
    tip = float(p.replace("%",""))/100
    return tip

main()