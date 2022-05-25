from flask import Flask, render_template
import gatya
import json
app = Flask(__name__)

with open('data.json','r') as file:
    data = json.load(file)

budget = 1000

@app.route('/')
def main():
    return render_template("index.html")

@app.route('/result')
def result():
    gatya_obj = gatya.Gatya()
    menu = gatya_obj.menize(data,"値段")
    selected = gatya_obj.Gatyaru(menu,budget)
    selected_menu,selected_price,Sum = selected[0],selected[1],selected[2]
    selected_calorie,selected_calorie_sum = gatya_obj.calorie(data,selected_menu)
    selected_salt,selected_salt_sum = gatya_obj.salt(data,selected_menu)
    selected_carbon,selected_carbon_sum = gatya_obj.carbon(data,selected_menu)
    n = len(selected_menu)
    return render_template("result.html",selected_manu=selected_menu,
        selected_price=selected_price,Sum=Sum,n=n,
        selected_calorie=selected_calorie,
        selected_calorie_sum=round(selected_calorie_sum,2),
        selected_salt=selected_salt,
        selected_salt_sum=round(selected_salt_sum,2),
        selected_carbon=selected_carbon,
        selected_carbon_sum=round(selected_carbon_sum,2))

@app.route('/notes')
def notes():
    return render_template("notes.html")

if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost')