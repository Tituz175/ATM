generalList = []
data = {}
email = ""
pin = ""
amountValue = 0
cardList = [1000,500,200,100]
cardOption = ""
phone = 0



def generallist():
    generalOption = input("Select option: ")
    if generalOption == "3":
        print(generalList)
        rootHome()
    else:
        print("error")

def logOut():
    print("Thank You for banking with us, have a nice day.")
    print("Welcome to ")
    print("1. Login")
    print("2. Register")
    print("3. Show generalList")

    rootHome()

def moneyOut1():
    global email
    global pin
    message = ""
    for details in generalList:
        if details["Email"] == email and details["Pin"] == pin:
            if details["Balance"] < 10000:
                print("Insufficient Balance")
            else:
                details["Balance"] = details["Balance"] - 10000
                data["History"].append("You withdral #10000.")
                print("Your #10000 withdrawal was successful.")
                print("Your current balance is #" + str(details["Balance"]) + ".")    
        else:
            message = "Transaction error"

def moneyOut2():
    global email
    global pin
    message = ""
    for details in generalList:
        if details["Email"] == email and details["Pin"] == pin:
            if details["Balance"] < 5000:
                print("Insufficient Balance")
            else:
                details["Balance"] = details["Balance"] - 5000
                data["History"].append("You withdral #5000.")
                print("Your #5000 withdrawal was successful.")
                print("Your current balance is #" + str(details["Balance"]) + ".")    
        else:
            message = "Transaction error"

def moneyOut3():
    global email
    global pin
    message = ""
    for details in generalList:
        if details["Email"] == email and details["Pin"] == pin:
            if details["Balance"] < 2000:
                print("Insufficient Balance")
            else:
                details["Balance"] = details["Balance"] - 2000
                data["History"].append("You withdral #2000.")
                print("Your #2000 withdrawal was successful.")
                print("Your current balance is #" + str(details["Balance"]) + ".")    
        else:
            message = "Transaction error"

def moneyOut4():
    global email
    global pin
    message = ""
    for details in generalList:
        if details["Email"] == email and details["Pin"] == pin:
            if details["Balance"] < 1000:
                print("Insufficient Balance")
            else:
                details["Balance"] = details["Balance"] - 1000
                data["History"].append("You withdral #1000.")
                print("Your #1000 withdrawal was successful.")
                print("Your current balance is #" + str(details["Balance"]) + ".")    
        else:
            message = "Transaction error"

def moneyOut5():
    global email
    global pin
    message = ""
    for details in generalList:
        if details["Email"] == email and details["Pin"] == pin:
            if details["Balance"] < 500:
                print("Insufficient Balance")
            else:
                details["Balance"] = details["Balance"] - 500
                data["History"].append("You withdral #500.")
                print("Your #500 withdrawal was successful.")
                print("Your current balance is #" + str(details["Balance"]) + ".")    
        else:
            message = "Transaction error"

def moneyOutothers():
    global email
    global pin
    global amountValue
    message = ""
    for details in generalList:
        if details["Email"] == email and details["Pin"] == pin:
            if details["Balance"] < amountValue:
                print("Insufficient Balance")
            else:
                details["Balance"] = details["Balance"] - amountValue
                data["History"].append("You withdral #" + str(amountValue) + ".")
                print("Your #" + str(amountValue) + " withdrawal was successful.")
                #print("Your current balance is #" + str(details["Balance"]) + ".")
        else:
            message = "Transaction error"

