def main():
    #  we sell coke  - 50 cents 
    ammount_due = 50
    #  tell the user ammount owned
    print("Change Owed: 50")
    #  calculate remainder
    #  repeat untill ammount is 0 and exit 
    request_pament(ammount_due)
    
def request_pament(ammount_due:int):
    while ammount_due > 0:
        coin = validate_coin(input("Insert coin: "))
        if coin <= ammount_due:
            ammount_due -= coin
        else:
            print("Invalid coin")
        print(f"Change Owed: {ammount_due}")

def validate_coin(ammount:str):
    #  only accept coins of : 25 cents, 10 cents, 5 cents 
    if ammount in ["25", "10", "5"]:
        return int(ammount)
    else:
        return 0

main()