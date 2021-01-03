from bmc import bmc_app, db
from bmc.forms import LoginForm, RegistrationForm
from bmc.library import Library
from bmc.models import User, Practice
from flask import render_template, request
from flask import request, flash, redirect, url_for
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from werkzeug.utils import secure_filename
from google.cloud import speech_v1p1beta1


ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'wav'}

@bmc_app.route('/hello', methods = ['POST', 'GET'])
def index():
    name = request.args.get('name', 'Nobody')

    if (request.method == 'POST'):
        name = request.form['name']
        greet = request.form['greet']
        greeting = f'{greet}, {name}'
        return render_template("index.html", greeting = greeting)
    else:
        return render_template("hello_form.html")

def good_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@bmc_app.route('/file', methods = ['POST', 'GET'])
@login_required
def potato():
    if (request.method == 'POST'):
        file = request.files['file']
        name = request.form['name']
        
        filename = secure_filename(name)

        if file and good_file(file.filename):
            file.save("images/" + filename + ".png")
            return render_template("uploaded.html")
    else:
        return render_template("file_upload.html")

@bmc_app.route('/bmc_start')
@login_required
def enter():
    return render_template("bmc_books.html")

@bmc_app.route('/voice', methods = ['POST'])
@login_required
def save_voice():
    file_bytes = request.files['audio_data'].read()
    # .WAV does not need encoding
    audio = { 'content': file_bytes}
    config = {
        "language_code": "en-US",
        "sample_rate_hertz": 48000,
    }
    speech_response = bmc_app.speech_client.recognize(config,audio)
    first_result = None
    for result in speech_response.results:
        alternative = result.alternatives[0]

        if first_result is None:
            first_result = "Transcript: {}".format(alternative.transcript)
        print(u"Transcript: {}".format(alternative.transcript))

    return first_result

@bmc_app.route('/bmc_trial')
def memory():
    global book
    global library
    library = Library()
    global format
    book = request.args.get("book")
    format = request.args.get("format")
    try:
        if (format == "text"):
                return render_template('bmc_form.html', length = len(library.get(book)))
        elif (format == "voice"):
            return render_template('bmc_questions.html', length = len(library.get(book)))
        else:
            return render_template('error.html')
    except TypeError:
        return render_template('error.html')

@bmc_app.route('/bmc_record')
def record():
    global chapter_num
    chapter_num = request.args.get("chapter")
    return render_template('bmc_voice.html')

@bmc_app.route('/bmc_final', methods = ['GET', 'POST'])
def result():
    if (request.method == 'POST'):
        user = User.query.filter_by(username=current_user.username).first_or_404()
        correct = 0
        try:
            if (format == "text"):
                for x in range(0, len(library.get(book))):
                    input = request.form[f"{x}"]
                    if (input.lower() == library.get(book)[x].lower()):
                        correct += 1
            elif (format == "voice"):
                correct = 6
            p = Practice(book=book, correct=correct, medium=format, user=user)
            db.session.add(p)
            db.session.commit()
            return render_template('bmc_result.html', result=correct)
        except TypeError:
            return render_template('error.html')
    else:
        return render_template('error.html')

@bmc_app.route('/bmc_history/<username>')
def history(username):
    user = User.query.filter_by(username=username).first_or_404()
    practices = user.practices
    return render_template('bmc_history.html', user = user, practices = practices)

@bmc_app.route('/login', methods = ['GET', 'POST'])
def login():
    if (current_user.is_authenticated):
        return redirect(url_for('enter'))
    form = LoginForm()
    if (form.validate_on_submit()):
        user = User.query.filter_by(username=form.username.data).first()
        if (user is None or not user.check_password(form.password.data)):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if (not next_page or url_parse(next_page).netloc != ''):
            next_page = url_for('enter')
        return redirect(next_page)
    return render_template('login.html', form = form)

@bmc_app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@bmc_app.route('/register', methods = ['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('enter'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Congratulations, you have been registered!")
        return redirect(url_for('login'))
    return render_template('registration.html', form=form)
    