from flask import Flask, render_template, redirect, session, flash, url_for
from flask_sqlalchemy import SQLAlchemy
import os
from forms import ProfileForm, SearchForm, DeleteForm
# from model import Profile



app = Flask(__name__)
app.config['SECRET_KEY'] = '48a89ef0b9a63e63dc8a5ca21fc1871d'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.app_context().push()
db = SQLAlchemy(app)



class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String, nullable=False)
    hobby = db.Column(db.String, nullable=False)



@app.route("/", methods=["GET","POST"])
def index():
    prof = Profile.query.all()
    form = SearchForm()
    
    names = []
    emails = []
    if form.validate_on_submit():
        search = form.search.data
        names = Profile.query.filter_by(name=search.title()).all()
        emails = Profile.query.filter_by(email=search).all()
        if search not in names and search not in emails:
            message = ('"'+search+'"' + " not found")
        return render_template("search.html", form=form, namez=names, emailz=emails, message=message)
    return render_template("home.html", profile=prof, form=form, title="Home")


@app.route("/reg_prof", methods=["GET","POST"])
def register():
    profile = ProfileForm()
    if profile.validate_on_submit():
        profile_db = Profile(name = profile.name.data.title(),
                             email = profile.email.data,
                             age = profile.age.data,
                             gender = profile.gender.data,
                             hobby = profile.hobby.data)
        flash("Details registered successfully")
        db.session.add(profile_db)
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("register.html", form=profile, title="Register")


@app.route("/profile/<int:profile_id>", methods=["GET","POST"])
def profile(profile_id):
    form = DeleteForm()
    prof = Profile.query.get(profile_id)
    if form.validate_on_submit():
        db.session.delete(prof)
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("profile_detail.html", profile=prof, form=form)


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)    