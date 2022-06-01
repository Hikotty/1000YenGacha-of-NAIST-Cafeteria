class Optimize():
    def return_result(self,menu):
        selected_menu = []
        selected_price = []
        selected_calorie = []
        selected_calorie_sum = 0
        selected_salt = []
        selected_salt_sum = 0
        selected_carbon = []
        selected_carbon_sum = 0
        for k,v in menu.items():
            selected_menu.append(k)
            selected_price.append(v['値段'])
            selected_calorie.append(v['カロリー'])
            selected_salt.append(v['塩分'])
            selected_carbon.append(v['炭水化物'])
        res = [selected_menu,
               selected_price,
               selected_calorie,
               selected_salt,
               selected_carbon]
        return res

 