from flask import Flask, render_template, Response, request, jsonify, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return(render_template("index.html", toggle_help=False))

@app.route('/question1')
def question1():
    return(render_template("question1.html", toggle_help=True))

@app.route('/question2')
def question2():
    return(render_template("question2.html", toggle_help=True))

@app.route('/question3')
def question3():
    return(render_template("question3.html", toggle_help=True))

@app.route('/question4')
def question4():
    return(render_template("question4.html", toggle_help=True))

@app.route('/question5')
def question5():
    return(render_template("question5.html", toggle_help=True))

@app.route('/question6')
def question6():
    return(render_template("question6.html", toggle_help=True))

@app.route('/question7')
def question7():
    return(render_template("question7.html", toggle_help=True))

@app.route('/review')
def review():
    return(render_template("review.html", toggle_help=True))

@app.route('/success')
def success():
    return(render_template("success.html", toggle_help=True))

if __name__ == '__main__':

    app.run(debug = True)
