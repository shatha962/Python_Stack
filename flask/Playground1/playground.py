from flask import Flask, render_template
from werkzeug.exceptions import HTTPException
app = Flask(__name__)

@app.route('/')
def hello():
    return 'hello'

@app.route('/success/<name>')
def success(name):
    return "hello  " +name

@app.route('/repeat/<num>/<text>')
def repeat(num, text):
    return (text + " " )*int(num)

@app.route('/template')
def template():
    return render_template('index.html')

@app.route('/template1')
def template1():
    return render_template("index1.html", phrase = "shatha", times = 5)

@app.route('/play')
def play():
    return render_template('play.html')

@app.route('/play/<num>')
def playtimes(num):
    return render_template('play1.html', num = int(num))

@app.route('/play/<num>/<color>')
def playtimes_color(num, color):
    return render_template('play2.html', num = int(num), color=color)

@app.errorhandler(Exception)
def handle_exception(e):
    # pass through HTTP errors
    # if isinstance(e, HTTPException):
    #     return e
    # now you're handling non-HTTP exceptions only
    return "Sorry! No response. Try again.", 500
if __name__=="__main__":  
    app.run(debug=True)  