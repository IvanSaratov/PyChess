from flask import render_template, flash, redirect, url_for
from flask_login import login_required

from app import db
from app.models import Task
from app.task import bp
from app.task.forms import TaskCreateForm


@bp.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    form = TaskCreateForm()
    if form.validate_on_submit():
        task = Task.query.filter_by(name=form.name.data).first()
        if task:
            flash('Такая задача уже существует')
            return redirect(url_for('task.create'))
        task = Task(name=form.name.data, start_pos=form.start_pos.data, end_pos=form.end_pos.data)
        db.session.add(task)
        db.session.commit()
        flash('Задача создана!')
        return redirect(url_for('main.index'))
    return render_template('task/create.html', title='Новое задание', form=form)
