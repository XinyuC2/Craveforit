# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask_pymongo import PyMongo
from flask import request, redirect, url_for, session
from datetime import datetime

# -- Initialization section --
app = Flask(__name__)

# name of database
app.config['MONGO_DBNAME'] = 'Crave_for_it'
# os.getenv("NAME_DB") 

# URI of database for read/write provileges
app.config['MONGO_URI'] = 'mongodb+srv://admin2:DqhHmSEzYZodCgXF@cluster0.amcew.mongodb.net/Crave_for_it?retryWrites=true&w=majority'


mongo = PyMongo(app)

# -- Routes section --
# INDEX

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", time = datetime.now())

@app.route('/finder')
def finder():
    # collection=mongo.db.Restaurants
    # # collection.insert_one({'name':'test', 'hours':'test name', 'allergen': 'none'})
    # restaurants=collection.find({})
    # print(restaurants)
    return render_template("finder.html", time=datetime.now(), restaurants = restaurants)

   
@app.route('/getinfo', methods=['GET', 'POST'])
def info():
    if request.method == 'GET':
        collection = mongo.db.Restaurants
        collection.find({ )}
        return render_template("finder.html", collection=list(collection), time=datetime.now)
    else:
        peanuts = request.form["peanuts"]
        shellfish = request.form["shellfish"]
        lactose = request.form["lactose"]



# Adding entries to MongoDB
# @app.route('/add')
# def add():
#     # define a variable for the collection you want to connect to
#     collection = mongo.db.Restaurants
    #collection.insert({"song":"Row, Row, Row Your Boat"})mydb = myclient["mydatabase"]
    # mylist = [
    #     { "title": "Amy", "artist": "Coldplay", "comment": "provilegesretty"},
    #     { "title": "Hannah", "artist": "Mumford and Sons", "comment": "soothing"},
    #     { "title": "Michael", "artist": "Mumford and Sons", "comment": "happy"},
    #     { "title": "Sandy", "artist": "Coldplay", "comment": "mellow"},
    #     { "title": "Betty", "artist": "Blue October", "comment": "pretty"},
    #     { "title": "Richard", "artist": "Blue October", "comment": "happy"},
    #     { "title": "Susan", "artist": "Coldplay", "comment": "happy"},
    #     { "title": "Vicky", "artist": "Blue October", "comment": "soothing"},
    #     { "title": "Ben", "artist": "Elton John", "comment": "fave"},
    #     { "title": "William", "artist": "Elton John", "comment": "happy"},
    #     { "title": "Chuck", "artist": "Mumford and Sons", "comment": "pretty"},
    #     { "title": "Viola", "artist": "Mumford and Sons", "comment": "mellow"}
    #     ]
    # collection.insert_many(mylist)
    # return redirect(url_for('display_main')) 


