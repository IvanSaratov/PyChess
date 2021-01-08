from flask import render_template, flash, redirect, url_for, request
from flask_login import login_required

from app import db
from app.models import Task, Tournament
from app.task import bp
from app.task.forms import TaskCreateForm, TournamentCreateForm


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
        return redirect(url_for('task.list'))
    return render_template('task/task_create.html', title='Новое задание', form=form)


@bp.route('/list')
@login_required
def list():
    page = request.args.get('page', 1, type=int)
    # Можно добавить поле task.timestamp и сортировать по времени создания задачи
    tasks = Task.query.order_by(Task.name.desc()).paginate(page, 12, False)
    next_url = url_for('task.list', page=tasks.next_num) if tasks.has_next else None
    prev_url = url_for('task.list', page=tasks.prev_num) if tasks.has_prev else None
    return render_template('task/task_list.html', title='Список всех задач', tasks=tasks.items, next_url=next_url,
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


@bp.route('/tournament/create', methods=['GET', 'POST'])
@login_required
def tournament_create():
    form = TournamentCreateForm()
    tasks = Task.query.order_by(Task.name.desc()).all()
    task_list = [(task.name, task.id) for task in tasks]
    if form.validate_on_submit():
        if request.form.get('tasks') is None:
            flash('Выберите хотя бы одно задание')
            return redirect(url_for('task.tournament_create'))
        set = Tournament.query.filter_by(name=form.name.data).first()
        if set:
            flash('Турнир с таким именем уже существует')
            return redirect(url_for('task.tournament_create'))
        tournament = Tournament(name=form.name.data)
        for task_id in request.form.getlist('tasks'):
            task = Task.query.filter_by(id=task_id).first()
            tournament.tasks.append(task)
        db.session.commit()
        flash('Вы создали турнир')
        return redirect(url_for('main.index'))
    return render_template('task/tournament_create.html', titile='Создать турнир', form=form, list=task_list)
