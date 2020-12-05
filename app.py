from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.secret_key = "Secret Key"

# SqlAlchemy Database Configuration With Mysql
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:NOSOCCUS@localhost/departments'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# Creating model table for our CRUD database
class Department(db.Model):
    id_dep = db.Column(db.Integer, primary_key=True)
    dep_name = db.Column(db.String(30))
    description = db.Column(db.String(100))
    avg_salary = db.Column(db.Integer())
    num_employees = db.Column(db.Integer())

    def __init__(self, dep_name, description, avg_salary, num_employees):
        self.dep_name = dep_name
        self.description = description
        self.avg_salary = avg_salary
        self.num_employees = num_employees


# This is the index route where we are going to
# query on all our employee data
@app.route('/')
def index():
    all_data = Department.query.all()

    return render_template("index.html", departments=all_data)


# this route is for inserting data to database via html forms
@app.route('/insert', methods=['POST'])
def insert():

    if request.method == 'POST':

        dep_name = request.form['dep_name']
        description = request.form['description']
        avg_salary = request.form['avg_salary']
        num_employees = request.form['num_employees']

        my_data = Department(dep_name, description, avg_salary, num_employees)
        db.session.add(my_data)
        db.session.commit()

        flash("Employee Inserted Successfully")

        return redirect(url_for('index'))


# This is our update route where we are going to update our employee
@app.route('/update', methods=['GET', 'POST'])
def update():

    if request.method == 'POST':
        my_data = Department.query.get(request.form.get('id_dep'))

        my_data.dep_name = request.form['dep_name']
        my_data.description = request.form['description']
        my_data.avg_salary = request.form['avg_salary']
        my_data.num_employees = request.form['num_employees']

        db.session.commit()
        flash("Department updated successfully")

        return redirect(url_for('index'))


# This route is for deleting our employee
@app.route('/delete/<id_dep>/', methods=['GET', 'POST'])
def delete(id_dep):
    my_data = Department.query.get(id_dep)
    db.session.delete(my_data)
    db.session.commit()
    flash("Department deleted successfully")

    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)
