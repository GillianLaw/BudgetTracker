class Category():
    """defines the type of expense being tracked"""
    def __init__(self, category):
        self.category = category
        self.ledger = []
        self.amount = 0

        
    def deposit(self, amount_added, decription = ''):
        if not description:
            description = ''
        self.ledger.append({'amount' : amount_added, 'description' : description})
        self.amount += amount_added
        return True

      # note "amount": amount, "description": description od what has been spent, add to ledger list

    def withdraw(self, amount_spent, description = ''):
        if not self.check_funds(amount_spent):
            return False
        if not description:
            descrition = ''
        self.ledge.append({'amount' : (amount_spent * -1), 'description' : description})
        self.amount -= amount_spent
        return True


    def get_balance(self):
      # this needs to go through and identify categories and add/ subtract amounts in each
        pass

    def transfer(self):
      # move from one category to another, but only if there's enough
        pass

    def check_funds(self):
      # this is used by both withdraw and transfer - checking there's enough money
        pass



  # et cetera  #



def create_spend_chart(categories):
  # this needs a list of all catoegories, and ... a string creating a bar chart. No idea at the moment how to do that!
