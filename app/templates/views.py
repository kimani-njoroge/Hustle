from flask import render_template,request,redirect,url_for,abort
from . import main
from flask_login import login_required,current_user
from forms import PostBidForm

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    title = 'Home'

    return render_template('index.html', title = title )


@main.route('/postjob/<int:id>')
@login_required
def post_job(id):

    '''
    View root page function that returns the index page and its data
    '''

    title = 'Home'

    return render_template('postjob.html', title = title )


@main.route('/postbid/<int:id>')
def post_bid(id):
    '''
    View root page function that returns the index page and its data
    '''
    bid_form = PostBidForm()
    if bid_form.validate_on_submit():
        bid = Bids(description = form.description.data, cost = form.cost.data)
        db.session.add(bid)
        db.session.commit()
        return redirect(url_for('auth.login'))
    title = 'Home'

    return render_template('postbid.html', title = title, bid_form = bid_form )
