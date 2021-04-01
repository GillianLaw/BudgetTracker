class Category():
    def __init__(self, category, funds):
        self.category = category
        self._funds = _funds
        self._alive = True
        # do i need to identify the categories here? or where?

    ledger = []

    def deposit(self, amount):
      remaining_balance = self._funds - amount
      if remaining_balance >= 0:
          self._funds = remaining_balance
          print("I spent {} and have {} left".format(amount, self.funds))
      else:
          print("You do not have sufficient funds")
          self._solvent = False

      # note "amount": amount, "description": description od what has been spent, add to ledger list

    def withdraw(self, amount, description):
      # as above but negative number
        pass

    def get_balance(self):
      # this needs to go through and identify categories and add/ subtract amounts in each
        pass

    def transfer(self):
      # move from one category to another, but only if there's enough
        pass

    def check_funds(self):
      # this is used by both withdraw and transfer - checking there's enough money
        pass

class Food(Category):

  def __init__(self, amount):
        super().__init__(amount=amount)
  pass

class Clothing(Category):
    def __init__(self, amount):
        super().__init__(amount=amount)
    pass

  # et cetera  #



def create_spend_chart(categories):
  # this needs a list of all catoegories, and ... a string creating a bar chart. No idea at the moment how to do that! 
