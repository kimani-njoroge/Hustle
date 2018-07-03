from flask import render_template,request,redirect,url_for,abort
from . import main
from flask_login import login_required,current_user
from . forms import PostBidForm
from .. models import Bids
from app import db

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    title = 'Home'

    return render_template('index.html', title = title )


@main.route('/postjob/<int:id>')
def post_job(id):

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


@main.route('/reviews/<int:id>')
def reviews(id):

    '''
    View root page function that returns the reviews page and its data
    '''

    title = 'Reviews'

    return render_template('reviews.html', title = title )
