from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.department import Department
from init_db import db


department = Blueprint("department", __name__)


@department.route('/department')
def dep_index():
    all_data = Department.query.all()

    return render_template("departments_index.html", departments=all_data)


@department.route('/department/insert', methods=['POST'])
def dep_insert():
    if request.method == 'POST':
        dep_name = request.form['dep_name']
        description = request.form['description']

        my_data = Department(dep_name, description)
        db.session.add(my_data)
        db.session.commit()

        flash("Department inserted successfully")

        return redirect(url_for('department.dep_index'))


@department.route('/department/update', methods=['GET', 'POST'])
def dep_update():
    if request.method == 'POST':
        my_data = Department.query.get(request.form.get('id_dep'))

        my_data.dep_name = request.form['dep_name']
        my_data.description = request.form['description']

        db.session.commit()
        flash("Department updated successfully")

        return redirect(url_for('department.dep_index'))


@department.route('/department/delete/<id_dep>/', methods=['GET', 'POST'])
def dep_delete(id_dep):
    my_data = Department.query.get(id_dep)
    db.session.delete(my_data)
    db.session.commit()
    flash("Department deleted successfully")

    return redirect(url_for('department.dep_index'))
