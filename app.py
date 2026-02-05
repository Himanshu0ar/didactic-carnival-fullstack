# from flask import Flask, render_template
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///employee.db"
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# db = SQLAlchemy(app)
# app.app_context().push()

# class Employee(db.Model):
#     sno = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(200), nullable=False)
#     email = db.Column(db.String(200), unique=True, nullable=False)

# @app.route("/")
# def home():
#     employee = Employee(name="Himanshu", email="hims@gmail.com")
#     db.session.add(employee)
#     db.session.commit()
#     all_employees = Employee(name="employee name", email="employee email")
#     return render_template('index.html')

# @app.route("/about")
# def about():
#     return render_template("about.html")

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///employee.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
app.app_context().push()

class Employee(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), unique=True, nullable=False)

@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        employee = Employee(name=name, email=email)
        db.session.add(employee)
        db.session.commit()
    all_employees = Employee.query.all()
    return render_template("index.html", employees=all_employees)


@app.route('/about')
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)