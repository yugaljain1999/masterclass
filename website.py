import os
from flask import Flask,url_for,render_template,redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from forms import Addform,Delform
app=Flask(__name__)
app.config['SECRET_KEY']='myfamily'


################################
######Database Section##########
################################

basedir=os.path.abspath(os.path.dirname(__file__))

app.config['SQLAlchemy_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config["SQLAlchemy_TRACK_MODIFICATIONS"]=False
db=SQLAlchemy(app)
Migrate(app,db)

#######################
######Create Forms#####
#######################

class Puppy(db.Model):
    __tablename__='puppies'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.Text)
    def __init__(self,name):
        self.name=name
    def __repr__(self):
        return "This is puppy name:{self.name}".format(self.name)
db.create_all()
#####################################
###########Add Forms#################
#####################################

@app.route('/')
def index():
    return render_template("home.html")
@app.route('/add',methods=['GET','POST'])
def add_pup():
    form=Addform()
    if form.validate_on_submit():
        name=form.name.data
        pup=Puppy(name)
        db.session.add(pup)
        db.session.commit()

        return render_template(url_for('list_pup'))
    return render_template("add.html",form=form)


@app.route('/list')
def list_pup():
    puppies=Puppy.query.all()
    return render_template('list.html',puppies=puppies)
@app.route('/del',methods=['GET','POST'])

def del_pup():
    form=Delform()
    if form.validate_on_submit():
        id=form.id.data
        pup=form.query.get(id)
        db.session.delete(pup)
        db.session.commit()
        return render_template(url_for('list_pup'))
    return render_template("delete.html",form=form)


if __name__=='__main__':
    app.run(debug=True)
