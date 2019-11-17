from flask import Blueprint, render_template, request, redirect, url_for
from . import db
from .models import Comment

main = Blueprint('main', __name__)

@main.route('/')
def index():
    comments = Comment.query.all()
    return render_template('index.html', comments=comments)

@main.route('/sign')
def sign():
    return render_template('sign.html')

@main.route('/sign', methods=['POST'])
def sign_post():
    name = request.form.get('name')
    email = request.form.get('email')   
    comment = request.form.get('comment')

    new_comment = Comment(name=name, email=email, comment_text=comment)
    db.session.add(new_comment)
    db.session.commit()
    
    return redirect(url_for('main.index'))

@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/learn')
def learn():
    return render_template('learn.html')

@main.route('/info')
def info():
    return render_template('info.html')