def withdraw():
    print("How much do you want to withdraw?")
    print("1. 10,000")
    print("2. 5,000")
    print("3. 2,000")
    print("4. 1,000")
    print("5. 500")
    print("6. others")
    print("7. Back")
    withdrawOption = input("Select option: ")
    if withdrawOption == "1":
        
        moneyOut1()
        print("Do you want to perform another transaction?")
        print("1. Yes")
        print("2. No")
        anotherOption = input("Select option: ")
        if anotherOption == "1":
            user()
        elif anotherOption == "2":
            logOut()
        else:
            print("Invalid selection")
    elif withdrawOption == "2":
        
        moneyOut2()
        print("Do you want to perform another transaction?")
        print("1. Yes")
        print("2. No")
        anotherOption = input("Select option: ")
        if anotherOption == "1":
            user()
        elif anotherOption == "2":
            logOut()
        else:
            print("Invalid selection")
    elif withdrawOption == "3":
        
        moneyOut3()
        print("Do you want to perform another transaction?")
        print("1. Yes")
        print("2. No")
        anotherOption = input("Select option: ")
        if anotherOption == "1":
            user()
        elif anotherOption == "2":
            logOut()
        else:
            print("Invalid selection")
    elif withdrawOption == "4":
        
        moneyOut4()
        print("Do you want to perform another transaction?")
        print("1. Yes")
        print("2. No")
        anotherOption = input("Select option: ")
        if anotherOption == "1":
            user()
        elif anotherOption == "2":
            logOut()
        else:
            print("Invalid selection")
    elif withdrawOption == "5":
        
        moneyOut5()
        print("Do you want to perform another transaction?")
        print("1. Yes")
        print("2. No")
        anotherOption = input("Select option: ")
        if anotherOption == "1":
            user()
        elif anotherOption == "2":
            logOut()
        else:
            print("Invalid selection")
    elif withdrawOption == "6":
        global amountValue
        amountValue = int(input())
        moneyOutothers()
        print("Do you want to perform another transaction?")
        print("1. Yes")
        print("2. No")
        anotherOption = input("Select option: ")
        if anotherOption == "1":
            withdraw()
        elif anotherOption == "2":
            logOut()
        else:
            print("Invalid selection")
    elif withdrawOption == "7":
        user()
    else:
        print("Invalid selection")

def histroy():
    global email
    global pin
    message = ""
    for details in generalList:
        if details["Email"] == email and details["Pin"] == pin:
            message = (data["History"])
        else:
            message = "Transaction error"
    print(message)

    print("Do you want to perform another transaction?")
    print("1. Yes")
    print("2. No")
    anotherOption = input("Select option: ")
    if anotherOption == "1":
        user()
    elif anotherOption == "2":
        logOut()
    else:
        print("Invalid selection")


def ban():
    global email
    global pin
    message = ""
    for details in generalList:
        if details["Email"] == email and details["Pin"] == pin:
            if details["Balance"] < 0:
                print("Your current balance is #0.")
            else:
                print("Your current balance is #" + str(details["Balance"]) + ".")
        else:
            message = "Transaction error"

    print("Do you want to perform another transaction?")
    print("1. Yes")
    print("2. No")
    anotherOption = input("Select option: ")
    if anotherOption == "1":
        user()
    elif anotherOption == "2":
        logOut()
    else:
        print("Invalid selection")

def proceed():
    global pin
    #word = ""
    email = input("Enter the receiver's email address: ")
    amount = input("Enter the amount you want to transfer: ")
    for details in generalList:
        if details["Pin"] == pin:
            if details["Balance"] > 0 and int(amount) <= details["Balance"]:
                details["Balance"] = details["Balance"] - int(amount)
                details["History"].append("You sent of #" + amount + ".")
                mess = ""
                for details in generalList:
                    if details["Email"] == email:
                        details["Balance"] = details["Balance"] + int(amount)
                        mess = "#" + amount + " transfered successfully to " + details["First Name"] + " " + details["Last Name"] + "."
                        break
                    else:
                        mess = "Invalid account details"
                # print("Your current balance is #" + str(details["Balance"] - (2*int(amount))) + ".")
                print(mess)
                break
            else:
                print("Insufficient fund")
        # else:
        #     word = "Insufficient fund"

    # for details in generalList:
    #    if(details["Email"] == email):
    #        details["Balance"] = details["Balance"] + int(amount)
    #        print("#" + amount + " was transfered successfully to " + email + ".")
    #    else:
    #        message="Invalid account details"
    # for details in generalList:
    #     if details["Pin"] == pin:
    #         details["Balance"] = details["Balance"] - int(amount)
    #         if details["Balance"] < 0:
    #             print("Insufficient fund")
    #         else:
    #             print("Your current balance is #" + str(details["Balance"]) + ".")

    print("Do you want to perform another transaction?")
    print("1. Yes")
    print("2. No")
    anotherOption = input("Select option: ")
    if anotherOption == "1":
        user()
    elif anotherOption == "2":
        logOut()
    else:
        print("Invalid selection")


def trans():
    print("1. Proceed")
    print("2. Back")
    transOption = input("Select option: ")
    if transOption == "1":
        proceed()
    elif transOption == "2":
        user()
    else:
        print("Invalid selection")


