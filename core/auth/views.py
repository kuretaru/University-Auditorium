from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, login_required, current_user
from . import auth
from .forms import RegistrationForm, LoginForm
from .models import User
from .. import db
from werkzeug.urls import url_parse
from config import CURRENT_LANGUAGE

@auth.route('/register', methods=['GET', 'POST'])
def register():
  if current_user.is_authenticated:
    return redirect(url_for('index'))
  form = RegistrationForm()
  #print(f"\n\n\n{form.username.data}\n\n\n{form.email.data}\n\n\n{form.is_teacher.data}\n\n\n{form.language.data}\n\n\n")
  if form.validate_on_submit():
    
    if form.is_teacher.data is None:
      is_teacher = False
    else:
      is_teacher=form.is_teacher.data
    if form.language.data is None:
      language = 'None'
    else:
      language=form.language.data
    user = User(username=form.username.data.lower(),
                email=form.email.data.lower(),
                is_teacher=is_teacher, language=language)
    user.set_password(form.password.data)
    db.session.add(user)
    db.session.commit()
    flash('Congratulations, you are now a registered user!')
    return redirect(url_for('login'))
  return render_template('/register.html', title='Register', form=form)


@auth.route('/login', methods=['GET', 'POST'])
def login():
  nologin = False
  if current_user.is_authenticated:
    return redirect(url_for('home'))
  form = LoginForm()
  if form.validate_on_submit():
    user = User.query.filter_by(email=form.email.data.lower()).first()
    print(user.language)
    CURRENT_LANGUAGE = user.language
    if user is None or not(user.check_password(form.password.data)):
      nologin = True
    else:
      login_user(user, remember=form.remember_me.data)
      next_page = request.args.get('next')
      if not next_page or url_parse(next_page).netloc != '':
        next_page = url_for('home')
      return redirect(next_page)
  return render_template('/login.html', title='Sign In',
                         form=form, message=nologin)


@auth.route('/logout')
def logout():
  logout_user()
  return redirect(url_for('index'))
