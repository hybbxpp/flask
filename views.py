from flask import render_template, flash, redirect, session, url_for, request, g
from flask_admin.contrib.sqla import ModelView
import datetime

from app import app, db, admin
from .models import Tasks,Finish

from .forms import TaskForm

admin.add_view(ModelView(Tasks, db.session))


@app.route("/")
def homepage():
    return render_template('index.html',
                           title='homepage',
                           )


@app.route('/create_task', methods=['GET', 'POST'])
def create_task():
    form = TaskForm()
    time = datetime.date.today()
    flash('Errors="%s"' %form.errors)
    if form.validate_on_submit():
        t = Tasks(title=form.name.data, state=form.urgent.data, year=form.year.data)
        db.session.add(t)
        db.session.commit()
        return redirect('/task')

    return render_template('create_task.html',
                           title='Create Student',
                           form=form,time=time)

@app.route('/task', methods=['GET'])
def getAllSTasks():
    Task = Tasks.query.all()
    return render_template('task_list.html',
                           title='All Tasks',
                           Task=Task)

@app.route('/finish', methods=['GET'])
def getAllFinished():
    Finished = Finish.query.all()
    return render_template('finish.html',
                           title='Finished tasks',
                           Finished=Finished)

@app.route('/finish/<id>', methods=['GET', 'POST'])
def create_finish(id):
    form = TaskForm()
    flash('Errors="%s"' %form.errors)
    finish = Tasks.query.get(id)
    db.session.delete(finish)
    db.session.commit()
    t = Finish(title=finish.title, state=finish.state, year=finish.year)
    db.session.add(t)
    db.session.commit()
    return redirect('/task')

@app.route('/task/<id>', methods=['GET', 'POST'])
def recover(id):
    form = TaskForm()
    flash('Errors="%s"' %form.errors)
    recover = Finish.query.get(id)
    db.session.delete(recover)
    db.session.commit()
    t = Tasks(title=recover.title, state=recover.state, year=recover.year)
    db.session.add(t)
    db.session.commit()
    return redirect('/finish')

@app.route('/edit_task/<id>', methods=['GET', 'POST'])
def edit_task(id):
    task = Tasks.query.get(id)
    form = TaskForm(obj=task)
    flash('Errors="%s"' %
          (form.errors))
    if form.validate_on_submit():
        t = task
        t.title = form.name.data
        t.year = form.year.data
        t.state = form.urgent.data
        db.session.commit()
        return redirect('/task')

    return render_template('edit_task.html',
                           title='Edit task',
                           form=form)

@app.route('/delete_task/<id>', methods=['GET'])
def delete_task(id):
    task = Tasks.query.get(id)
    db.session.delete(task)
    db.session.commit()
    return redirect('/task')

@app.route('/delete_finish/<id>', methods=['GET'])
def delete_finish(id):
    finish = Finish.query.get(id)
    db.session.delete(finish)
    db.session.commit()
    return redirect('/finish')


