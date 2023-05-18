import random
from flask import Flask, render_template  

app = Flask(__name__)    

@app.route('/play')          
def hello_world():
    return render_template('index.html')

@app.route('/play/<int:times>')          
def play(times):
    return render_template('index.html', times = times)

@app.route('/play/<int:times>/<color>')          
def playcolor(times, color):
    return render_template('index.html', times = times, color = color)

# create random color for blocks
@app.route('/rand/<int:times>')          
def playcolor1(times):
    color = '#{:02x}{:02x}{:02x}'.format(*random.sample(range(256), 3))
    return render_template('index.html', times = times, color = color)

if __name__=="__main__":   
    app.run(debug=True)    

