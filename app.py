from schema import *

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///schema.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200))
    status = db.Column(db.Integer)

@app.route('/')
def index():
    stat_todo = Task.query.filter_by(status=0).all()
    stat_doing = Task.query.filter_by(status=1).all()
    stat_done = Task.query.filter_by(status=2).all()

    return render_template('index.html', 
                           todo=stat_todo, 
                           doing=stat_doing,
                           done=stat_done)

@app.route('/add', methods=['POST'])
def add():
    task = Task(text=request.form['todoitem'], status=0)
    db.session.add(task)
    db.session.commit()

    return redirect(url_for('index'))

@app.route('/updatestat', methods=['POST'])
def updatestat():
    card_id = request.form.get('card_id', type=int)
    new_section = request.form.get('new_section', type=str)
    new_section_id = section_dict[new_section]
    print('updatestat:', card_id, new_section, new_section_id)

    task = Task.query.filter_by(id=card_id).first()
    task.status = new_section_id
    db.session.commit()
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug = True)