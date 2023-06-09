from flask import Flask, render_template, request

app  =Flask(__name__)

@app.route('/')
def renderForm():
    return render_template("index.html")
@app.route('/result', methods=['POST'])
def process():
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    comment = request.form['comment']
    gender = request.form['gender']
    
    if request.form['done']:
        print(request.form['done'])
        done = request.form['done']
    else: 
        done = True
    
    return render_template("show.html", name=name, location=location, language=language, comment=comment, gender=gender, done=done)
if __name__ == "__main__":
    app.run(debug=True)