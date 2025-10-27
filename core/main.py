
from flask import Flask, Blueprint, g, render_template, url_for, redirect, request, session
main = Blueprint('main', __name__)
from core import db, create_app



@main.route('/index')
@main.route('/home')
@main.route('/')
def home():
  return render_template('index.html')

@main.route('/setlocale', methods=['POST'])
def set_locale():
  locale = request.form.get('locale')
  session['locale'] = locale
  path = f'{locale}_index'
  print(path)
  print(session['locale'])
  
  return redirect(url_for(path))

@main.route('/book-class/<int:class_id>')
def book_class(class_id):
    # Get the Class object with the specified ID
    #c = Class.query.get_or_404(class_id)

    # Set the is_booked attribute to True
    #c.is_booked = True
    #db.session.commit()

    # Redirect to the class schedule page
    return redirect(url_for('class_schedule'))

@main.route('/profile')
def profile():
    return 'Profile'
  

@main.route('/cn/home')
@main.route('/cn')
def cn_index():
    return render_template('cn/index.html')

@main.route('/cn/classes')
def cn_classes():
    return render_template('cn/classes.html')
  
@main.route('/cn/contact')
def cn_contact():
    return render_template('cn/contact.html')


@main.route('/de/home')
@main.route('/de')
def de_index():
    return render_template('de/index.html')

@main.route('/de/classes')
def de_classes():
    return render_template('de/classes.html')
  
@main.route('/de/contact')
def de_contact():
    return render_template('de/contact.html')


@main.route('/en/home')
@main.route('/en')
def en_index():
    return render_template('en/index.html')

@main.route('/en/classes')
def en_classes():
    return render_template('en/classes.html')
  
@main.route('/en/contact')
def en_contact():
    return render_template('en/contact.html')


@main.route('/ru/home')
@main.route('/ru')
def ru_index():
    return render_template('ru/index.html')

@main.route('/ru/classes')
def ru_classes():
    return render_template('ru/classes.html')
  
@main.route('/ru/contact')
def ru_contact():
    return render_template('ru/contact.html')

create_app()