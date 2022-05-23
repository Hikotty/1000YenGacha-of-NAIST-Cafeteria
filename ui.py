from flask import Flask, render_template
import gatya
import json
app = Flask(__name__)

with open('data.json','r') as file:
    menu = json.load(file)

@app.route('/')
def main():
    return render_template("index.html")

@app.route('/result')
def result():
    x = gatya.Gatya()
    selected = x.Gatyaru(menu,1000)
    #print(selected)
    selected,Sum = selected[0],selected[1]
    print(type(selected))
    return render_template("result.html",selected=selected,Sum=Sum)

if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost')