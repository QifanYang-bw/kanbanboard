from schema import *

from flask import Flask, render_template, request, jsonify, redirect, url_for
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
    try:
        text = request.form.get('card_text', type=str)
        print(text, request.form)

        task = Task(text=text, status=0)
        db.session.add(task)
        db.session.commit()

        return jsonify({
            "status":"success",
            "err":None,
            "card_id":str(task.id),
            "session":section_dict_rev[0],
            "text":task.text
        })
    except Exception as e:
        return jsonify({"status":"fail", "err":str(e)})

@app.route('/updatestat', methods=['POST'])
def updatestat():
    try:
        card_id = request.form.get('card_id', type=int)
        section = request.form.get('section', type=str)
        section_id = section_dict[section]  

        task = Task.query.filter_by(id=card_id).first()
        task.status = section_id
        db.session.commit()
        
        return jsonify({"status":"success", "err":None})
    except Exception as e:
        return jsonify({"status":"fail", "err":str(e)})

if __name__ == '__main__':
    app.run(debug = True)