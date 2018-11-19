
from flask_mail import Message
from flask import render_template
from app import mail
import app
from threading import Thread

app.config['FLASKY_MAIL_SUBJECT_PREFIX'] = '[Flasky]'
app.config['FLASKY_MAIL_SENDER'] = 'haibosoft@gmail.com'

def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)

def send_mail(to, subject, template, **kwargs):
    msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + subject,
                  sender=app.config['FLASKY_MAIL_SENDER'], recipients=[to])
    msg.body = "what is you name?"
    msg.html = '<h1>HTML</h>, what is you name?'
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()
    return thr