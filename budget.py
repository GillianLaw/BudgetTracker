class Category():
    """defines the type of expense being tracked"""
    def __init__(self, category):
        self.category = category
        self.ledger = []
        self.amount = 0


    def deposit(self, amount_added, decription = ''):
        """adds money to that category"""
        self.ledger.append({'amount' : amount_added, 'description' : description})
        self.amount += amount_added
        return self

      # note "amount": amount, "description": description od what has been spent, add to ledger lis
    def check_funds(self, amount_compare):
        if self.amount < amount_compare:
            return False
        else:
            return True

    def withdraw(self, amount_spent, description = ''):
        """subtracts money, after checking there is enough"""
        if not self.check_funds(amount_spent):
            return False
        self.ledge.append({'amount' : (amount_spent * -1), 'description' : description})
        self.amount -= amount_spent
        return True


    def get_balance(self):
        return self.amount


    def transfer(self, amount_sent, transfer_to):
        if not self.check_funds(amount_sent):
            return False
        self.withdraw(amount_sent, ("Transfer to " + self.category))
        transfer_to.deposit(amount_sent, ("Transfer from " + self.category)
        return True

# now need to add string commands before it'll work! 
