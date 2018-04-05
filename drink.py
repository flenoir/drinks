#! /usr/bin/python
# -*- coding:utf-8 -*-

from flask import Flask, render_template,request
app = Flask(__name__)


# vitesse elimination alcool
# Homme : 0,10g/L à 0,15g/L par heure,
# Femme : 0,085g/L à 0,10g/L par heure.

bar = {
    "small_beer" : ["small_beer", 25, 6],
    "medium_beer" : ["medium_beer", 33, 6],
    "large_beer" : ["large_beer", 50, 6],
    "small_wine" : ["small_wine",12, 12],
    "medium_wine" : ["medium_wine",25, 12],
    "large_wine" : ["large_wine",33, 12],
    "small_water" : ["small_water",33, 0],
    "medium_water" : ["medium_water",50, 0],
    "large_water" : ["large_water",100, 0]
}

class Drink:
    """
    Drink class
    """
    # Man and woman alcool diffusion coefficient
    man_diff = 0.6
    woman_diff = 0.7

    def __init__(self, name, volume, alcool_degree=0, sugar=0):
        self.name = name
        self.volume = volume
        self.alcool_degree = alcool_degree
        self.sugar = sugar

class User:
    """
    Users class
    """

    # Man and woman alcool diffusion coefficient
    man_diff = 0.6
    woman_diff = 0.7

    def __init__(self, firstname, lastname, gender, age, height, weight):
        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender
        self.age = age
        self.height = height
        self.weight = weight
        self.todays_drinks = []

    def add_drink(self, beverage):
        self.newDrink = Drink(beverage[0],beverage[1],beverage[2])
        self.todays_drinks.append(self.newDrink)
        return self.todays_drinks

    def drinks_today(self):
        return len(self.todays_drinks)

    def volume_today(self):
        return sum([int(x.volume) for x in self.todays_drinks])
    
    def alcool_today(self):
        for x in self.todays_drinks:
            total_alcool_degree_today = sum(x.alcool_degree for x in self.todays_drinks)
            alcool_rate = (8 * total_alcool_degree_today * self.volume_today()) / 100
            # calcul alcoolémie => (g) ÷ [ Poids (kg) x le coefficient de diffusion
            alcolemie = round((alcool_rate / (64 * self.man_diff)), 2)
            next_hour = round(alcolemie - 0.10, 2)
        return alcolemie


@app.route('/')
def index():
    customer1 = User("Mike", "Stevenson", "M", 34, 175, 70)

    print(customer1.lastname, customer1.todays_drinks)
    # customer1.add_drink(bar["medium_beer"])
    # res = customer1.add_drink(bar["large_wine"])

    # print(customer1.lastname, "drinked",customer1.drinks_today(), "drinks", customer1.todays_drinks[0].name, "and", customer1.todays_drinks[1].name, "for a total volume of", customer1.volume_today(), "cl for an alcool rate of", customer1.alcool_today())
    # return "<h1>{} drinked {} drinks, a {} and a {} for a total volume of {} cl and for an alcool rate of {}</h1>".format(customer1.lastname,customer1.drinks_today(),customer1.todays_drinks[0].name, customer1.todays_drinks[1].name, customer1.volume_today(), customer1.alcool_today())
  
    # mot =  "{} drinked {} drinks, a {} and a {} for a total volume of {} cl and for an alcool rate of {}".format(customer1.lastname,customer1.drinks_today(),customer1.todays_drinks[0].name, customer1.todays_drinks[1].name, customer1.volume_today(), customer1.alcool_today())
  
    return render_template('adddrink.html')

@app.route('/adddrink', methods=['GET', 'POST'])
def adddrink():
    customer1 = User("Mike", "Stevenson", "M", 34, 175, 70)
    if request.method == 'POST':
        for i in request.form:
            if request.form[i] != "":
                print(i,request.form[i])
                customer1.add_drink(bar[request.form[i]])
            else:
                print("empty")

        # customer1.add_drink(bar[request.form['pouet']])
        result = request.form
        # print(request.form)
        mot = "{} drinked {} drinks, a {} for a total volume of {} cl and for an alcool rate of {}".format(customer1.lastname,customer1.drinks_today(),customer1.todays_drinks[0].name, customer1.volume_today(), customer1.alcool_today())
        return render_template("allbeverages.html",result=result, mot=mot)
    
@app.route('/customer',methods=['GET','POST'])
def customer():
    return render_template("customer.html")

if __name__ == '__main__':
    app.run(debug=True)