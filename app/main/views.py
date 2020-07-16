from flask import render_template, request, redirect, url_for, abort
from . import main
from ..models import Comment, User, Pitch
from flask_login import login_required
from .forms import PitchForm, CommentForm
from .. import db

# Main page
@main.route('/')
def index():
    '''
    Homepage
    '''

    pitch = Pitch.query.all()

    return render_template('index.html', pitch = pitch)

@main.route('/pitch/comment/new/<int:id>', methods = ['GET', 'POST'])
@login_required
def new_comment(id):
    pass

@main.route('/pitch/<uname>/new/', methods = ['GET', 'POST'])
@login_required
def new_pitch(uname):
    form = PitchForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username = uname).first()

        # Submitting the data
        pitch_data = Pitch(pitch = form.pitch.data, category = form.category.data, upvotes  = 0, downvote = 0, submitted_by = user.id)

        db.session.add(pitch_data)
        db.session.commit()

        return redirect(url_for('main.index'))

    return render_template('pitch.html', uname=uname, pitch_form = form)

@main.route('/user/<uname>')
@login_required
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    user_id = user.id

    # Getting pitch by users
    # user_id = User.query.filter_by(id = user.id).first()
    pitch_data = Pitch.query.filter_by(submitted_by = user_id).all()

    if user is None:
        abort(404)
        
    
    return render_template("profile/profile.html", user = user, pitch_data = pitch_data)