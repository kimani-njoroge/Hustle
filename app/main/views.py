from flask import render_template,request,redirect,url_for,abort
from . import main

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


@main.route('/postbid/<int:id>')
def post_bid(id):

    '''
    View root page function that returns the index page and its data
    '''

    title = 'Home'

    return render_template('postbid.html', title = title )

@main.route('/bid/<int:id>')
def bid(id):

    '''
    View root page function that returns the index page and its data
    '''

    title = 'Home'

    return render_template('client.html', title = title )


@main.route('/job/<int:id>')
def job(id):

    '''
    View root page function that returns the index page and its data
    '''

    title = 'Home'

    return render_template('freelancer.html.html', title = title )