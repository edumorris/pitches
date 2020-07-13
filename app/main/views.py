from flask import render_template, request, redirect, url_for
from . import main
from ..models import Comment
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