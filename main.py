from flask import Flask, render_template
import gatya
import optimization
import json
from pathlib import Path

from test import optimazation
app = Flask(__name__)

with open('data.json','r') as file:
    data = json.load(file)

with open('photo_data.json','r') as file:
    photo_names = json.load(file)

with open('maxcal_data.json','r') as file:
    maxcal_menu = json.load(file)

budget = 1000
DIR = "./static/images/"

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
    selected_photos = []
    for i in selected_menu:
        selected_photos.append(DIR+photo_names[i])
    return render_template("result.html",
        selected_menu=selected_menu,
        selected_price=selected_price,Sum=Sum,n=n,
        selected_calorie=selected_calorie,
        selected_calorie_sum=round(selected_calorie_sum,2),
        selected_salt=selected_salt,
        selected_salt_sum=round(selected_salt_sum,2),
        selected_carbon=selected_carbon,
        selected_carbon_sum=round(selected_carbon_sum,2),
        selected_photos=selected_photos)

@app.route('/maxcal')
def maxcal():
    opt_obj = optimization.Optimize()
    res = opt_obj.return_result(maxcal_menu)
    selected_menu,selected_price,selected_calorie,selected_salt,selected_carbon = res[0],res[1],res[2],res[3],res[4]
    Sum = sum(selected_price)
    selected_calorie_sum = sum(selected_calorie)
    selected_salt_sum = sum(selected_salt)
    selected_carbon_sum = sum(selected_carbon)
    n = len(selected_price)

    selected_photos = []
    for i in selected_menu:
        selected_photos.append(DIR+photo_names[i])

    return render_template("result.html",
        selected_menu=selected_menu,
        selected_price=selected_price,Sum=Sum,n=n,
        selected_calorie=selected_calorie,
        selected_calorie_sum=round(selected_calorie_sum,2),
        selected_salt=selected_salt,
        selected_salt_sum=round(selected_salt_sum,2),
        selected_carbon=selected_carbon,
        selected_carbon_sum=round(selected_carbon_sum,2),
        selected_photos=selected_photos)

@app.route('/notes')
def notes():
    return render_template("notes.html")

if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost')