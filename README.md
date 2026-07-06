# Hospital Management System (HMS)

A full-stack Hospital Management System built using Streamlit and SQLite. It provides a complete solution for managing patients, doctors, and nurses with authentication, CRUD operations, and scheduling features.
<img width="1600" height="1112" alt="image" src="https://github.com/user-attachments/assets/c5024145-b8b8-41ac-9e3b-df2f3ff5d3eb" />
<img width="1600" height="1112" alt="image" src="https://github.com/user-attachments/assets/c203ed65-7bc9-4174-84f9-00a5435a02e0" />
<img width="1600" height="1112" alt="image" src="https://github.com/user-attachments/assets/69c48709-6b47-47bd-abf4-88bd11e5f897" />
<img width="1600" height="1112" alt="image" src="https://github.com/user-attachments/assets/d103e356-75e4-4dae-8c9f-006ea23a2ceb" />

---

## Features

### User Authentication
- User Registration
- Login and Logout system
- Password reset (Forgot Password)
- Session-based access control using Streamlit session state

---

### Patient Management
- Add new patients with auto-generated ID
- View all patients in table format
- Search patients by Patient ID or Name
- Modify patient details:
  - Name
  - Doctor assignment
  - Gender
  - DOB / DOA / DOD
  - Ward
  - Reason for admission
- Doctor ID validation
- Age calculation from DOB

---

### Doctor Management
- View all doctors
- Search doctor by ID or name
- View doctor profile with:
  - Specialization
  - Date of Joining
- Weekly schedule (Mon–Sun)

---

### Nurse Management
- View all nurses
- Search nurse by ID or name
- Filter nurses by ward
- View nurse details:
  - Ward
  - Date of Joining

---

## Database (SQLite)

- Database file: `hms.db`
- Auto-created on first run
- Preloaded sample data included

Tables:
- usr_pwd
- Patient
- doc
- nurse
- dtime

---

## Tech Stack

- Streamlit (Frontend + UI)
- Python (Backend logic)
- SQLite3 (Database)

Libraries:
- streamlit
- sqlite3
- datetime

---

## Project Structure

hms.py - Main application file  
hms.db - SQLite database (auto-generated)

---

## Default Behavior

- Database is created automatically on first run
- Sample data is inserted if database is empty
- No default admin account; user must register

---

## Key Highlights

- Fully interactive Streamlit web application
- Secure SQL queries using parameterized inputs
- Modular architecture:
  - UserAuth
  - PatientOps
  - DoctorOps
  - NurseOps
- Strong input validation
- Clean tabular data presentation

---

## Author

Soumyadeep Basu

---
