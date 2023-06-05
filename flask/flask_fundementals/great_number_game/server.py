from flask import Flask, render_template, session, redirect, request;
import random
app =Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    if "guess" not in session:
        session["guess"] = random.randint(1,100)
    if "number" not in session:
        session["number"] = 0
        session["attempt"] = 0
    print(session["guess"])
    print(session["number"])
    number = session["number"]
    guess = session["guess"]
    tries = int(session["attempt"])

    return render_template('index.html', guess=guess, number=number, tries=tries)

@app.route('/process', methods=['POST'])
def process():
    session["number"] = int(request.form['number'])
    # session["attempts"] += 1
    return redirect('/')

@app.route('/destroy', methods=['POST'])
def destroy():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)