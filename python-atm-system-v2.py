balance = 1000.00
correct_pin = "1234"
deposit = []
withdraw = []


print("====================================")
print("  WELCOME TO PYTHON BOOTCAMP ATM ")
print("====================================")

while True:
    entered_pin = input("Enter your 4-digit PIN: ")

    if entered_pin != correct_pin:
        print("[!] Incorrect PIN. Please try again.")
    else:
        print("[✓] PIN Verified. Welcome back!")
        break

while True:
    print("\n---------- MAIN MENU ----------")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. View Transaction History")
    print("5. Exit")

    option = input("Choose an option: ")

    if option == "1":
        print(f"[i] Your current balance is: ${balance:.2f}")
    
    elif option == "2":
        amount_str = input("Enter amount to deposit: ")

        if not amount_str.isdigit():
            print("[!] Invalid input. Please enter whole numbers only.")
            continue

        balance += float(amount_str)
        print(f"[✓] ${amount_str} deposited successfully.")
        print(f"[i] New Balance: ${balance:.2f}")

        deposit.append(amount_str)

    
    elif option == "3":
        withdraw_str = input("Enter amount to withdraw: ")

        if not withdraw_str.isdigit():
            print("[!] Invalid input. Please enter whole numbers only.")
            continue
        
        withdraw_amount = float(withdraw_str)

        if withdraw_amount > balance:
            print("[!] Transaction Failed: Insufficient funds.")
            print(f"[!] Your balance is only ${balance:.2f}")
        else:
            balance -= withdraw_amount
            print(f"[✓] Processing... Please take your ${withdraw_amount:.2f}")    
            print(f"[i] New Balance: ${balance:.2f}")

            withdraw.append(withdraw_str)

    elif option == "4":
       print("\n===== TRANSACTION HISTORY =====")

       if len(deposit) and len(withdraw) == 0:
            print("No transactions yet.")
       
       else:
        if len(deposit) > 0:
            print("\nDeposits:")
            for d in deposit:
                print(f"+${d}")

        if len(withdraw) > 0:
            print("\nWithdrawals:")
            for w in withdraw:
                print(f"-${w}")

    elif option == "5":
        print("[!] Session Ended. Please take your card.")
        print("Thank you for using Python ATM!")
        print("====================================")
        break
    
    else: 
        print("[!] Invalid option. Please choose 1-4.")
