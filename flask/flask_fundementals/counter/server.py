from flask import Flask, render_template, session, redirect;
app =Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    if "counter" not in session:
        session["counter"] = 0
        return redirect('/')
    session["counter"] +=1
    return render_template('index.html', counter=session["counter"])
@app.route("/destroy", methods=["POST"])
def destroy():
    session.clear()
    return redirect('/')
if __name__=="__main__":
    app.run(debug=True)