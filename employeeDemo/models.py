"""Sample file demonstrating SQLAlchemy joins & relationships."""

from flask_sqlalchemy import SQLAlchemy

# This is the connection to the database; we're getting this through
# the Flask-SQLAlchemy helper library. On this, we can find the `session`
# object, where we do most of our interactions (like committing, etc.)

db = SQLAlchemy()


def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)

##############################################################################
# Model definitions


class Employee(db.Model):
    """Employee."""

    __tablename__ = "employees"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    name = db.Column(db.Text, nullable=False, unique=True)
    state = db.Column(db.Text, nullable=False, default='CA')
    dept_code = db.Column(
        db.Text,
        db.ForeignKey('departments.dept_code'))

    dept = db.relationship('Department')

    # direct navigation: emp -> employeeproject & back
    assignments = db.relationship('EmployeeProject',
                                  backref='employee')

    # direct navigation: emp -> project & back
    projects = db.relationship('Project',
                               secondary='employees_projects',
                               backref='employees')

    def __repr__(self):
        e = self
        return f"<Employee {e.id} {e.name} {e.state}>"


class Department(db.Model):
    """Department. A department has many employees."""

    __tablename__ = "departments"

    dept_code = db.Column(db.Text, primary_key=True)
    dept_name = db.Column(db.Text,
                          nullable=False,
                          unique=True)
    phone = db.Column(db.Text)

    employees = db.relationship('Employee')

    def __repr__(self):
        return f"<Department {self.dept_code} {self.dept_name}>"


##############################################################################
# Example queries

# This is inefficient, as it makes a query for each department!


def phone_dir_nav():
    """Show phone dir of emps & their depts."""

    emps = Employee.query.all()

    for emp in emps:  # [<Emp>, <Emp>]
        if emp.dept is not None:
            print(emp.name, emp.dept.dept_code, emp.dept.phone)
        else:
            print(emp.name, "-", "-")


def phone_dir_join():
    """Show employees with a join."""

    emps = (db.session.query(Employee.name,
                             Department.dept_name,
                             Department.phone)
            .join(Department).all())

    for name, dept, phone in emps:  # [(n, d, p), (n, d, p)]
        print(name, dept, phone)


def phone_dir_join_class():
    """Show employees with a join.

    This second version doesn't just get a list of data tuples,
    but a list of tuples of classes.
    """

    emps = (db.session.query(Employee, Department)
            .join(Department).all())

    for emp, dept in emps:  # [(<E>, <D>), (<E>, <D>)]
        print(emp.name, dept.dept_name, dept.phone)


def phone_dir_join_outerjoin():
    """Show all employees, even those without a dept."""

    emps = (db.session.query(Employee, Department)
            .outerjoin(Department).all())

    for emp, dept in emps:  # [(<E>, <D>), (<E>, <D>)]
        if dept:
            print(emp.name, dept.dept_name, dept.phone)
        else:
            print(emp.name, "-", "-")
