from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
import models, schemas
from datetime import date

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Add Employee
@app.post("/employees")
def add_employee(emp: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    existing = db.query(models.Employee).filter(
        (models.Employee.employee_id == emp.employee_id) |
        (models.Employee.email == emp.email)
    ).first()

    if existing:
        raise HTTPException(status_code=400, detail="Employee ID or Email already exists")

    new_emp = models.Employee(**emp.dict())
    db.add(new_emp)
    db.commit()
    db.refresh(new_emp)
    return {"message": "Employee added successfully"}

# Get Employees
@app.get("/employees")
def get_employees(db: Session = Depends(get_db)):
    return db.query(models.Employee).all()

# Delete Employee
@app.delete("/employees/{emp_id}")
def delete_employee(emp_id: int, db: Session = Depends(get_db)):
    emp = db.query(models.Employee).filter(models.Employee.id == emp_id).first()
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")
    db.delete(emp)
    db.commit()
    return {"message": "Employee deleted"}

# Mark Attendance
@app.post("/attendance")
def mark_attendance(att: schemas.AttendanceCreate, db: Session = Depends(get_db)):
    emp = db.query(models.Employee).filter(models.Employee.id == att.employee_id).first()
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")

    new_att = models.Attendance(**att.dict())
    db.add(new_att)
    db.commit()
    return {"message": "Attendance marked"}

# Get Attendance by Employee
@app.get("/attendance/{emp_id}")
def get_attendance(emp_id: int, db: Session = Depends(get_db)):
    return db.query(models.Attendance).filter(models.Attendance.employee_id == emp_id).all()
