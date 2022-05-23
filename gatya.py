class Gatya():
    def Gatyaru(self,menu, budget):
        res = {}
        while budget > 0:
            #print(menu,budget)
            dish, price, budget = self.Select_menue_under_budget(menu,budget)
            if  dish == -1:
                break
            else:
                res[dish] = price
        return res, sum(res.values())
    def Select_menue_under_budget(self,menu,balance):
        import random
        #print(menu,balance)
        tmp = {}
        keys = []
        for dish, price in menu.items():
            if price <= balance:
                tmp[dish] = price
                keys.append(dish)
        if len(tmp) == 0:
            return -1,-1,-1
        rand = random.randint(0,len(keys)-1)
        selected = keys[rand]
        selected_price = tmp[keys[rand]]
        balance -= tmp[keys[rand]]
        #print(selected,selected_price, balance)
        return selected,selected_price, balance
#x = Gatya()
#print(x.Gatyaru(menu,1000))
