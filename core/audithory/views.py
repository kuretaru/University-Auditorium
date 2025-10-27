from flask import render_template, flash, redirect, url_for, request
from flask_login import login_required, current_user
from .models import Number
from ..models import Audithories
from . import audithory
from .forms import BookForm
from .. import db
from datetime import datetime


@audithory.route('/audithory/book-audithory', methods=['GET', 'POST'])
@login_required
def book_audithory():
  check = None
  user = current_user
  audithories = Audithories.query.filter_by(author=user)
  date = datetime.now()
  now = date.strftime("%Y-%m-%d")

  print(check+'\n'+audithory+'\n'+date+'\n'+now)
  
  form = BookForm()
  form.category.choices = [(number.id, number.name) for number in Number.query.all()]

  if request.method == "POST":
    if request.form.get('taskDelete') is not None:
      deleteTask = request.form.get('checkedbox')
      if deleteTask is not None:
        audithories = audithories.query.filter_by(id=int(deleteTask)).one()
        db.session.delete(audithories)
        db.session.commit()
        return redirect(url_for('task.tasks'))
      else:
        check = 'Please check-box of task to be deleted'

    elif form.validate_on_submit():
      selected = form.category.data
      number = Number.query.get(selected)
      audithories = Audithories(name=form.name.data, reason=form.reason.data, 
                                date=form.date.data, time=form.time.data, 
                                number=number.name, author=user)
      db.session.add(audithories)
      db.session.commit()
      if CURRENT_LANGUAGE == 'cn':
        flash('Congratulations, you just added a new note')
      elif CURRENT_LANGUAGE == 'de':
        flash('')
      elif CURRENT_LANGUAGE == 'en':
        flash('')
      elif CURRENT_LANGUAGE == 'ru':
        flash('')
      else:
        flash('Missing localization!')
        
      return redirect(url_for('task.tasks'))

  
  return render_template('audithory/book-audithory.html', 
                         title='Auditorium Bookings', form=form, 
                         audithories=audithories, DateNow=now, check=check)