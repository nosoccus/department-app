from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

from wtforms.ext.sqlalchemy.fields import QuerySelectField

app = Flask(__name__)

app.secret_key = "Secret Key"

# SqlAlchemy Database Configuration With Mysql
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:NOSOCCUS@localhost/departments'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# Creating model table for our CRUD database
class Department(db.Model):
    __tablename__ = 'department'

    id_dep = db.Column(db.Integer, primary_key=True)
    dep_name = db.Column(db.String(30))
    description = db.Column(db.String(100))
    employees = db.relationship('Employee', backref='department',
                                lazy='dynamic')

    def __init__(self, dep_name, description):
        self.dep_name = dep_name
        self.description = description


class Employee(db.Model):
    __tablename__ = 'employee'

    id_emp = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30))
    last_name = db.Column(db.String(30))
    birth_date = db.Column(db.Date())
    salary = db.Column(db.Integer())
    department_id = db.Column(db.Integer, db.ForeignKey("department.id_dep"))

    def __init__(self, first_name, last_name, birth_date, salary, department_id):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.salary = salary
        self.department_id = department_id


@app.route('/')
def index():
    return redirect("/department")


# This is the index route where we are going to
# query on all our employee data
@app.route('/department')
def dep_index():
    all_data = Department.query.all()

    return render_template("departments_index.html", departments=all_data)


# this route is for inserting data to database via html forms
@app.route('/department/insert', methods=['POST'])
def dep_insert():
    if request.method == 'POST':
        dep_name = request.form['dep_name']
        description = request.form['description']

        my_data = Department(dep_name, description)
        db.session.add(my_data)
        db.session.commit()

        flash("Department inserted successfully")

        return redirect(url_for('dep_index'))


# This is our update route where we are going to update our employee
@app.route('/department/update', methods=['GET', 'POST'])
def dep_update():
    if request.method == 'POST':
        my_data = Department.query.get(request.form.get('id_dep'))

        my_data.dep_name = request.form['dep_name']
        my_data.description = request.form['description']

        db.session.commit()
        flash("Department updated successfully")

        return redirect(url_for('dep_index'))


# This route is for deleting our employee
@app.route('/department/delete/<id_dep>/', methods=['GET', 'POST'])
def dep_delete(id_dep):
    my_data = Department.query.get(id_dep)
    db.session.delete(my_data)
    db.session.commit()
    flash("Department deleted successfully")

    return redirect(url_for('dep_index'))


@app.route('/employee')
def emp_index():
    all_data = Employee.query.all()

    return render_template("employees_index.html", employees=all_data)


# this route is for inserting data to database via html forms
@app.route('/employee/insert', methods=['POST'])
def emp_insert():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        birth_date = request.form['birth_date']
        salary = request.form['salary']
        department_id = request.form['department_id']
        my_data = Employee(first_name, last_name, birth_date, salary, department_id)

        db.session.add(my_data)
        db.session.commit()

        flash("Employee inserted successfully")

        return redirect(url_for('emp_index'))


# This is our update route where we are going to update our employee
@app.route('/employee/update', methods=['GET', 'POST'])
def emp_update():
    if request.method == 'POST':
        my_data = Employee.query.get(request.form.get('id_emp'))

        my_data.first_name = request.form['first_name']
        my_data.last_name = request.form['last_name']
        my_data.birth_date = request.form['birth_date']
        my_data.salary = request.form['salary']
        my_data.department_id = request.form['department_id']

        db.session.commit()
        flash("Employee updated successfully")

        return redirect(url_for('emp_index'))


# This route is for deleting our employee
@app.route('/employee/delete/<id_emp>/', methods=['GET', 'POST'])
def emp_delete(id_emp):
    my_data = Employee.query.get(id_emp)
    db.session.delete(my_data)
    db.session.commit()
    flash("Employee deleted successfully")

    return redirect(url_for('emp_index'))


if __name__ == "__main__":
    app.run(debug=True)

"""
TODO: connect employees with departments;
      calculate avg salary
      calculate num of employees
      employees/departments tabs
"""
