class Gatya():
    def menize(self,data,target):
        res = {}
        for k,v in data.items():
            res[k] = v[target]
        return res
    def calorie(self,menu,selected_menu):
        tmp = []
        for dish in selected_menu:
            tmp.append(menu[dish]["カロリー"])
        return tmp,sum(tmp)
    def salt(self,menu,selected_menu):
        tmp = []
        for dish in selected_menu:
            tmp.append(menu[dish]["塩分"])
        return tmp,sum(tmp)
    def carbon(self,menu,selected_menu):
        tmp = []
        for dish in selected_menu:
            tmp.append(menu[dish]["炭水化物"])
        return tmp,sum(tmp)
    def Gatyaru(self,menu, budget):
        res_price = []
        res_manu = []
        while budget > 0:
            dish, price, budget = self.Select_menue_under_budget(menu,budget)
            if  dish == -1:
                break
            else:
                res_price.append(price)
                res_manu.append(dish)
        return res_manu,res_price, sum(res_price)
    def Select_menue_under_budget(self,menu,balance):
        import random
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
        return selected,selected_price, balance