from flask import Flask, request, make_response, render_template
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/landing_page')
def landing_page():
   return render_template('landing_page.html')

@app.route('/order_form')
def order_form():
   return render_template('order_form.html')

@app.route('/survet')
def survey():
   return render_template('survey.html')




