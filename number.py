from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'key'

@app.route('/')
def index():
    
    if 'number' in session:
        session['number'] = session['number']
    else:
        session['number'] = random.randrange(1,101)

    print session['number']
    return render_template("root.html", res = session['res'])
    


@app.route('/submit', methods=["POST"])
def check():
    
    guessednum = int(request.form["entry"])

    if guessednum < session["number"]:
        session['res'] = "you guessed too low"
    elif guessednum > session["number"]:
        session['res'] = "you guessed too high"
    elif guessednum == session["number"]:
        session['res'] = "you are correct!"
        session['number'] = random.randrange(1,101)


    return redirect('/')







app.run(debug=True) # run our server