from flask import render_template, redirect, request
from peakbagger import app, db
from peakbagger.forms import CreatePost, ChangePost 
from peakbagger.models import Post

## GET the home page
@app.get("/")
def home():
    form = ChangePost()
    posts = Post.query.all()
    return render_template("home.html", posts=posts, form=form)

## GET the create page
@app.get('/post')
def post():
    form = CreatePost()
    return render_template('create.html', form=form)

# POST new post using create form
@app.post("/post")
def new_post():
    form = CreatePost()
    if form.validate_on_submit():
        post = Post(name=form.name.data, notes=form.notes.data, link=form.link.data)
        db.session.add(post)
        db.session.commit() 
        return redirect('/')
    return render_template('create.html', form=form)

## GET the create.html page and load in the db values for that certain ID 
@app.get("/post/<int:post_id>")
def get_post(post_id):
    form = CreatePost()
    post = Post.query.filter_by(id=post_id).first()
    form.name.data = post.name
    form.notes.data = post.notes
    form.link.data = post.link
    return render_template('create.html', form=form)

## Update current ID on create page 
@app.post("/post/<int:post_id>")
def update_post(post_id):
    post = Post.query.filter_by(id=post_id).first()
    form = CreatePost()
    if form.validate_on_submit():
        post.name = form.name.data
        post.notes = form.notes.data
        post.link = form.link.data
        db.session.commit()
        return redirect('/')

## DELETE the selected db ID
@app.delete("/post/<int:post_id>")
def delete_post(post_id):
    post = Post.query.filter_by(id=post_id).first()
    db.session.delete(post)
    db.session.commit()
    return redirect('/')


