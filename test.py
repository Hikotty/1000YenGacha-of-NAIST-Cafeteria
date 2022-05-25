class Gatya():
    def menize(self,data,target):
        res = {}
        for k,v in data.items():
            res[k] = v[target]
        return res
    def Gatyaru(self,menu, budget):
        res_price = []
        res_manu = []
        while budget > 0:
            #print(menu,budget)
            dish, price, budget = self.Select_menue_under_budget(menu,budget)
            if  dish == -1:
                break
            else:
                res_price.append(price)
                res_manu.append(dish)
        return res_manu,res_price, sum(res_price)
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

import json
with open('data.json','r') as file:
    data = json.load(file)

x = Gatya()
menu = x.menize(data,"値段")
print(x.Gatyaru(menu,1000))
