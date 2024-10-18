from flask import Flask, render_template,request, flash
from threading import Thread
import requests
import random
api = "http://api.quotable.io/random"
quotes = []


app = Flask(__name__)
app.secret_key = "hnguyen"
@app.route('/hello')

def index():
    
    flash("Welcome to A Quote A Day! What's your name? ")
    return render_template("index.html")

@app.route('/greet',methods=['POST','GET'])
def greet():
    #catch/fetch an input from user, which is a name
    name = request.form.get('name_input')
    quote = get_rand_quote()
    flash("Hi, "+ str(name)  + "! \nHere is a quote for you: "  + str(quote)) 
    return render_template("index.html")

def preload_quotes():
    global quotes
    for i in range(10):
        #pick a random quote
        rand_quote = requests.get(api).json()
        content = rand_quote['content']
        author = rand_quote['author']
        quote = content  + "\n(By " + author + ")."
        quotes.append(quote)
    return quotes
        
def get_rand_quote():
    quotes = preload_quotes()
    rand_num = random.randint(0,len(quotes))
    return quotes[rand_num]
if __name__=='__main__':
    app.run(port=5000)