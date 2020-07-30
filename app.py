# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
<<<<<<< josephineII
from flask import render_template
from flask_pymongo import PyMongo
from flask import request, redirect, url_for, session
from datetime import datetime
=======
#from flask import render_template
# from flask import request
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
