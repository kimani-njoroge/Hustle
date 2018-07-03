from flask import render_template, request, redirect, url_for, abort
import secrets
import os
from . import main
from flask_login import login_required, current_user
from .forms import PostBidForm, PostJobForm,SetUpAccountForm
from ..models import Bids, Jobs,Profile
from app import db
from manage import app


@main.route('/')
def index():
    """
    View root page function that returns the index page and its data
    """

    title = 'Home'

    return render_template('index.html', title=title)


@main.route('/postjob', methods=['GET', 'POST'])
@login_required
def post_job():
    if current_user.role != 'client':
        abort(403)
    """
    View root page function that returns the index page and its data
    """
    job_form = PostJobForm()

    title = 'Post a job'
    if job_form.validate_on_submit():
        jobs = Jobs(title=job_form.title.data, description=job_form.description.data, duration=job_form.duration.data,
                    technologies=job_form.technologies.data, user=current_user)
        db.session.add(jobs)
        db.session.commit()
        return redirect(url_for('main.index'))

    return render_template('postjob.html', title=title, job_form=job_form)


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
           # return redirect(url_for('main.index'))

    return render_template('profile/profile.html',form=form)