def mobile():
    print("Welcome to mobile top-up")
    print("1. MTN e-topup")
    print("2. GLO e-topup")
    print("3. Airtel e-topup")
    print("4. Etisalat e-topup")
    print("5. Back")

    mobileOption = input("Select option: ")
    if mobileOption == "1":
        print("Welcome to MTN e-topup")
        card()
    elif mobileOption == "2":
        print("Welcome to GLO e-topup")
        card()
    elif mobileOption == "3":
        print("Welcome to Airtel e-topup")
        card()
    elif mobileOption == "4":
        print("Welcome to Etisalat e-topup")
        card()
    elif mobileOption == "5":
        user()
    else:
        print("Invalid Selection")
        user()

def cardProceed(i):
    global pin
    message = ""
    for details in generalList:
        if details["Pin"] == pin:
            details["Balance"] = details["Balance"] - i
            message = "Success"
            break
        else:
            message = "Error"
    print(message)

def cardAnother():
    print("Do you want to perform another transaction?")
    print("1. Yes")
    print("2. No")
    cardAnotheroption = input("Select option: ")
    if cardAnotheroption == "1":
        card()
    elif cardAnotheroption == "2":
        user()
    else:
        print("Invalid Selection")
        user()

def card():
    global cardList
    global pin
    global cardOption
    global phone
    print("How much airtime do you want to buy?")
    print("1. 1,000")
    print("2. 500")
    print("3. 200")
    print("4. 100")
    print("5. Others")
    print("6. Back")

    cardOption = input("Select option: ")  

    if cardOption == "1":
        for details in generalList:
            if details["Pin"] == pin:
                if details["Balance"] >= cardList[0]:
                    ask()
                    askOption = input("Select option: ")
                    if askOption == "1":
                        cardProceed(cardList[0])
                        details["History"].append("You recharge #" + str(cardList[0]) + ".")
                        print("Your recharge of #" + str(cardList[0]) + " was successful.")
                        cardAnother()
                        
                    elif askOption == "2":
                        otherNumber()
                        cardProceed(cardList[0])
                        details["History"].append("You recharge #" + str(cardList[0]) + " for " + phone + ".")
                        print("Your #" + str(cardList[0]) + " recharge for " + phone + " was successful.")
                        cardAnother()

                    elif askOption == "3":
                        user()
                    else:
                        print("Invalid Selection")
                        user()
                else:
                    print("Insufficient fund")
                    mobile()
    elif cardOption == "2":
        for details in generalList:
            if details["Pin"] == pin:
                if (details["Balance"] >= cardList[1]):
                    ask()
                    askOption = input("Select option: ")
                    if askOption == "1":
                        cardProceed(cardList[1])
                        details["History"].append("You recharge #" + str(cardList[1]) + ".")
                        print("Your recharge of #" + str(cardList[1]) + " was successful.")
                        cardAnother()
                        
                    elif askOption == "2":
                        otherNumber()
                        cardProceed(cardList[1])
                        details["History"].append("You recharge #" + str(cardList[1]) + " for " + phone + ".")
                        print("Your #" + str(cardList[1]) + " recharge for " + phone + " was successful.")
                        cardAnother()
                        
                    elif askOption == "3":
                        user()
                    else:
                        print("Invalid Selection")
                        user()
                else:
                    print("Insufficient fund")
                    mobile()
    elif cardOption == "3":
        for details in generalList:
            if details["Pin"] == pin:
                if (details["Balance"] >= cardList[2]):
                    ask()
                    askOption = input("Select option: ")
                    if askOption == "1":
                        cardProceed(cardList[2])
                        details["History"].append("You recharge #" + str(cardList[2]) + ".")
                        print("Your recharge of #" + str(cardList[2]) + " was successful.")
                        cardAnother()
                        
                    elif askOption == "2":
                        otherNumber()
                        cardProceed(cardList[2])
                        details["History"].append("You recharge #" + str(cardList[2]) + " for " + phone + ".")
                        print("Your #" + str(cardList[2]) + " recharge for " + phone + " was successful.")
                        cardAnother()
                        
                    elif askOption == "3":
                        user()
                    else:
                        print("Invalid Selection")
                        user()
                else:
                    print("Insufficient fund")
                    mobile()
    elif cardOption == "4":
        for details in generalList:
            if details["Pin"] == pin:
                if (details["Balance"] >= cardList[3]):
                    ask()
                    askOption = input("Select option: ")
                    if askOption == "1":
                        cardProceed(cardList[3])
                        details["History"].append("You recharge #" + str(cardList[3]) + ".")
                        print("Your recharge of #" + str(cardList[3]) + " was successful.")
                        cardAnother()
                        
                    elif askOption == "2":
                        otherNumber()
                        cardProceed(cardList[3])
                        details["History"].append("You recharge #" + str(cardList[3]) + " for " + phone + ".")
                        print("Your #" + str(cardList[3]) + " recharge for " + phone + " was successful.")
                        cardAnother()
                        
                    elif askOption == "3":
                        user()
                    else:
                        print("Invalid Selection")
                        user()
                else:
                    print("Insufficient fund")
                    mobile()
    elif cardOption == "5":
        value = input("Input the card amount: ")
        for details in generalList:
            if details["Pin"] == pin :
                if details["Balance"] >= int(value):
                    ask()
                    askOption = input("Select option: ")
                    if askOption == "1":
                        cardProceed(int(value))
                        details["History"].append("You recharge #" + value + ".")
                        print("Your recharge of #" + value + " was successful.")
                        cardAnother()
                        
                    elif askOption == "2":
                        otherNumber()
                        cardProceed(int(value))
                        details["History"].append("You recharge #" + value + " for " + phone + ".")
                        print("Your #" + value + " recharge for " + phone + " was successful.")
                        cardAnother()
                        
                    elif askOption == "3":
                        user()
                    else:
                        print("Invalid Selection")
                        user()
                else:
                    print("Insufficent fund")
                    mobile()
    elif cardOption == "6":
        mobile()
    else:
        print("Invalid Selection")
        card()


