from flask import render_template, request, redirect, url_for, abort, send_file
import secrets
import os
from . import main
from flask_login import login_required, current_user
from .forms import PostBidForm, PostJobForm, ReviewsForm, UpdateAccountForm, DownloadKeyForm, AddCategoriesForm
from ..models import Bids, Jobs, Reviews, User, FileContents, Acceptbids
from app import db
from manage import app
from io import BytesIO

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
<<<<<<< HEAD
    '''
=======
    """
    job_form = PostJobForm()

    title = 'Post a job'
    if job_form.validate_on_submit():
        jobs = Jobs(title=job_form.title.data, description=job_form.description.data, duration=job_form.duration.data,
                    technologies=job_form.technologies.data, category=job_form.category.data, user=current_user)
        db.session.add(jobs)
        db.session.commit()
        return redirect(url_for('main.index'))
>>>>>>> a4d7ff321f0a724bd9b481f174839e2b8dda38bf

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
<<<<<<< HEAD
        return redirect(url_for('auth.login'))
    title = 'Home'
=======
        return redirect(url_for('main.view_job', jobs_id=jobs_id))
    title = 'Post a bid'
    bids = Bids.query.filter_by(jobs_id=jobs_id).all()

    return render_template('job.html', title=title, bid_form=bid_form, job=job, bids=bids)


@main.route('/jobs/<string:category>', methods=['GET', 'POST'])
def view_jobs(category):
    jobs = Jobs.query.filter_by(category=category)
    return render_template('jobs.html', jobs=jobs)
>>>>>>> a4d7ff321f0a724bd9b481f174839e2b8dda38bf

    return render_template('postbid.html', title = title, bid_form = bid_form )


@main.route("/accept/<int:bids_id>/<int:user_id>", methods=['GET', 'POST'])
def accept(bids_id, id):
    accepted_bid = Acceptbids(accepted_bid=bids_id, user=current_user, jobs_id=id)
    db.session.add(accepted_bid)
    db.session.commit()
    return '<h1>Bid accepted</h1><a href="/">Go back home</a>'


@main.route("/accepted")
def show_accept():
    bids = Acceptbids.query.all()
    return render_template("accepted.html", bids=bids)


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


@main.route('/user', methods=['GET', 'POST'])
def profile():
    form = SetUpAccountForm()
    if form.validate_on_submit():
        profile = Profile(bio=form.bio.data, cows=form.cows.data, user=current_user)
        db.session.add(profile)
        db.session.commit()

    return render_template('profile/profile.html',form=form)




@main.route("/uploader")
def show_uploader():
    return render_template('upload.html')


@main.route("/upload", methods=['POST', 'GET'])
def upload():
    file = request.files['inputFile']
    new_file = FileContents(name=file.filename, data=file.read())
    db.session.add(new_file)
    db.session.commit()

    return "Succesfully uploaded " + file.filename + " Your secret key is " + str(new_file.id)


@main.route('/download', methods=['GET', 'POST'])
def download_key():
    form = DownloadKeyForm()
    if form.validate_on_submit():
        key = form.download_key.data
        file_data = FileContents.query.filter_by(id=key).first()
        return send_file(BytesIO(file_data.data), attachment_filename='download', as_attachment=True)
    return render_template('download.html', form=form)

@main.route('/addcategory', methods=['GET', 'POST'])
def add_category():
    form = AddCategoriesForm()
    if form.validate_on_submit():
        Categories = Categories(name=form.Category.data, jobs_id=jobs.id)
        db.session.add(Categories)
        db.session.commit()
        return redirect(url_for('.index'))
    title = 'Categories'



@main.route('/job/<int:jobs_id>', methods=['GET', 'POST'])
def view_job(jobs_id):
   """
   View root page function that returns the index page and its data
   """
   job = Jobs.query.get_or_404(jobs_id)
   bid_form = PostBidForm()
   if bid_form.validate_on_submit():
       bid = Bids(description=bid_form.description.data, cost=bid_form.cost.data, user=current_user, jobs_id=job.id)
       db.session.add(bid)
       db.session.commit()
       return redirect(url_for('main.view_job', jobs_id=jobs_id))
   title = 'Post a bid'
   bids = Bids.query.filter_by(jobs_id=jobs_id).all()

   return render_template('job.html', title=title, bid_form=bid_form, job=job, bids=bids)


@main.route('/jobs', methods=['GET', 'POST'])
def view_jobs():
   jobs = Jobs.query.all()
   return render_template('jobs.html', jobs=jobs)
