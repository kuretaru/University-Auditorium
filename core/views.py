from flask import request, redirect, render_template, session, url_for
from core import app
from config import CURRENT_LANGUAGE

@app.route('/index')
@app.route('/home')
@app.route('/')
def home():
  return render_template('index.html')

@app.route('/setlocale', methods=['POST'])
def set_locale():
  CURRENT_LANGUAGE = request.form.get('locale')
  session['locale'] = CURRENT_LANGUAGE
  path = f'{CURRENT_LANGUAGE}_index'
  print(path)
  print(session['locale'])
  
  
  return redirect(url_for(path))

@app.route('/book-class/<int:class_id>')
def book_class(class_id):
    # Get the Class object with the specified ID
    #c = Class.query.get_or_404(class_id)

    # Set the is_booked attribute to True
    #c.is_booked = True
    #db.session.commit()

    # Redirect to the class schedule page
    return redirect(url_for('class_schedule'))

@app.route('/profile')
def profile():
    return 'Profile'
  

@app.route('/cn/home')
@app.route('/cn')
def cn_index():
    return render_template('cn/index.html')

@app.route('/cn/classes')
def cn_classes():
    return render_template('cn/classes.html')
  
@app.route('/cn/contact')
def cn_contact():
    return render_template('cn/contact.html')


@app.route('/de/home')
@app.route('/de')
def de_index():
    return render_template('de/index.html')

@app.route('/de/classes')
def de_classes():
    return render_template('de/classes.html')
  
@app.route('/de/contact')
def de_contact():
    return render_template('de/contact.html')


@app.route('/en/home')
@app.route('/en')
def en_index():
    return render_template('en/index.html')

@app.route('/en/classes')
def en_classes():
    return render_template('en/classes.html')
  
@app.route('/en/contact')
def en_contact():
    return render_template('en/contact.html')


@app.route('/ru/home')
@app.route('/ru')
def ru_index():
    return render_template('ru/index.html')

@app.route('/ru/classes')
def ru_classes():
    return render_template('ru/classes.html')
  
@app.route('/ru/contact')
def ru_contact():
    return render_template('ru/contact.html')