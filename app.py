from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/tracker")
def about(name=None):
    return render_template('traker.html', name=name) 

if __name__ == "__main__":
    app.run(debug=True)
