SECRET_KEY = 'asdfasdfadsfadsfasdf'
DEBUG = True


DB_USERNAME = 'arif_hanif'
#DB_PASSWORD = 'szah9703'
BLOG_DATABASE_NAME = 'blog'

SQLALCHEMY_DATABASE_URI = 'mysql://%s@127.0.0.1:3306/%s' % (DB_USERNAME, BLOG_DATABASE_NAME)