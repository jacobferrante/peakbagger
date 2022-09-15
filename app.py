from crypt import methods
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

## DATABASE SETUP
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///db.sqlite'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False 
db = SQLAlchemy(app)


## Class for saving hikes, including ID, name, general info, date and optiont to save link for strava
class Hike(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    notes = db.Column(db.String(100), nullable=False)
    link = db.Column(db.String(100), nullable=True)

# Create hikes using request form
@app.route("/hikes", methods=["POST"])
def add():
    name = request.form.get("name")
    notes = request.form.get("notes")
    link = request.form.get("link")
    new_hike = Hike(name=name, notes=notes, link=link)
    db.session.add(new_hike)
    db.session.commit() 
    return redirect(url_for("home"))

## Need to finish this and add update
@app.route("/hikes/<int:hike_id>", methods=["PUT"])
def update(hike_id):
    hike = Hike.query.filter_by(id=hike_id).first()


@app.route("/hikes/<int:hike_id>", methods=["DELETE"])
def delete(hike_id):
    hike = Hike.query.filter_by(id=hike_id).first()
    db.session.delete(hike)
    db.session.commit()
    return redirect(url_for("home"))

@app.route("/", methods=["GET"])
def home():
    hikes = Hike.query.all()
    return render_template("base.html", hikes=hikes)

if __name__ == "__main__":
    db.create_all() 
    app.run(debug=True)
    