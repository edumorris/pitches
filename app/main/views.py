from flask import render_template, request, redirect, url_for, abort
from . import main
from ..models import Comment, User, Pitch
from flask_login import login_required

# Main page
@main.route('/')
def index():
    '''
    Homepage
    '''

    return render_template('index.html')

@main.route('/pitch/comment/new/<int: id>', methods = ['GET', 'POST'])
@login_required
def new_comment(id):
    pass

@main.route('/user/<uname>')
@login_required
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)
    
    return render_template("profile/profile.html", user = user)