from flask import Flask, render_template


app = Flask(__name__)



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

