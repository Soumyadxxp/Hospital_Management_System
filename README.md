# Hospital Management System (HMS)

A full-stack Hospital Management System built using Streamlit and SQLite. It provides a complete solution for managing patients, doctors, and nurses with authentication, CRUD operations, and scheduling features.
<img width="1600" height="1112" alt="image" src="https://github.com/user-attachments/assets/c5024145-b8b8-41ac-9e3b-df2f3ff5d3eb" />  
<img width="1600" height="1112" alt="image" src="https://github.com/user-attachments/assets/c203ed65-7bc9-4174-84f9-00a5435a02e0" />
<img width="1600" height="1112" alt="image" src="https://github.com/user-attachments/assets/69c48709-6b47-47bd-abf4-88bd11e5f897" />
<img width="1600" height="1112" alt="image" src="https://github.com/user-attachments/assets/d103e356-75e4-4dae-8c9f-006ea23a2ceb" />
<img width="1600" height="1112" alt="image" src="https://github.com/user-attachments/assets/4c3911d1-394d-4604-853f-a9a7fa6c1a5f" />
<img width="1600" height="1112" alt="image" src="https://github.com/user-attachments/assets/ee65f0ef-7882-40ff-9129-c5c5f3ee44cc" />
<img width="1600" height="1112" alt="image" src="https://github.com/user-attachments/assets/6bbb19de-1fa4-4d58-ba7e-1190422607e0" />
<img width="1600" height="1112" alt="image" src="https://github.com/user-attachments/assets/635032b9-be7c-46df-82a0-7e9750817454" />
<img width="1600" height="1112" alt="image" src="https://github.com/user-attachments/assets/db8a04f7-2911-4e6a-a78b-c58305b303c7" />
<img width="1600" height="1112" alt="image" src="https://github.com/user-attachments/assets/3dcaabec-5881-40fc-b4e2-5bc0458f7b50" />
<img width="1600" height="1112" alt="image" src="https://github.com/user-attachments/assets/3598a99d-0052-4c70-8d00-ea00e097e82f" />
<img width="1600" height="1112" alt="image" src="https://github.com/user-attachments/assets/c46f89b5-a754-4e69-90fa-f856b8b156e4" />
<img width="1600" height="1112" alt="image" src="https://github.com/user-attachments/assets/8b9e1715-9109-47fe-add3-dd85e2d127d9" />
<img width="1600" height="1112" alt="image" src="https://github.com/user-attachments/assets/4d900d08-33ce-4bd5-8771-358e2a901f72" />
<img width="1600" height="1112" alt="image" src="https://github.com/user-attachments/assets/eee2982d-47da-4b8a-918e-169d3fde3312" />
<img width="1600" height="1112" alt="image" src="https://github.com/user-attachments/assets/a7498d1b-96aa-4594-94f2-98d8977cc932" />
<img width="1600" height="1112" alt="image" src="https://github.com/user-attachments/assets/1187299d-af0c-4cff-a521-0f44de31d1ad" />
<img width="1600" height="1112" alt="image" src="https://github.com/user-attachments/assets/8b52fe75-f631-4f44-b8be-0f71418681f2" />
<img width="1600" height="1112" alt="image" src="https://github.com/user-attachments/assets/a24f7348-20cf-4838-96e0-2ed9c41d1378" />
<img width="1600" height="1112" alt="image" src="https://github.com/user-attachments/assets/54fdc36b-3ded-4259-bc36-34aa635ddefe" />
<img width="1600" height="1112" alt="image" src="https://github.com/user-attachments/assets/83a3886a-fb64-4fd9-868e-30cb8b0974d7" />

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

# Database Schema

## Patient Table

| Column Name | Data Type | Constraints | Description |
|-------------|-----------|-------------|-------------|
| `PNUM` | INTEGER | PRIMARY KEY | Unique Patient ID |
| `FNAME` | TEXT | NOT NULL | Patient First Name |
| `MNAME` | TEXT | Nullable | Patient Middle Name |
| `LNAME` | TEXT | NOT NULL | Patient Last Name |
| `DID` | TEXT | NOT NULL | Assigned Doctor ID |
| `GENDER` | TEXT | NOT NULL | Gender (M/F/O) |
| `DOB` | TEXT | NOT NULL | Date of Birth (YYYY-MM-DD) |
| `DOA` | TEXT | NOT NULL | Date of Admission |
| `DOD` | TEXT | Nullable | Date of Discharge |
| `WARD` | TEXT | NOT NULL | Ward Number |
| `REASON` | TEXT | NOT NULL | Reason for Admission |

