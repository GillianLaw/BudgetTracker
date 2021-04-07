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


def create_spend_chart(cat_list):
    answer = ""
    text = ""
    value = 0

    for x in cat_list:
        value += x.spent

    answer = "Percentage spent by category" + '\n'
    i = 100
    while i >= 0:
        answer += (str(i) + "| ").rjust(5)

        for x in cat_list:
            value2 = 0
            if x.spent != 0:
                # value2 = int(math.floor(((x.spent/value) * 100)/ 10.0)) * 10
                value2=int(math.floor(((x.spent/value)*100)/ 10.0)) * 10
            if value2 >= 1:
                answer += "o  "
            else:
                answer += "   "

        i = i - 10
        answer += '\n'

    shifted = 3 * (len(cat_list) + 1) + 2
    # answer += ("-" * (3 * (len(cat_list)) + 1).r.just(shifted) + '\n'
    answer+=("-"*(3*(len(cat_list))+1)).rjust(shifted)+'\n'


    for z in cat_list:
        text += z.category + ' '
    for p in zip_longest(* text.split(), fillvalue=' '):
        # not sure of above
        answer += " " * 5 + '  '.join(p)+'  '+ '\n'

    return answer[:-1]










# def create_spend_chart(arg):
#     print("Percentage spent by category")
#     num = len(arg)
#     totalSpent = 0
#     wordList = []
#     for item in range(num):
#         wordList.append(list(arg[item].category))
#         totalSpent += arg[item].spent
#
#     pctList = []
#     for item in range(num):
#         if totalSpent >= 1:
#             pctList.append(math.floor(arg[item].spent/totalSpent * 10))
#             ht = 10
#             while ht >= 0:
#                 print(f"{(ht*10):3d}| ", end = "")
#                 for p in range(num):
#                     if pctList[p-1] >= ht:
#                         print("o  ",end ="")
#                     else:
#                         print("",end="   ")
#                 print()
#                 ht -= 1
#             print(" "*4+"-"*(num*3+1))#bottom axis
#
#         l= len(max(wordList, key=len))
#         x=0
#         while x < l:
#             print("     ",end="")
#             i=0
#             while i < num:
#                 try:
#                     print(wordList[i][x],end = "  ")
#                 except IndexError:
#                     print("   ", end="")
#                 i+=1
#             print("")
#             x+=1
#         return





# now need to add string commands before it'll work!
