# Bank Account

usd_rate = 0.71
total = 0

# Welcome message 
# Get the initial balance from the user
# Store it in the global balance
def start ():
    print("Welcome!")
    balance = float(input("Enter initial balance: "))
    total = balance
    
    
# Add money to the balance
def deposit(): 
    global total           
    amount = float(input("Enter the value of the depostied money: "))
    total += amount
    
    
# Display the current balance   
def check_balance():
    print("Your total money:",total)
    
    
# Subtract money from the balance
def withdraw():
    global total
    amount = float(input("Enter the value of the money that will be withdrawn: "))
    total = total - amount
    
    
# Convert balance to USD  
def convert_to_dolar():
    return total * usd_rate


def exit_():
    print("The process is succesful!") 



def main():
    while True:
        
        # Display service menu
        print("1. Deposit")
        print("2. Check Balance")
        print("3. Withdraw")
        print("4. Convert to Dolar")
        print("5. Exit")
        service = int(input("Choose a service: "))

        match service:
            case 1:
                print("Deposit")
                deposit()
            case 2:
                print("Check Balance")
                check_balance()
            case 3:
                print("Withdraw")
                withdraw()
     
            case 4:
                print("Convert to Dolar")
                print(convert_to_dolar())
            case 5:
                exit_()
                break
            case _:
                print("Invalid Syntax , try again!")
        
        # Ask user if they want another service
        
        end = input("Is there another service? (yes/no): ")
        if end.upper() == "YES":
            continue
        else:
            exit_()  
            break
start()    
main()    
