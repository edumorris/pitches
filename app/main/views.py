from flask import render_template, request, redirect, url_for
from . import main
from ..models import Comment

# Main page
@main.route('/')
def index():
    '''
    Homepage
    '''

    return render_template('index.html')