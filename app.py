from flask import Flask
from flask import render_template
from flask import request, flash, redirect, url_for
from werkzeug.utils import secure_filename
from bmc.library import Library

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)

@app.route('/hello', methods = ['POST', 'GET'])
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

@app.route('/file', methods = ['POST', 'GET'])
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

@app.route('/bmc_start')
def enter():
    return render_template("bmc_books.html")

@app.route('/bmc_trial')
def memory():
    global book
    book = request.args.get("book")
    return render_template('bmc_form.html')

@app.route('/bmc_final')
def result():
    library = Library()
    correct = 0
    for x in range(1, len(library.get(book)) + 1):
        input = request.args.get(f"{x}")
        if (input.lower() == library.get(book)[x - 1].lower()):
            correct += 1
    return render_template('bmc_result.html', result=correct)

if (__name__ == '__main__'):
    app.run()
