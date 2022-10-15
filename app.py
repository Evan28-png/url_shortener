import os
from dotenv import load_dotenv
load_dotenv()
from flask import Flask, request, url_for, render_template
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




@app.route('/')
def index():
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)
