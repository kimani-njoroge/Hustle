from flask import render_template,request,redirect,url_for,abort
from . import main
from flask_login import login_required,current_user
from . forms import PostJobForm
from ..models import Jobs
from app import db



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

    '''
    View root page function that returns the index page and its data
    '''
    job_form = PostJobForm()

    title = 'Home'
    if job_form.validate_on_submit():

        jobs = Jobs(title=job_form.title.data, description=job_form.description.data, duration=job_form.duration.data, technologies=job_form.technologies.data, user=current_user)
        db.session.add(jobs)
        db.session.commit()
        return redirect(url_for('auth.register'))


    return render_template('postjob.html', title = title, job_form=job_form )


@main.route('/postbid/<int:id>')
def post_bid(id):

    '''
    View root page function that returns the index page and its data
    '''

    title = 'Home'

    return render_template('postbid.html', title = title )
