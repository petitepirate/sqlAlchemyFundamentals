from models import Department, Employee, db
from app import app

db.drop_all()
db.create_all()

d1 = Department(dept_code="mktg", dept_name="Marketing", phone="899-0909")
d2 = Department(dept_code="acct", dept_name="Accounting", phone="111-5432")
d3 = Department(dept_code="it", dept_name="Tech", phone="111-5933")
d4 = Department(dept_code="hr", dept_name="Human Resources", phone="121-5436")


river = Employee(name="River Bottom", state="NY", dept_code="mktg")
joan = Employee(name="Joan Rivers", state="CA", dept_code="acct")
sam = Employee(name="Samwell Tarley", state="CA", dept_code="acct")
jim = Employee(name="Jim Barkazi", state="CA", dept_code="acct")
lacey = Employee(name="Lacey Price", state="CA", dept_code="acct")

db.session.add(d1)
db.session.add(d2)
db.session.add(d3)
db.session.add(d4)
db.session.commit()

db.session.add(river)
db.session.add(joan)
db.session.add(jim)
db.session.add(sam)
db.session.add(lacey)
db.session.commit()
