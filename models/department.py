from init_db import db


# create DB model for department
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
