from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.employee import Employee
from init_db import db


employee = Blueprint("employee", __name__)


@employee.route('/employee')
def emp_index():
    all_data = Employee.query.all()

    return render_template("employees_index.html", employees=all_data)


@employee.route('/employee/insert', methods=['POST'])
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

        return redirect(url_for('employee.emp_index'))


@employee.route('/employee/update', methods=['GET', 'POST'])
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

        return redirect(url_for('employee.emp_index'))


@employee.route('/employee/delete/<id_emp>/', methods=['GET', 'POST'])
def emp_delete(id_emp):
    my_data = Employee.query.get(id_emp)
    db.session.delete(my_data)
    db.session.commit()
    flash("Employee deleted successfully")

    return redirect(url_for('employee.emp_index'))