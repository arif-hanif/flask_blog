from flask_blog import app

@app.route('/login')

def login():
    return 'User Login'