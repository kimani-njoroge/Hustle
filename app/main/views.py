import profile

from flask import render_template, request, redirect, url_for, abort
import secrets
import os
from . import main
from flask_login import login_required, current_user
from .forms import PostBidForm, PostJobForm, ReviewsForm, UpdateAccountForm
from ..models import Bids, Jobs, Reviews, User
from app import db
from manage import app

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    title = 'Home'

    return render_template('index.html', title = title )


@main.route('/postjob', methods=['GET', 'POST'])
@login_required
def post_job():
    if current_user.role != 'client':
        abort(403)
    '''
    View root page function that returns the index page and its data
    '''

    title = 'Home'

    return render_template('postjob.html', title = title )


@main.route('/postbid/<int:id>', methods=['GET', 'POST'])
def post_bid(id):
    '''
    View root page function that returns the index page and its data
    '''
    bid_form = PostBidForm()
    if bid_form.validate_on_submit():
        bid = Bids(description = bid_form.description.data, cost = bid_form.cost.data, user=current_user)
        db.session.add(bid)
        db.session.commit()
        return redirect(url_for('auth.login'))
    title = 'Home'

    return render_template('postbid.html', title = title, bid_form = bid_form )


@main.route('/reviews', methods=['GET', 'POST'])
def reviews():
    '''
    View root page function that returns the reviews page and its data
    '''
    form = ReviewsForm()
    if form.validate_on_submit():
        reviews = Reviews(description = form.description.data, scale = form.scale.data)
        db.session.add(reviews)
        db.session.commit()
        return redirect(url_for('main.reviews'))
    title = 'Reviews'
    return render_template('reviews.html', title = title ,form_reviews = form)

@main.route("/bid/<int:bids_id>", methods=['GET', 'POST'])
def bid(bids_id):
    bid = Bids.query.get_or_404(bids_id)
    return render_template('bid.html', title='Comment', bid=bid)

@main.route('/reviews', methods=['GET', 'POST'])
def reviews():
    '''
    View root page function that returns the reviews page and its data
    '''
    form = ReviewsForm()
    if form.validate_on_submit():
        reviews = Reviews(description = form.description.data, scale = form.scale.data)
        db.session.add(reviews)
        db.session.commit()
        return redirect(url_for('main.reviews'))
    title = 'Reviews'

    return render_template('reviews.html', title = title ,form_reviews = form)

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile/', picture_fn)
    form_picture.save(picture_path)
    current_user.image_file = picture_fn
    image_file = url_for('static', filename='profile/' + current_user.image_file)


@main.route("/user", methods=['GET', 'POST'])
@login_required
def profile():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)

        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        return redirect(url_for('main.profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename='profile/' + current_user.image_file)
    return render_template('profile/profile.html', title='Account', image_file=image_file, form=form)


@main.route("/user/<int:user_id>", methods=['GET'])
def view_account(user_id):
    user = User.query.get_or_404(user_id)
    image_file = url_for('static', filename='profile/' + user.image_file)
    return render_template('profile/display_profile.html', user=user, image_file=image_file)

