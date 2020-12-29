from flask import render_template

from app.task import bp

from flask_login import login_required

from app.task.forms import TaskCreateForm


@bp.route('/create')
@login_required
def create():
    form = TaskCreateForm()
    return render_template('task/create.html', title='Новое задание', form=form)
