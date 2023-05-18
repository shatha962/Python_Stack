from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return render_template('index.html',phrase="hello", times=5)
@app.route('/dojo')
def hello_dojo():
    return "Dojo!"
@app.route('/say/<name>')
def hi_name(name):
    return f"Hi {name}!"
@app.route('/repeat/<number>/<word>')
def repeat(number, word):
    return f"{word} -" * int(number)
@app.route("/repeat1/<int:number>/<word>")
def repeat1(number, word):
    return f"{word} -" * number
  # Return the string 'Hello World!' as a response
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

