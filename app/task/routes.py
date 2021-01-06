from flask import render_template, flash, redirect, url_for, request
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


@bp.route('/list')
@login_required
def list():
    page = request.args.get('page', 1, type=int)
    # Можно добавить поле task.timestamp и сортировать по времени создания задачи
    tasks = Task.query.order_by(Task.name.desc()).paginate(page, 12, False)
    next_url = url_for('task.list', page=tasks.next_num) if tasks.has_next else None
    prev_url = url_for('task.list', page=tasks.prev_num) if tasks.has_prev else None
    return render_template('task/taskList.html', title='Список всех задач', tasks=tasks.items, next_url=next_url,
                           prev_url=prev_url)


@bp.route('/delete/<id>', methods=['GET'])
@login_required
def delete(id):
    task = Task.query.filter_by(id=id).first()
    if task is None:
        flash('Задача не найдена')
        return redirect(url_for('task.list'))
    db.session.delete(task)
    db.session.commit()
    flash('Задача успешно удалена')
    return redirect(url_for('task.list'))
