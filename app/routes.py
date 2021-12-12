from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Stepan Krivchenkov'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }, 
        {
            'author': {'username': 'Ippolit'},
            'body': 'Kakaya gadost vasha zalivnaya ryba!!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
