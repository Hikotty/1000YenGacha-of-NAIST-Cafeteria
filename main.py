menu = {"日替定食":510,"アラカルト丼":380,"アラカルト丼（大盛り）":440,
        "親子丼":370,"親子丼（大盛り）":430,
        "玉子丼":310,"玉子丼（大盛り）":370,
        "月見うどん":250,"月見うどん（大盛り）":310,
        "カツ丼":420,"カツ丼（大盛り）":480,
        "カレーライス":370,"カレーライス（大盛り）":430,
        "カツカレー":470,"カツカレー（大盛り）":530,
        "チャーハン":320,"チャーハン（大盛り）":420,
        "かけうどん":200,"かけうどん（大盛り）":300,
        "かけそば":200,"かけそば（大盛り）":300,
        "きつねうどん":250,"きつねうどん（大盛り）":350,
        "きつねそば":250,"きつねそば（大盛り）":350,
        "カレーうどん":370,"カレーうどん（大盛り）":470,
        "ラーメン":310,"ラーメン（大盛り）":410,
        "納豆":100,"卵":50,"味噌汁":50,
        "ライス（中）":150,"ライス（小）":100,"漬物":50}
        
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
x = Gatya()
print(x.Gatyaru(menu,1000))
