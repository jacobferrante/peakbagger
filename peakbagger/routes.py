from flask import render_template, redirect, request
from peakbagger import app, db
from peakbagger.forms import CreateHike 
from peakbagger.models import Hike


## GET the home page
@app.get("/")
def home():
    hikes = Hike.query.all()
    return render_template("home.html", hikes=hikes)

## GET the create page
@app.get('/hike')
def hike():
    form = CreateHike()
    return render_template('create.html', form=form)

@app.get('/hike')
def hike_search():
    hikes = Hike.query.all()
    return render_template("home.html", hikes=hikes)

# POST new hike using create form
@app.post("/hike")
def new_hike():
    form = CreateHike()
    if form.validate_on_submit():
        post = Hike(name=form.name.data, notes=form.notes.data, link=form.link.data)
        db.session.add(post)
        db.session.commit() 
        return redirect('/')
    return render_template('create.html', form=form)

## DELETE the selected db ID
@app.delete("/hike/<int:hike_id>")
def delete_hike(hike_id):
    hike = Hike.query.filter_by(id=hike_id).first()
    db.session.delete(hike)
    db.session.commit()
    return redirect('/')

## GET the create.html page and load in the db values for that certain ID 
@app.get("/hike/<int:hike_id>")
def get_hike(hike_id):
    form = CreateHike()
    hike = Hike.query.filter_by(id=hike_id).first()
    form.name.data = hike.name
    form.notes.data = hike.notes
    form.link.data = hike.link
    return render_template('update.html', form=form)

## PUT the new DB values on the create page
@app.put("/hike/<int:hike_id>")
def update_hike(hike_id):
    hike = Hike.query.filter_by(id=hike_id).first()
    form = CreateHike()
    if form.validate_on_submit():
        hike.name = form.name.data
        hike.notes = form.notes.data
        hike.link = form.link.data
        db.session.commit()
        return redirect('/')

