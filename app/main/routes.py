from flask import render_template

from app.main import bp

from flask_login import login_required


@bp.route('/')
@bp.route('/index')
@login_required
def index():
    return render_template('index.html', title='Домашняя страница')


@bp.route('/creator')
@login_required
def creator():
    return render_template('creator.html', title='Новое задание')