def otherNumber():
    global phone
    phone = input("Input the receive's number: ")
    if len(phone) == 11:
        pass
    else:
        print("Invalid number")
        ask()
    
    

def ask():
    global cardOption
    print("1. Self Recharge")
    print("2. Other Party")
    print("3. Back")
    

    



def user():
    for details in generalList:
        if details["Email"] == email and details["Pin"] == pin:
            print("Welcome " + details["First Name"] + " " + details["Last Name"] + ".")
            print("1. Withdraw")
            print("2. Mobile Top-up")
            print("3. Transfer")
            print("4. Banlance")
            print("5. Histroy")
            print("6. Log Out")


    userOption = input("Select option: ")
        
    if userOption == "1":
        withdraw()
    elif userOption == "2":
        mobile()
    elif userOption == "3":
        trans()
    elif userOption == "4":
        ban()
    elif userOption == "5":
        histroy()
    elif userOption == "6":
        logOut()
    else:
        print("Invalid selection")



def login():
    global email
    global pin
    message = ""
    email = input("Enter your Email: ")
    pin = input("Enter your Pin: ")
    for details in generalList:
        if(details["Email"] == email and details["Pin"] == pin):
           
            user()

            break
        else:
            message = "Invalid login details"
    print(message)       
   

         


# def access():
#     if generalList[0]["Email"] == "email" and generalList[0]["Pin"] == "pin":
#         user()
#     else:
#         print("Invalid login details")

def reg():
    global data
    data = {}
    data["First Name"] = input("Enter your first name: ")
    data["Last Name"] = input("Enter your last name: ")
    data["Email"] = input("Enter your email address: ")
    data["Pin"] = input("Enter your pin: ")
    data["Balance"] = 50000
    data["History"] = []
    
    # for details in generalList:
    #     if(details["Email"] == data["Email"]):
    #         print("Used email address, input a new one.")
    #     else:

    generalList.append(data)
    print("Welcome "+ data["First Name"] + " " + data["Last Name"] +".")
    print("Do you wish to transact? ")
    print("1. Yes")
    print("2. No")
    regOption = input("Select option: ")
    if regOption == "1":
        login()
    elif regOption == "2":
        logOut()
    else:
        print("Invalid selection")


def rootHome():
    homeOption = input("Select option: ")
    if homeOption == "1":
        login()
    elif homeOption == "2":
        reg()
    elif homeOption == "3":
        generallist()
    else:
        print("Invalid selection")
    

print("Welcome to ")
print("1. Login")
print("2. Register")

rootHome()
