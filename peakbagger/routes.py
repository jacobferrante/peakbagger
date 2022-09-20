from crypt import methods
from flask import render_template, redirect
from peakbagger import app, db
from peakbagger.forms import CreateHike, UpdateHike
from peakbagger.models import Hike

## Home Route
@app.route("/", methods=["GET"])
@app.route ("/hike", methods=["GET"])
def home():
    hikes = Hike.query.all()
    return render_template("home.html", hikes=hikes)

# Create hikes using request form
@app.route("/hike/create", methods=['GET', 'POST'])
def hike():
    form = CreateHike()
    if form.validate_on_submit():
        post = Hike(name=form.name.data, notes=form.notes.data, link=form.link.data)
        db.session.add(post)
        db.session.commit()
        return redirect('/')
    return render_template('create.html', form=form)

## Delete the hike
@app.route("/hike/delete/<int:hike_id>", methods=['POST'])
def delete(hike_id):
    hike = Hike.query.filter_by(id=hike_id).first()
    db.session.delete(hike)
    db.session.commit()
    return redirect('/')

# Update the hike
@app.route("/hike/update/<int:hike_id>", methods=['GET, POST'])
def update(hike_id):
    hike = Hike.query.filter_by(id=hike_id).first()
    form = UpdateHike()
    if form.validate_on_submit(): 
        hike.name = form.name.data 
        hike.notes = form.notes.data
        hike.link = form.link.data
        db.session.commit()
        return redirect('/')
    return render_template('create.html', form=form)

