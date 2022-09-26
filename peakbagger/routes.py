from flask import render_template, redirect, request
from peakbagger import app, db
from peakbagger.forms import CreateHike 
from peakbagger.models import Hike

## Home Route
@app.get("/")
def home():
    hikes = Hike.query.all()
    return render_template("home.html", hikes=hikes)

@app.get('/hike')
def hike():
    form = CreateHike()
    return render_template('create.html', form=form)

# Create hikes using request form
@app.post("/hike")
def new_hike():
    form = CreateHike()
    if form.validate_on_submit():
        post = Hike(name=form.name.data, notes=form.notes.data, link=form.link.data)
        db.session.add(post)
        db.session.commit() 
        return redirect('/')
    return render_template('create.html', form=form)

# Update the hike

## Delete the hike
@app.delete("/hike/<int:hike_id>")
def delete(hike_id):
    hike = Hike.query.filter_by(id=hike_id).first()
    db.session.delete(hike)
    db.session.commit()
    return redirect('/')


#@app.put("/hike/<int:hike_id>") 
#def update(hike_id):
#    hike = Hike.query.filter_by(id=hike_id).first()
#    form = CreateHike()
#    ## Ask for user input to update hike
#    if form.validate_on_submit():
#        hike.name = form.name.data
#        hike.notes = form.notes.data
#        hike.link = form.link.data
#        db.session.commit()
#        return redirect('/')
#    ## Populate form with the current database info for that item
#    elif request.method == 'GET':
#        form.name.data = hike.name
#        form.notes.data = hike.notes
#        form.link.data = hike.link
#    return render_template('create.html', form=form)
