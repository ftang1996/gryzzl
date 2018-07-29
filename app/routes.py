from flask import render_template, flash, redirect
from app import app, db
from app.models import Nonprofit, Item
from app.forms import SearchForm


@app.route('/')
@app.route('/index')
def index():
    form = SearchForm()
    if form.validate_on_submit():
        return redirect('/results')

    return render_template('index.html', title='Home', form=form)


@app.route('/nonprofit/<id>')
def nonprofit(id):
    nonprofit = Nonprofit.query.filter_by(id=id).first_or_404()
    items = Item.query.filter_by(nonprofit_id=id)

    return render_template('nonprofit.html', nonprofit=nonprofit, items=items)


@app.route('/results')
def results():
    posts = Nonprofit.query.all()
    return render_template('profile-list.html', posts=posts)


@app.route('/profile-builder')
def profileBuilder():
    return render_template('profile-builder.html')

@app.route('/confirm')
def confirm():
    return render_template('confirmation.html')
