import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = ''
app.config.from_object(Config)

db = SQLAlchemy(app)
# migrate = Migrate(app, db)

@app.route("/")
def home():
    return "Your Python API is running!"

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=os.environ.get('PORT', 3000))