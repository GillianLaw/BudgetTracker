class Category():
    """defines the type of expense being tracked"""
    def __init__(self, category):
        self.category = category
        self.ledger = []
        self.amount = 0


    def deposit(self, amount_added, description=False):
        """adds money to that category"""
        if not description:
            description = ''
        self.ledger.append({'amount' : amount_added, 'description' : description})
        self.amount += amount_added
        return self

      # note "amount": amount, "description": description od what has been spent, add to ledger lis
    def check_funds(self, amount_compare):
        if self.amount < amount_compare:
            return False
        else:
            return True

    def withdraw(self, amount_spent, description=False):
        """subtracts money, after checking there is enough"""
        if not self.check_funds(amount_spent):
            return False
        if not description:
            description = ''
        self.ledger.append({'amount' : (amount_spent * -1), 'description' : description})
        self.amount -= amount_spent
        return True


    def get_balance(self):
        return self.amount


    def transfer(self, amount_sent, transfer_to):
        funny_thing = transfer_to.category
        if not self.withdraw(amount_sent, f"Transfer to {funny_thing}"):
            return False
        elif not transfer_to.deposit(amount_sent, f"Transfer from {self.category}"):
            return False
        return True

    def __str__(self):
        resultStr = ""
        resultStr+= self.category.center(30, '*')
        resultStr+="\n"
        i = 0
        for line in self.ledger:
            resultStr += f"{self.ledger[i]['description'][0:23]:23}" + \
            f"{self.ledger[i]['amount']:>7.2f} \n"
            i+=1
        resultStr += f"Total: {self.get_balance()}"
        return resultStr


def split_word(str):
  return [char for char in str]
        #     body += items['description'] + (' ' * spaces_between) + f_amount + '\n'
        # message = "Total: {}"
        # total = message.format(self.get_balance())
        # return header + body + total

# now need to add string commands before it'll work!
