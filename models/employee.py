from init_db import db


# create DB model for employee
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
