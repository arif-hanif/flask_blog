import os, sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask_blog import app
import sqlalchemy

try:
    db_uri = 'mysql://%s@127.0.0.1:3306/' % (app.config['DB_USERNAME'])
    engine = sqlalchemy.create_engine(db_uri)
    conn = engine.connect()
    conn.execute("commit")
    conn.execute("CREATE DATABASE " + app.config['BLOG_DATABASE_NAME'])
    conn.close()
except:
    print "Database Exists"
    
from flask_blog import db

# add all models here
from user.models import *

db.create_all()