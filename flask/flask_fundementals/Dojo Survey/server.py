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

    print(request.form['comment'])
    done = request.form['done']
    
    return render_template("show.html", name=name, location=location, language=language, comment=comment, gender=gender, done=done)
if __name__ == "__main__":
    app.run(debug=True)