---

## Doctor Table (`doc`)

| Column Name | Data Type | Constraints | Description |
|-------------|-----------|-------------|-------------|
| `DID` | TEXT | PRIMARY KEY | Doctor ID |
| `DFNAME` | TEXT | NOT NULL | Doctor First Name |
| `DMNAME` | TEXT | Nullable | Doctor Middle Name |
| `DLNAME` | TEXT | NOT NULL | Doctor Last Name |
| `FIELD` | TEXT | NOT NULL | Medical Specialization |
| `DOJ` | TEXT | NOT NULL | Date of Joining |

---

## Nurse Table

| Column Name | Data Type | Constraints | Description |
|-------------|-----------|-------------|-------------|
| `NID` | TEXT | PRIMARY KEY | Nurse ID |
| `NFNAME` | TEXT | NOT NULL | Nurse First Name |
| `NMNAME` | TEXT | Nullable | Nurse Middle Name |
| `NLNAME` | TEXT | NOT NULL | Nurse Last Name |
| `WARD` | TEXT | NOT NULL | Assigned Ward |
| `DOJ` | TEXT | NOT NULL | Date of Joining |

---

## Doctor Schedule Table (`dtime`)

| Column Name | Data Type | Constraints | Description |
|-------------|-----------|-------------|-------------|
| `DID` | TEXT | PRIMARY KEY | Doctor ID |
| `MON` | TEXT | Nullable | Monday Schedule |
| `TUE` | TEXT | Nullable | Tuesday Schedule |
| `WED` | TEXT | Nullable | Wednesday Schedule |
| `THU` | TEXT | Nullable | Thursday Schedule |
| `FRI` | TEXT | Nullable | Friday Schedule |
| `SAT` | TEXT | Nullable | Saturday Schedule |
| `SUN` | TEXT | Nullable | Sunday Schedule |

---

## User Credentials Table (`usr_pwd`)

| Column Name | Data Type | Constraints | Description |
|-------------|-----------|-------------|-------------|
| `USERNAME` | TEXT | PRIMARY KEY | Login Username |
| `PASSWORD` | TEXT | NOT NULL | User Password |

---

# Entity Relationships

| Parent Table | Child Table | Relationship |
|--------------|-------------|--------------|
| `doc` | `Patient` | One doctor can be assigned to multiple patients through `DID`. |
| `doc` | `dtime` | One doctor has one weekly schedule through `DID`. |
| `nurse` | `Patient` | Nurses are associated with patients through the assigned `WARD`. |
| `usr_pwd` | Application | Stores user login credentials for authentication. |

# Entity Relationship (ER) Diagram

```mermaid
erDiagram

    PATIENT {
        INTEGER PNUM PK
        TEXT FNAME
        TEXT MNAME
        TEXT LNAME
        TEXT DID FK
        TEXT GENDER
        TEXT DOB
        TEXT DOA
        TEXT DOD
        TEXT WARD
        TEXT REASON
    }

    DOCTOR {
        TEXT DID PK
        TEXT DFNAME
        TEXT DMNAME
        TEXT DLNAME
        TEXT FIELD
        TEXT DOJ
    }

    NURSE {
        TEXT NID PK
        TEXT NFNAME
        TEXT NMNAME
        TEXT NLNAME
        TEXT WARD
        TEXT DOJ
    }

    DOCTOR_SCHEDULE {
        TEXT DID PK
        TEXT MON
        TEXT TUE
        TEXT WED
        TEXT THU
        TEXT FRI
        TEXT SAT
        TEXT SUN
    }

    USER_LOGIN {
        TEXT USERNAME PK
        TEXT PASSWORD
    }

    DOCTOR ||--o{ PATIENT : "Treats"

    DOCTOR ||--|| DOCTOR_SCHEDULE : "Has"

    NURSE }o--o{ PATIENT : "Assigned to Ward"

    USER_LOGIN {
        TEXT USERNAME
        TEXT PASSWORD
    }
```

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
