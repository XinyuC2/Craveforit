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
@app.route('/finder', methods=['GET', 'POST'])
def finder():
    if request.method =="GET":
        collection=mongo.db.Restaurants
        restaurants=collection.find({})
        return render_template('finder.html', time=datetime.now(), restaurants= [ ])
    else:
        print (request.form)
        collection = mongo.db.Restaurants
        restaurants=collection.find ({ })
        if 'peanut-free' in dict(request.form):
            restaurants = collection.find({'peanut-free':'true'})
        # peanuts = request.form['peanut']
        # shellfish = request.form['shellfish']
        # soy = request.form['soy']
        # lactose = request.form['lactose']
        # vegan = request.form['vegan']
        # gluten = request.form['gluten']
        # kosher = request.form['kosher']
        # peanuts == (collection.find({'peanut': 'true'})) 
        #      list(collection.find({'name', 'hours', 'contact'}))
        # elif shellfish == (collection.find({'shellfish': 'true' })):
        #     list(collection.find({'name', 'hours', 'contact'}))
        # elif soy == (collection.find ({'soy': 'true'})):
        # elif lactose == (collection.find ({'lactose': 'true'})):
        # elif vegan ==  (collection.find ({'vegan': 'true'})):
        # elif gluten ==  (collection.find ({'gluten': 'true'})):
        # elif kosher ==  (collection.find ({'kosher': 'true'})):
            # else:
            #     return (collection.find({ })
    return render_template("finder.html", restaurants=restaurants, time=datetime.now)