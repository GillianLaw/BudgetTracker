import math
from itertools import zip_longest

class Category():
    """defines the type of expense being tracked"""
    def __init__(self, category):
        self.category = category
        self.ledger = []
        self.amount = 0
        self.spent = 0


    def deposit(self, amount_added, description=False):
        """adds money to that category"""
        if not description:
            description = ''
        self.ledger.append({'amount' : amount_added, 'description' : description})
        self.amount += amount_added
        return self

      # note "amount": amount, "description": description od what has been spent, add to ledger lis
    def check_funds(self, amount_compare):
        """checks account is positive"""
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
        """Transfers money from one category to another"""
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


# def split_word(str):
#   return [char for char in str]


def create_spend_chart(cat_list):
    """This tries to print a graph showing percentage in each category. So far it only half works...
    and I'm coming to the conclusion that maybe it never will. New approach?"""
    answer = ""
    text = ""
    value = 0


    for x in cat_list:
        value = x.amount
        # value should really be total of ALL cats. or should it?

    answer = "Percentage spent by category" + '\n'
    i = 100
    while i >= 0:
        answer += (str(i) + "| ").rjust(5)

        for z in cat_list:
            # value2 = 0
            if z.amount != 0:
                # this is where my problem lies - eveything is showing up as 0
                # Switched to using x.amount, now get 100% for two cats, none for one!
                value2=int(math.floor(((z.amount/value)*100)/ 10.0)) * 10


            if value2 >= 1:
                answer += "o  "
            else:
                answer += "   "
        i = i - 10
        answer += '\n'


    shifted = 3 * (len(cat_list) + 1) + 2

    answer+=("-"*(3*(len(cat_list))+1)).rjust(shifted)+'\n'


    for z in cat_list:
        text += z.category + ' '
    for p in zip_longest(* text.split(), fillvalue=' '):
        # not sure of above
        answer += " " * 5 + '  '.join(p)+'  '+ '\n'

    return answer[:-1]
