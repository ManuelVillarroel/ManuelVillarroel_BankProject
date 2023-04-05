print("+----------------------------------------------+")
print("| Welcome to your own personal banking system. |")
print("|         What would you like to do?           |")
print("+----------------------------------------------+\n")
# Future methods to be made
print("1. Check my Balance")
print("2. Make a Deposit")
print("3. Make a Withdrawal")
print("4. Create a New Account")
print("5. Delete an Existing Account")
print("6. Modify an Existing Account\n")

def CheckBalance():
    print("balance")
    return
def MakeDeposit():
    print("deposit")
    return
def MakeWithdrawal():
    print("withdrawal")
    return
def CreateAccount():
    print("create an account")
    return
def DeleteAccount():
    print("delete an account")
    return
def ModifyAccount():
    print("modify an account")
    return

while(True):
    playerInput = input("Please input the number you would like to access: ")
    try:
        if playerInput.upper().__contains__("BALANCE"):
            CheckBalance()
            break
        elif playerInput.upper().__contains__("DEPOSIT"):
            MakeDeposit()
            break
        elif playerInput.upper().__contains__("WITHDRAWAL"):
            MakeWithdrawal()
            break
        elif playerInput.upper().__contains__("CREATE"):
            CreateAccount()
            break
        elif playerInput.upper().__contains__("DELETE"):
            DeleteAccount()
            break
        elif playerInput.upper().__contains__("MODIFY"):
            ModifyAccount()
            break

        playernumber = int(playerInput)
        
        if playernumber == 1:
            CheckBalance()
            break
        elif playernumber == 2:
            MakeDeposit()
            break
        elif playernumber == 3:
            MakeWithdrawal()
            break
        elif playernumber == 4:
            CreateAccount()
            break
        elif playernumber == 5:
            DeleteAccount()
            break
        elif playernumber == 6:
            ModifyAccount()
            break
        else:
            print(f"[{playerInput}] is not a number or an option")

    except ValueError:
        print(f"[{playerInput}] is not a number or an option")
