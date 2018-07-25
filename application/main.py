from flask import Flask, render_template
from flask_pymongo import PyMongo
import json

app = Flask(__name__)
app.config["MONGO_URI"]="mongodb://localhost:27017/davinciDb"

mongo = PyMongo(app)

@app.route('/')
@app.route('/dashboard')
def dashboard():
    notification = False
    return render_template('dashboard/test.html',notification = notification)



@app.route('/table')
def table():
    notification = False
    return render_template('dashboard/table.html',notification = notification)




@app.route('/form')
def form():
    notification = True
    return render_template('dashboard/forms.html',notification = notification,item_title='Account')





@app.route('/records')
def records():
    notification = True
    return render_template('dashboard/records_counter.html')


@app.route('/db')
def dbtest():
    test = mongo.db.Account.find()
    return str(test[0])
