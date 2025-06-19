class BankAccount:
    bank_title="SBI"
    
    # Constructor to initialize account holder's name and balance
    def __init__(self, customer_name, current_balance, minimum_balance):
        #instance variables
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance
        
    # Method to deposit money into the account
    def deposit(self, amount):
        self.current_balance += amount
        
        
    # Method to withdraw money from the account
    def withdraw(self, amount):
        if self.current_balance - amount >= self.minimum_balance:
            self.current_balance -= amount
        else:
            print("Insufficient balance to maintain minimum balance after withdrawal.") 
            
    # Method to display account details
    def print_customer_information(self):
        print(f"Bank: {self.bank_title}")
        print(f"Customer Name: {self.customer_name}")
        print(f"Current Balance: {self.current_balance}")
        print(f"Minimum Balance: {self.minimum_balance}")
        
    
    #example
account = BankAccount("Ethan", 1000, 100)
account.print_customer_information()
account.deposit(500)
account.print_customer_information()
#account.withdraw(200)
#account.print_customer_information() 