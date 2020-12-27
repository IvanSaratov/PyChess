# -*- coding: utf-8 -*-
from flask import render_template
from flask_login import login_required

from app import app


@app.route('/')
@app.route('/index')
@login_required
def index():
    return render_template('index.html', title='Домашняя страница')


@app.route('/creator')
@login_required
def creator():
    return render_template('creator.html', title='Новое задание')
