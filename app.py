from flask import Flask, render_template, request, redirect, url_for
from models import *
from smartEmail import emailClassifier, reminder

app = Flask(__name__)

@app.before_request
def before_request():
    initialize_db()

@app.teardown_request
def teardown_request(exception):
    db.close()

@app.route('/')
def index():
    return render_template('dashboard.html', emails=Emails.select())

@app.route('/newmail/')
def newmail():
    return render_template('newmail.html')

@app.route('/primary/')
def primary():
    return render_template('primary.html', emails=Emails.select().where(Emails.category=='primary'))

@app.route('/social/')
def social():
    return render_template('social.html', emails=Emails.select().where(Emails.category=='social'))

@app.route('/updates/')
def updates():
    return render_template('updates.html', emails=Emails.select().where(Emails.category=='update'))

@app.route('/promotion/')
def promotion():
    return render_template('promotion.html', emails=Emails.select().where(Emails.category=='promotion'))

@app.route('/spam/')
def spam():
    return render_template('spam.html', emails=Emails.select().where(Emails.category=='spam'))

@app.route('/readmail/<id>')
def readmail(id):
    return render_template('mail.html', mails=Emails.select().where(Emails.id==id), reminder=reminder(Emails.get(Emails.id==id).content))

@app.route('/addmail/', methods=['POST'])
def addmail():
    Emails.create(
        sender = request.form['sender'],
        subject = request.form['subject'],
        content = request.form['content'],
        category = emailClassifier(request.form['content'])
    )
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run()
