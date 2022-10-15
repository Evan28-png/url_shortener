import os
import random
from dotenv import load_dotenv
load_dotenv()
from flask import Flask, request, url_for, render_template, redirect, g
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SECRET_KEY']=os.environ['SECRET_KEY']
app.config['SQLALCHEMY_DATABASE_URI']=os.environ['SQLALCHEMY_DATABASE_URI']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=os.environ['SQLALCHEMY_TRACK_MODIFICATIONS']
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Url_form(FlaskForm):
    url = StringField('Enter url')
    submit = SubmitField()



class Url(db.Model):
    __tablename__='urls'
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(64))
    short_url = db.Column(db.String(64))
    #date_created = db.Column(db.Date)



@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        form = Url_form()
        if form.validate_on_submit():
            url = request.values.get('url')
            short_url = f'evan.ly{random.randint(1,48748374823749)}'
            url = Url(original_url=url, short_url=short_url)
            db.session.add(url)
            db.session.commit()
            return render_template('url.html', short_url=short_url)
    return render_template('index.html', form=Url_form())


@app.route('/url')
def url():
    return render_template('url.html')


if __name__ == '__main__':
    app.run(debug=True)
