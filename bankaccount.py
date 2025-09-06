import random

class BankAccount:
    promo_prize = 2000  

    def __init__(self, name, amount, isPromo=False, isAdmin=Fals):
        if isPromo:
            amount += self.promo_prize

        self.account_name = name
        self.account_balance = amount
        self.account_number = random.randint(1000, 9000)
        self.isAdmin = isAdmin
        self.isFrozen = False 

    
    def freeze_account(self, target_account):
        if self.isAdmin:
            target_account.isFrozen = True
            return f"{target_account.account_name}'s account has been frozen."
        return "Permission denied. Only admin can freeze accounts."

    def unfreeze_account(self, target_account):
        if self.isAdmin:
            target_account.isFrozen = False
            return f"{target_account.account_name}'s account has been unfrozen."
        return "Permission denied. Only admin can unfreeze accounts."

  
    def deposit(self, amount):
        if self.isFrozen:
            return "Account is frozen. Deposit not allowed."
        self.account_balance += amount
        return self.send_message("credit", amount)

    def withdrawal(self, amount):
        if self.isFrozen:
            return "Account is frozen. Withdrawal not allowed."
        if amount > self.account_balance:
            return "Insufficient funds."
        self.account_balance -= amount
        return self.send_message("debit", amount)

    def transfer(self, target_account, amount):
        if self.isFrozen:
            return "Account is frozen. Transfer not allowed."
        if amount > self.account_balance:
            return "Insufficient funds for transfer."
        self.account_balance -= amount
        target_account.account_balance += amount
        debit_msg = self.send_message("debit", amount)
        credit_msg = target_account.send_message("credit", amount)
        return debit_msg + "\n" + credit_msg


 
ab = BankAccount("AB", 1000, True)
jc = BankAccount("JC", 2000)


admin = BankAccount("Admin", 0, isAdmin=True)

print(admin.freeze_account(jc))
print(jc.deposit(500))


print(admin.unfreeze_account(jc))
print(jc.deposit(500))


print(ab.transfer(jc, 1000))