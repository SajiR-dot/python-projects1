from flask import Flask, render_template,redirect,url_for,request
import requests



app = Flask(__name__)


@app.route('/',methods =['POST','GET'])
def home():
    if request.method =="POST":
        return redirect(url_for("get_quote"))
    return render_template("home.html")
    



@app.route('/quote')
def get_quote():
    url =  'https://api.kanye.rest'
    response = requests.get(url)
    data = response.json()
    print(data)
    quote = data["quote"]
    
    return render_template("quote.html",quotes = quote)



if __name__ == '__main__':
    app.run(debug=True)




