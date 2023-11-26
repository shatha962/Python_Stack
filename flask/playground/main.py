from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def play():
    return render_template('index.html', times = 3, color = 'blue')

@app.route('/play/<x>')
def playx(x):
    x=int(x)
    return render_template('index.html', times = x, color = 'blue')

@app.route('/play/<x>/<color>')
def playxcolor(x, color):
    x=int(x)
    return render_template('index.html', times = x, color=color)

if __name__=="__main__":
    app.run(debug=True)