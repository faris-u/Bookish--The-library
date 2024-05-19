from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hellothere'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/bookish'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate=Migrate(app,db)





class Books(db.Model):
    book_id = db.Column(db.Integer,primary_key=True)
    book_name = db.Column(db.String(100))
    author_name = db.Column(db.String(50))
    book_category = db.Column(db.String(50))
    story = db.Column(db.Text)
    image = db.Column(db.String(200))

    def __repr__(self):
        return f"<Books {self.book_name}"

def create_tables():
    db.create_all()

@app.route('/',endpoint='home')
def home():
    books = Books.query.all()
    return render_template('home.html',books=books,endpoint='view')

@app.route('/view/<int:book_id>')
def view(book_id):
    book = Books.query.filter_by(book_id=book_id)
    return render_template('view.html',book=book)

@app.route('/mystery',endpoint='mystery')
def mystery():
    books = Books.query.filter_by(book_category='mystery')
    return render_template('mystery.html',books=books)

@app.route('/romance',endpoint='romance')
def romance():
    books = Books.query.filter_by(book_category='romance')
    return render_template('romance.html',books=books)


@app.route('/adventure',endpoint='adventure')
def adventure():
    books = Books.query.filter_by(book_category='adventure')
    return render_template('adventure.html',books=books)

@app.route('/anime',endpoint='anime')
def anime():
    books = Books.query.filter_by(book_category='anime')
    return render_template('anime.html',books=books)

@app.route('/fiction',endpoint='fiction')
def fiction():
    books = Books.query.filter_by(book_category='fiction')
    return render_template('fiction.html',books=books)


admin = Admin(app, name="Book Admin", template_mode="bootstrap3")
admin.add_view(ModelView(Books, db.session))



if __name__ == '__main__':
    app.run(debug=True)