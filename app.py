from flask import Flask, render_template, request, redirect #here we hve used redirect to make a new page for th4 delete one 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///employee.db"
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False

db = SQLAlchemy(app)
app.app_context().push()

class Employee(db.Model):
   sno = db.Column(db.Integer, primary_key = True)
   name = db.Column(db.String(200), nullable = False)
   email = db.Column(db.String(500), nullable = False)

@app.route("/", methods=['GET', 'POST'])
def home():
   if request.method == 'POST':
      name = request.form['name']
      email = request.form['email']
      employee = Employee(name = name, email = email)
      db.session.add(employee)
      db.session.commit()
   allemployee = Employee.query.all()	
   return render_template("index.html", allemployee=allemployee)

@app.route("/about")
def about():
   return render_template("about.html")

@app.route("/delete/<int:sno>") # serial no is variable and it has datatype as integer 
def delete(sno):
    employee = Employee.query.filter_by(sno=sno).first()# data is filtered on the basis of serial no 
    db.session.delete(employee)
    db.session.commit()
    return redirect("/")
@app.route("/update/<int:sno>")
def update(sno):
    pass

@app.route("/contact")
def contact():
   return render_template("contact.html")


if __name__ == '__main__':
   app.run(debug=True)