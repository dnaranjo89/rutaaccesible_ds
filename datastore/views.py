from flask import render_template

from datastore import webapp, db
# from load_data import parse_caceres


@webapp.route('/')
@webapp.route('/index')
def index():
    cur = db.connection.cursor()
    cur.execute('''SELECT * FROM sakila.actor''')
    rv = cur.fetchall()
    # data = parse_caceres()
    user = {'nickname': 'David'}  # fake user
    return render_template('index.html',
                           title='Home',
                           user=user)
