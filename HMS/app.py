import streamlit as st
import sqlite3
import datetime

# --------------------- DATABASE SETUP ---------------------
DB_PATH = "hms.db"

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_connection()
    c = conn.cursor()
    # Tables
    c.execute('''CREATE TABLE IF NOT EXISTS usr_pwd (
        USERNAME TEXT PRIMARY KEY,
        PASSWORD TEXT NOT NULL
    )''')
    c.execute('''CREATE TABLE IF NOT EXISTS Patient (
        PNUM INTEGER PRIMARY KEY,
        FNAME TEXT NOT NULL,
        MNAME TEXT,
        LNAME TEXT NOT NULL,
        DID TEXT NOT NULL,
        GENDER TEXT NOT NULL,
        DOB TEXT NOT NULL,
        DOA TEXT NOT NULL,
        DOD TEXT,
        WARD TEXT NOT NULL,
        REASON TEXT NOT NULL
    )''')
    c.execute('''CREATE TABLE IF NOT EXISTS doc (
        DID TEXT PRIMARY KEY,
        DFNAME TEXT NOT NULL,
        DMNAME TEXT,
        DLNAME TEXT NOT NULL,
        FIELD TEXT NOT NULL,
        DOJ TEXT NOT NULL
    )''')
    c.execute('''CREATE TABLE IF NOT EXISTS nurse (
        NID TEXT PRIMARY KEY,
        NFNAME TEXT NOT NULL,
        NMNAME TEXT,
        NLNAME TEXT NOT NULL,
        WARD TEXT NOT NULL,
        DOJ TEXT NOT NULL
    )''')
    c.execute('''CREATE TABLE IF NOT EXISTS dtime (
        DID TEXT PRIMARY KEY,
        MON TEXT,
        TUE TEXT,
        WED TEXT,
        THU TEXT,
        FRI TEXT,
        SAT TEXT,
        SUN TEXT
    )''')

    # Insert sample data if empty
    c.execute("SELECT COUNT(*) FROM Patient")
    if c.fetchone()[0] == 0:
        sample_patient = [
            (1, 'AMIT', None, 'SHARMA', 'D007', 'M', '1980-01-01', '2024-01-01', '2024-01-10', 'W03', 'ROUTINE HEALTH CHECKUP'),
            (2, 'SUNITA', 'KUMARI', 'SINGH', 'D003', 'F', '1985-02-02', '2024-01-02', None, 'W07', 'UNDERGOING SURGERY FOR APPENDICITIS'),
            (3, 'RAJESH', None, 'GUPTA', 'D010', 'M', '1990-03-03', '2024-01-03', '2024-01-13', 'W02', 'ROUTINE HEALTH CHECKUP'),
            (4, 'ANITA', None, 'YADAV', 'D001', 'F', '1995-04-04', '2024-01-04', None, 'W10', 'UNDERGOING SURGERY FOR GALLSTONES'),
            (5, 'RAVI', 'KUMAR', 'VERMA', 'D006', 'M', '2000-05-05', '2024-01-05', '2024-01-15', 'W01', 'ROUTINE HEALTH CHECKUP'),
            (6, 'POOJA', None, 'PATEL', 'D002', 'F', '2005-06-06', '2024-01-06', '2024-01-16', 'W06', 'UNDERGOING SURGERY FOR HERNIA'),
            (7, 'VIJAY', None, 'CHAUDHARY', 'D009', 'M', '2010-07-07', '2024-01-07', None, 'W04', 'ROUTINE HEALTH CHECKUP'),
            (8, 'REKHA', 'DEVI', 'JHA', 'D004', 'F', '2015-08-08', '2024-01-08', '2024-01-18', 'W09', 'UNDERGOING SURGERY FOR CATARACT'),
            (9, 'SANJAY', None, 'JAIN', 'D005', 'M', '2020-09-09', '2024-01-09', '2024-01-19', 'W05', 'ROUTINE HEALTH CHECKUP'),
            (10, 'KIRAN', None, 'AGARWAL', 'D008', 'F', '2021-10-10', '2024-01-10', None, 'W08', 'UNDERGOING SURGERY FOR KNEE REPLACEMENT'),
            (11, 'RAHUL', None, 'KHANNA', 'D001', 'M', '1981-11-11', '2024-01-11', '2024-01-21', 'W06', 'ROUTINE HEALTH CHECKUP'),
            (12, 'GEETA', None, 'SRIVASTAVA', 'D006', 'F', '1986-12-12', '2024-01-12', None, 'W01', 'UNDERGOING SURGERY FOR HIP REPLACEMENT'),
            (13, 'SUNIL', None, 'KAPOOR', 'D003', 'M', '1991-01-13', '2024-01-13', '2024-01-23', 'W07', 'ROUTINE HEALTH CHECKUP'),
            (14, 'MEENA', None, 'RANA', 'D010', 'F', '1996-02-14', '2024-01-14', '2024-01-24', 'W02', 'UNDERGOING SURGERY FOR TONSILLECTOMY'),
            (15, 'ANIL', None, 'MALHOTRA', 'D002', 'M', '2001-03-15', '2024-01-15', None, 'W10', 'ROUTINE HEALTH CHECKUP'),
            (16, 'SARITA', None, 'DAS', 'D009', 'F', '2006-04-16', '2024-01-16', '2024-01-26', 'W03', 'UNDERGOING SURGERY FOR SINUSITIS'),
            (17, 'RAKESH', None, 'MEHRA', 'D004', 'M', '2011-05-17', '2024-01-17', None, 'W04', 'ROUTINE HEALTH CHECKUP'),
            (18, 'SEEMA', None, 'BISWAS', 'D007', 'F', '2016-06-18', '2024-01-18', '2024-01-28', 'W08', 'UNDERGOING SURGERY FOR ADENOIDECTOMY'),
            (19, 'RAJIV', None, 'NAIR', 'D008', 'M', '2021-07-19', '2024-01-19', '2024-01-29', 'W06', 'ROUTINE HEALTH CHECKUP'),
            (20, 'SAVITA', None, 'PANDEY', 'D005', 'F', '2022-08-20', '2024-01-20', '2024-01-30', 'W09', 'UNDERGOING SURGERY FOR MASTECTOMY'),
            (21, 'AMIT', None, 'SHARMA', 'D010', 'M', '1990-01-01', '2024-01-01', '2024-01-10', 'W03', 'ROUTINE HEALTH CHECKUP')
        ]
        c.executemany('''INSERT INTO Patient (PNUM, FNAME, MNAME, LNAME, DID, GENDER, DOB, DOA, DOD, WARD, REASON)
                         VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', sample_patient)

    c.execute("SELECT COUNT(*) FROM doc")
    if c.fetchone()[0] == 0:
        sample_doc = [
            ('D001', 'ANAND', 'KUMAR', 'GUPTA', 'GASTROENTEROLOGIST', '2000-01-01'),
            ('D002', 'BHARTI', None, 'PATEL', 'ORTHOPEDIC', '2005-02-02'),
            ('D003', 'CHETAN', 'SINGH', 'SINGH', 'GYNECOLOGIST', '2010-03-03'),
            ('D004', 'DEEPA', None, 'JHA', 'OPHTHALMOLOGIST', '2015-04-04'),
            ('D005', 'ESHA', 'RAJ', 'JAIN', 'PEDIATRICIAN', '2020-05-05'),
            ('D006', 'FARHAN', None, 'VERMA', 'ORTHOPEDIC', '2021-06-06'),
            ('D007', 'GAURAV', 'KUMAR', 'SHARMA', 'CARDIOLOGIST', '2015-07-07'),
            ('D008', 'HEMA', None, 'AGARWAL', 'SURGEON', '2010-08-08'),
            ('D009', 'ISHA', None, 'CHAUDHARY', 'ENT SPECIALIST', '2005-09-09'),
            ('D010', 'JAYA', 'DEVI', 'GUPTA', 'DERMATOLOGIST', '2000-10-10'),
            ('D011', 'ANAND', 'KUMAR', 'GUPTA', 'ENT SPECIALIST', '2003-01-01')
        ]
        c.executemany('''INSERT INTO doc (DID, DFNAME, DMNAME, DLNAME, FIELD, DOJ)
                         VALUES (?, ?, ?, ?, ?, ?)''', sample_doc)

    c.execute("SELECT COUNT(*) FROM nurse")
    if c.fetchone()[0] == 0:
        sample_nurse = [
            ('N001', 'PRIYA', 'KUMARI', 'SHARMA', 'W03', '2005-01-15'),
            ('N002', 'RAHUL', 'SINGH', 'MEHTA', 'W08', '2010-02-22'),
            ('N003', 'ANITA', None, 'YADAV', 'W05', '2015-03-30'),
            ('N004', 'VIKRAM', 'RAJ', 'VERMA', 'W02', '2020-04-10'),
            ('N005', 'NISHA', None, 'GUPTA', 'W10', '2021-05-12'),
            ('N006', 'ARJUN', 'KUMAR', 'SINGH', 'W06', '2010-06-18'),
            ('N007', 'ANJALI', None, 'CHAUDHARY', 'W01', '2015-07-25'),
            ('N008', 'RAVI', 'KUMAR', 'JHA', 'W09', '2020-08-30'),
            ('N009', 'SARITA', None, 'YADAV', 'W04', '2005-09-05'),
            ('N010', 'SUMIT', 'SINGH', 'RAJPUT', 'W07', '2010-10-12'),
            ('N011', 'NEHA', 'RAJ', 'SHARMA', 'W02', '2015-11-15'),
            ('N012', 'ROHIT', None, 'MEHTA', 'W10', '2020-12-22'),
            ('N013', 'POOJA', 'KUMARI', 'YADAV', 'W08', '2008-01-30'),
            ('N014', 'VIJAY', None, 'VERMA', 'W03', '2012-02-10'),
            ('N015', 'ANJU', 'DEVI', 'GUPTA', 'W05', '2017-03-12'),
            ('N016', 'RAMESH', None, 'SINGH', 'W01', '2019-04-18'),
            ('N017', 'KIRAN', 'KUMARI', 'CHAUDHARY', 'W06', '2014-05-25'),
            ('N018', 'SUNIL', None, 'JHA', 'W04', '2011-06-30'),
            ('N019', 'PRIYANKA', 'KUMARI', 'YADAV', 'W09', '2016-07-05'),
            ('N020', 'RISHABH', 'KUMAR', 'RAJPUT', 'W07', '2013-08-12'),
            ('N021', 'MANISH', None, 'SHARMA', 'W01', '2018-09-15'),
            ('N022', 'SIMRAN', 'KUMARI', 'MEHTA', 'W04', '2007-10-22'),
            ('N023', 'AJAY', None, 'YADAV', 'W10', '2012-11-30'),
            ('N024', 'KAVITA', 'DEVI', 'VERMA', 'W06', '2014-12-10'),
            ('N025', 'SANDEEP', None, 'GUPTA', 'W03', '2019-01-12'),
            ('N026', 'PRIYA', 'KUMARI', 'SHARMA', 'W05', '2009-03-15')
        ]
        c.executemany('''INSERT INTO nurse (NID, NFNAME, NMNAME, NLNAME, WARD, DOJ)
                         VALUES (?, ?, ?, ?, ?, ?)''', sample_nurse)

    c.execute("SELECT COUNT(*) FROM dtime")
    if c.fetchone()[0] == 0:
        sample_dtime = [
            ('D001', '09:00-17:00', None, '09:00-17:00', None, '09:00-17:00', '10:00-14:00', None),
            ('D002', '08:30-16:30', '08:30-16:30', None, '08:30-16:30', '08:30-16:30', None, '10:30-15:30'),
            ('D003', None, '10:00-18:00', '10:00-18:00', '10:00-18:00', None, '11:00-15:00', None),
            ('D004', '08:00-16:00', None, '08:00-16:00', None, '08:00-16:00', None, '09:00-14:00'),
            ('D005', '09:30-17:30', '09:30-17:30', '09:30-17:30', '09:30-17:30', '09:30-17:30', '10:30-14:30', None),
            ('D006', None, '10:30-18:30', None, '10:30-18:30', '10:30-18:30', None, '11:30-16:30'),
            ('D007', '08:00-16:00', None, '08:00-16:00', None, '08:00-16:00', '09:00-13:00', None),
            ('D008', '09:30-17:30', '09:30-17:30', None, '09:30-17:30', '09:30-17:30', None, '10:30-15:30'),
            ('D009', None, '11:00-19:00', '11:00-19:00', '11:00-19:00', '11:00-19:00', '12:00-16:00', None),
            ('D010', '08:30-16:30', None, '08:30-16:30', '08:30-16:30', '08:30-16:30', None, '09:30-14:30'),
            ('D011', None, '12:00-16:00', '13:00-15:00', '14:00-19:00', '11:00-17:00', '12:00-16:30', None)
        ]
        c.executemany('''INSERT INTO dtime (DID, MON, TUE, WED, THU, FRI, SAT, SUN)
                         VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', sample_dtime)

    conn.commit()
    conn.close()

# --------------------- HELPER FUNCTIONS ---------------------
def display_patient(pid):
    conn = get_connection()
    row = conn.execute("SELECT * FROM Patient WHERE PNUM = ?", (pid,)).fetchone()
    conn.close()
    if row:
        st.subheader("Patient Details")
        st.write(f"**PID:** {row['PNUM']}")
        name = row['FNAME'] + (" " + row['MNAME'] if row['MNAME'] else "") + " " + row['LNAME']
        st.write(f"**Name:** {name}")
        gender = {'M':'Male','F':'Female','O':'Others'}.get(row['GENDER'], row['GENDER'])
        st.write(f"**Gender:** {gender}")
        st.write(f"**DOB:** {row['DOB']}")
        age = datetime.datetime.now().year - int(row['DOB'][:4])
        st.write(f"**Age:** {age}")
        st.write(f"**Doctor ID:** {row['DID']}")
        drow = get_connection().execute("SELECT * FROM doc WHERE DID = ?", (row['DID'],)).fetchone()
        if drow:
            dname = "Dr. " + drow['DFNAME'] + (" " + drow['DMNAME'] if drow['DMNAME'] else "") + " " + drow['DLNAME']
            st.write(f"**Doctor:** {dname}")
        st.write(f"**Admission:** {row['DOA']}")
        st.write(f"**Discharge:** {row['DOD'] if row['DOD'] else 'Not yet'}")
        st.write(f"**Ward:** {row['WARD']}")
        st.write(f"**Reason:** {row['REASON']}")
    else:
        st.error("Patient not found.")

def display_patients_table(rows):
    if not rows:
        st.info("No patients found.")
        return
    data = []
    for r in rows:
        drow = get_connection().execute("SELECT * FROM doc WHERE DID = ?", (r['DID'],)).fetchone()
        dname = "Dr. " + drow['DFNAME'] + (" " + drow['DMNAME'] if drow['DMNAME'] else "") + " " + drow['DLNAME'] if drow else "Unknown"
        data.append({
            "PID": r['PNUM'],
            "First": r['FNAME'],
            "Middle": r['MNAME'] or "",
            "Last": r['LNAME'],
            "Gender": {'M':'Male','F':'Female','O':'Others'}.get(r['GENDER'], r['GENDER']),
            "Doctor": dname,
            "Admission": r['DOA'],
            "Discharge": r['DOD'] or "—",
            "Ward": r['WARD'],
            "Reason": r['REASON']
        })
    st.dataframe(data, use_container_width=True)

def date_input(label):
    col1, col2, col3 = st.columns(3)
    with col1:
        year = st.number_input(f"{label} Year", min_value=1900, max_value=datetime.datetime.now().year, step=1, value=2000, key=f"{label}_year")
    with col2:
        month = st.number_input(f"{label} Month", min_value=1, max_value=12, step=1, value=1, key=f"{label}_month")
    with col3:
        day = st.number_input(f"{label} Day", min_value=1, max_value=31, step=1, value=1, key=f"{label}_day")
    try:
        return datetime.date(year, month, day).isoformat()
    except:
        return None

# --------------------- CLASSES ---------------------
class UserAuth:
    def register(self):
        st.subheader("Sign Up")
        with st.form("register"):
            username = st.text_input("Username (alphanumeric, max 15)")
            password = st.text_input("Password (no spaces, max 15)", type="password")
            if st.form_submit_button("Register"):
                if not username.isalnum() or len(username)>15 or " " in username:
                    st.error("Invalid username.")
                    return
                if not password or len(password)>15 or " " in password:
                    st.error("Invalid password.")
                    return
                conn = get_connection()
                cur = conn.cursor()
                cur.execute("SELECT COUNT(*) FROM usr_pwd WHERE USERNAME = ?", (username,))
                if cur.fetchone()[0] > 0:
                    st.error("Username already taken.")
                else:
                    cur.execute("INSERT INTO usr_pwd (USERNAME, PASSWORD) VALUES (?, ?)", (username, password))
                    conn.commit()
                    st.success("Registration successful! Please log in.")
                conn.close()

    def login(self):
        st.subheader("Sign In")
        with st.form("login"):
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            if st.form_submit_button("Login"):
                conn = get_connection()
                cur = conn.cursor()
                cur.execute("SELECT PASSWORD FROM usr_pwd WHERE USERNAME = ?", (username,))
                row = cur.fetchone()
                conn.close()
                if row and row['PASSWORD'] == password:
                    st.session_state.logged_in = True
                    st.session_state.username = username
                    st.success(f"Welcome, {username}!")
                    st.rerun()
                else:
                    st.error("Invalid credentials.")

    def forgot(self):
        st.subheader("Change Password")
        with st.form("forgot"):
            username = st.text_input("Username")
            new_pass = st.text_input("New Password (no spaces, max 15)", type="password")
            if st.form_submit_button("Update"):
                if not username or not new_pass or len(new_pass)>15 or " " in new_pass:
                    st.error("Invalid input.")
                    return
                conn = get_connection()
                cur = conn.cursor()
                cur.execute("SELECT COUNT(*) FROM usr_pwd WHERE USERNAME = ?", (username,))
                if cur.fetchone()[0] == 1:
                    cur.execute("UPDATE usr_pwd SET PASSWORD = ? WHERE USERNAME = ?", (new_pass, username))
                    conn.commit()
                    st.success("Password updated.")
                else:
                    st.error("Username not found.")
                conn.close()

class PatientOps:
    def add(self):
        st.subheader("Add New Patient")
        with st.form("add_patient"):
            conn = get_connection()
            cur = conn.cursor()
            cur.execute("SELECT MAX(PNUM) FROM Patient")
            max_pid = cur.fetchone()[0] or 0
            next_pid = max_pid + 1
            conn.close()
            st.write(f"**Auto PID:** {next_pid}")
            fname = st.text_input("First Name").strip().upper()
            mname = st.text_input("Middle Name (optional)").strip().upper() or None
            lname = st.text_input("Last Name").strip().upper()
            did = st.text_input("Doctor ID (e.g., D000)").strip().upper()
            gender = st.selectbox("Gender", ["M","F","O"])
            dob = date_input("DOB")
            doa = date_input("DOA")
            dod = date_input("DOD (optional)") if st.checkbox("Enter DOD") else None
            ward = st.text_input("Ward (e.g., W01)").strip().upper()
            reason = st.text_input("Reason for admission").strip().upper()

            if st.form_submit_button("Add Patient"):
                if not fname or not lname or not did or not ward or not reason:
                    st.error("Required fields missing.")
                    return
                if not fname.isalpha() or not lname.isalpha() or (mname and not mname.isalpha()):
                    st.error("Names must be alphabetic.")
                    return
                if len(did)!=4 or did[0]!='D':
                    st.error("Doctor ID must be like D000.")
                    return
                if len(ward)!=3 or ward[0]!='W' or ward=='W00':
                    st.error("Ward must be W01..W99.")
                    return
                if not dob or not doa:
                    st.error("Invalid date.")
                    return
                conn = get_connection()
                cur = conn.cursor()
                cur.execute("SELECT COUNT(*) FROM doc WHERE DID = ?", (did,))
                if cur.fetchone()[0] == 0:
                    st.error("Doctor ID not found.")
                    conn.close()
                    return
                cur.execute('''INSERT INTO Patient (PNUM, FNAME, MNAME, LNAME, DID, GENDER, DOB, DOA, DOD, WARD, REASON)
                               VALUES (?,?,?,?,?,?,?,?,?,?,?)''',
                            (next_pid, fname, mname, lname, did, gender, dob, doa, dod, ward, reason))
                conn.commit()
                conn.close()
                st.success("Patient added!")
                display_patient(next_pid)

    def view_all(self):
        st.subheader("All Patients")
        conn = get_connection()
        rows = conn.execute("SELECT * FROM Patient ORDER BY PNUM").fetchall()
        conn.close()
        display_patients_table(rows)

    def search_by_id(self):
        st.subheader("Search by Patient ID")
        pid = st.number_input("Enter PID", min_value=1, step=1)
        if st.button("Search"):
            display_patient(pid)

    def search_by_name(self):
        st.subheader("Search by Name")
        fname = st.text_input("First Name").strip().upper()
        mname = st.text_input("Middle Name (optional)").strip().upper() or None
        lname = st.text_input("Last Name").strip().upper()
        if st.button("Search"):
            if not fname or not lname:
                st.error("First and last names required.")
                return
            conn = get_connection()
            if mname:
                rows = conn.execute("SELECT * FROM Patient WHERE FNAME=? AND MNAME=? AND LNAME=?", (fname, mname, lname)).fetchall()
            else:
                rows = conn.execute("SELECT * FROM Patient WHERE FNAME=? AND LNAME=?", (fname, lname)).fetchall()
            conn.close()
            if rows:
                display_patients_table(rows)
                if len(rows) == 1:
                    display_patient(rows[0]['PNUM'])
            else:
                st.info("No patient found.")

    def modify(self):
        st.subheader("Modify Patient")
        pid = st.number_input("Enter PID to modify", min_value=1, step=1)
        if st.button("Load Patient"):
            display_patient(pid)
            st.session_state.mod_pid = pid

        if 'mod_pid' in st.session_state and st.session_state.mod_pid == pid:
            choice = st.selectbox("What to modify?", ["Name", "Doctor", "Gender", "DOB", "DOA", "DOD", "Ward", "Reason"])
            with st.form("modify_form"):
                if choice == "Name":
                    new_f = st.text_input("New First Name").strip().upper()
                    new_m = st.text_input("New Middle Name (optional)").strip().upper() or None
                    new_l = st.text_input("New Last Name").strip().upper()
                    if st.form_submit_button("Update Name"):
                        if not new_f or not new_l:
                            st.error("First and last required.")
                        else:
                            conn = get_connection()
                            conn.execute("UPDATE Patient SET FNAME=?, MNAME=?, LNAME=? WHERE PNUM=?", (new_f, new_m, new_l, pid))
                            conn.commit()
                            conn.close()
                            st.success("Updated.")
                            display_patient(pid)
                elif choice == "Doctor":
                    new_did = st.text_input("New Doctor ID").strip().upper()
                    if st.form_submit_button("Update Doctor"):
                        if not new_did or len(new_did)!=4 or new_did[0]!='D':
                            st.error("Invalid format.")
                        else:
                            conn = get_connection()
                            cur = conn.cursor()
                            cur.execute("SELECT COUNT(*) FROM doc WHERE DID = ?", (new_did,))
                            if cur.fetchone()[0] == 0:
                                st.error("Doctor not found.")
                            else:
                                cur.execute("UPDATE Patient SET DID=? WHERE PNUM=?", (new_did, pid))
                                conn.commit()
                                st.success("Updated.")
                                display_patient(pid)
                            conn.close()
                elif choice == "Gender":
                    new_g = st.selectbox("New Gender", ["M","F","O"])
                    if st.form_submit_button("Update Gender"):
                        conn = get_connection()
                        conn.execute("UPDATE Patient SET GENDER=? WHERE PNUM=?", (new_g, pid))
                        conn.commit()
                        conn.close()
                        st.success("Updated.")
                        display_patient(pid)
                elif choice == "DOB":
                    new_dob = date_input("New DOB")
                    if new_dob and st.form_submit_button("Update DOB"):
                        conn = get_connection()
                        conn.execute("UPDATE Patient SET DOB=? WHERE PNUM=?", (new_dob, pid))
                        conn.commit()
                        conn.close()
                        st.success("Updated.")
                        display_patient(pid)
                elif choice == "DOA":
                    new_doa = date_input("New DOA")
                    if new_doa and st.form_submit_button("Update DOA"):
                        conn = get_connection()
                        conn.execute("UPDATE Patient SET DOA=? WHERE PNUM=?", (new_doa, pid))
                        conn.commit()
                        conn.close()
                        st.success("Updated.")
                        display_patient(pid)
                elif choice == "DOD":
                    new_dod = date_input("New DOD (leave empty to clear)")
                    if st.form_submit_button("Update DOD"):
                        conn = get_connection()
                        conn.execute("UPDATE Patient SET DOD=? WHERE PNUM=?", (new_dod, pid))
                        conn.commit()
                        conn.close()
                        st.success("Updated.")
                        display_patient(pid)
                elif choice == "Ward":
                    new_ward = st.text_input("New Ward").strip().upper()
                    if st.form_submit_button("Update Ward"):
                        if not new_ward or len(new_ward)!=3 or new_ward[0]!='W' or new_ward=='W00':
                            st.error("Invalid ward.")
                        else:
                            conn = get_connection()
                            conn.execute("UPDATE Patient SET WARD=? WHERE PNUM=?", (new_ward, pid))
                            conn.commit()
                            conn.close()
                            st.success("Updated.")
                            display_patient(pid)
                elif choice == "Reason":
                    new_reason = st.text_input("New Reason").strip().upper()
                    if st.form_submit_button("Update Reason"):
                        if not new_reason:
                            st.error("Reason cannot be empty.")
                        else:
                            conn = get_connection()
                            conn.execute("UPDATE Patient SET REASON=? WHERE PNUM=?", (new_reason, pid))
                            conn.commit()
                            conn.close()
                            st.success("Updated.")
                            display_patient(pid)

class DoctorOps:
    def view_all(self):
        st.subheader("All Doctors")
        conn = get_connection()
        rows = conn.execute("SELECT * FROM doc ORDER BY DID").fetchall()
        conn.close()
        if rows:
            data = []
            for r in rows:
                data.append({
                    "DID": r['DID'],
                    "First": r['DFNAME'],
                    "Middle": r['DMNAME'] or "",
                    "Last": r['DLNAME'],
                    "Specialization": r['FIELD'],
                    "DOJ": r['DOJ']
                })
            st.dataframe(data, use_container_width=True)
        else:
            st.info("No doctors found.")

    def view_schedule(self):
        st.subheader("All Doctors with Weekly Schedule")
        conn = get_connection()
        rows = conn.execute("SELECT * FROM dtime ORDER BY DID").fetchall()
        data = []
        for r in rows:
            drow = conn.execute("SELECT * FROM doc WHERE DID = ?", (r['DID'],)).fetchone()
            if drow:
                dname = "Dr. " + drow['DFNAME'] + (" " + drow['DMNAME'] if drow['DMNAME'] else "") + " " + drow['DLNAME']
            else:
                dname = "Unknown"
            data.append({
                "DID": r['DID'],
                "Doctor": dname,
                "Mon": r['MON'] or "—",
                "Tue": r['TUE'] or "—",
                "Wed": r['WED'] or "—",
                "Thu": r['THU'] or "—",
                "Fri": r['FRI'] or "—",
                "Sat": r['SAT'] or "—",
                "Sun": r['SUN'] or "—"
            })
        conn.close()
        if data:
            st.dataframe(data, use_container_width=True)
        else:
            st.info("No schedule data.")

    def search_by_id(self):
        st.subheader("Search Doctor by ID")
        did = st.text_input("Doctor ID").strip().upper()
        if st.button("Search"):
            conn = get_connection()
            row = conn.execute("SELECT * FROM doc WHERE DID = ?", (did,)).fetchone()
            conn.close()
            if row:
                self._display_single(row)
            else:
                st.error("Not found.")

    def search_by_name(self):
        st.subheader("Search Doctor by Name")
        fname = st.text_input("First Name").strip().upper()
        mname = st.text_input("Middle Name (optional)").strip().upper() or None
        lname = st.text_input("Last Name").strip().upper()
        if st.button("Search"):
            if not fname or not lname:
                st.error("First and last required.")
                return
            conn = get_connection()
            if mname:
                rows = conn.execute("SELECT * FROM doc WHERE DFNAME=? AND DMNAME=? AND DLNAME=?", (fname, mname, lname)).fetchall()
            else:
                rows = conn.execute("SELECT * FROM doc WHERE DFNAME=? AND DLNAME=?", (fname, lname)).fetchall()
            conn.close()
            if rows:
                # show table
                data = [{"DID": r['DID'], "First": r['DFNAME'], "Middle": r['DMNAME'] or "", "Last": r['DLNAME'], "Field": r['FIELD'], "DOJ": r['DOJ']} for r in rows]
                st.dataframe(data, use_container_width=True)
                if len(rows)==1:
                    self._display_single(rows[0])
            else:
                st.info("No doctor found.")

    def _display_single(self, row):
        st.subheader("Doctor Details")
        st.write(f"**DID:** {row['DID']}")
        name = "Dr. " + row['DFNAME'] + (" " + row['DMNAME'] if row['DMNAME'] else "") + " " + row['DLNAME']
        st.write(f"**Name:** {name}")
        st.write(f"**Specialization:** {row['FIELD']}")
        st.write(f"**Date of Joining:** {row['DOJ']}")
        
        # Fetch schedule
        conn = get_connection()
        sched = conn.execute("SELECT * FROM dtime WHERE DID = ?", (row['DID'],)).fetchone()
        conn.close()
        
        st.subheader("Weekly Schedule")
        if sched:
            # Display as a single-row DataFrame with days as columns
            schedule_dict = {
                "Monday": sched['MON'] or "—",
                "Tuesday": sched['TUE'] or "—",
                "Wednesday": sched['WED'] or "—",
                "Thursday": sched['THU'] or "—",
                "Friday": sched['FRI'] or "—",
                "Saturday": sched['SAT'] or "—",
                "Sunday": sched['SUN'] or "—"
            }
            # Convert to list of one dict for DataFrame
            st.dataframe([schedule_dict], use_container_width=True)
        else:
            st.info("No schedule available for this doctor.")

class NurseOps:
    def view_all(self):
        st.subheader("All Nurses")
        conn = get_connection()
        rows = conn.execute("SELECT * FROM nurse ORDER BY NID").fetchall()
        conn.close()
        if rows:
            data = []
            for r in rows:
                data.append({
                    "NID": r['NID'],
                    "First": r['NFNAME'],
                    "Middle": r['NMNAME'] or "",
                    "Last": r['NLNAME'],
                    "Ward": r['WARD'],
                    "DOJ": r['DOJ']
                })
            st.dataframe(data, use_container_width=True)
        else:
            st.info("No nurses found.")

    def search_by_id(self):
        st.subheader("Search Nurse by ID")
        nid = st.text_input("Nurse ID").strip().upper()
        if st.button("Search"):
            conn = get_connection()
            row = conn.execute("SELECT * FROM nurse WHERE NID = ?", (nid,)).fetchone()
            conn.close()
            if row:
                self._display_single(row)
            else:
                st.error("Not found.")

    def search_by_name(self):
        st.subheader("Search Nurse by Name")
        fname = st.text_input("First Name").strip().upper()
        mname = st.text_input("Middle Name (optional)").strip().upper() or None
        lname = st.text_input("Last Name").strip().upper()
        if st.button("Search"):
            if not fname or not lname:
                st.error("First and last required.")
                return
            conn = get_connection()
            if mname:
                rows = conn.execute("SELECT * FROM nurse WHERE NFNAME=? AND NMNAME=? AND NLNAME=?", (fname, mname, lname)).fetchall()
            else:
                rows = conn.execute("SELECT * FROM nurse WHERE NFNAME=? AND NLNAME=?", (fname, lname)).fetchall()
            conn.close()
            if rows:
                data = [{"NID": r['NID'], "First": r['NFNAME'], "Middle": r['NMNAME'] or "", "Last": r['NLNAME'], "Ward": r['WARD'], "DOJ": r['DOJ']} for r in rows]
                st.dataframe(data, use_container_width=True)
                if len(rows)==1:
                    self._display_single(rows[0])
            else:
                st.info("No nurse found.")

    def by_ward(self):
        st.subheader("Nurses by Ward")
        ward = st.text_input("Ward (e.g., W01)").strip().upper()
        if st.button("Search"):
            if not ward or len(ward)!=3 or ward[0]!='W':
                st.error("Invalid ward.")
                return
            conn = get_connection()
            rows = conn.execute("SELECT * FROM nurse WHERE WARD = ?", (ward,)).fetchall()
            conn.close()
            if rows:
                data = [{"NID": r['NID'], "First": r['NFNAME'], "Middle": r['NMNAME'] or "", "Last": r['NLNAME'], "DOJ": r['DOJ']} for r in rows]
                st.dataframe(data, use_container_width=True)
            else:
                st.info("No nurses in this ward.")

    def _display_single(self, row):
        st.subheader("Nurse Details")
        st.write(f"**NID:** {row['NID']}")
        name = row['NFNAME'] + (" " + row['NMNAME'] if row['NMNAME'] else "") + " " + row['NLNAME']
        st.write(f"**Name:** {name}")
        st.write(f"**Ward:** {row['WARD']}")
        st.write(f"**DOJ:** {row['DOJ']}")

# --------------------- MAIN APP ---------------------
def main():
    init_db()

    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
        st.session_state.username = None

    st.set_page_config(page_title="HMS", layout="wide")
    st.title("🏥 Hospital Management System")

    if not st.session_state.logged_in:
        auth = UserAuth()
        menu = st.radio("Choose action", ["Login", "Register", "Forgot Password"], horizontal=True)
        if menu == "Login":
            auth.login()
        elif menu == "Register":
            auth.register()
        else:
            auth.forgot()
    else:
        st.sidebar.success(f"Logged in as {st.session_state.username}")
        if st.sidebar.button("Logout"):
            st.session_state.logged_in = False
            st.session_state.username = None
            st.rerun()

        choice = st.sidebar.selectbox("Module", ["Patient", "Doctor", "Nurse"])
        if choice == "Patient":
            p = PatientOps()
            action = st.selectbox("Action", ["View All", "Add", "Search by ID", "Search by Name", "Modify"])
            if action == "View All": p.view_all()
            elif action == "Add": p.add()
            elif action == "Search by ID": p.search_by_id()
            elif action == "Search by Name": p.search_by_name()
            else: p.modify()
        elif choice == "Doctor":
            d = DoctorOps()
            action = st.selectbox("Action", ["View All", "View Schedule", "Search by ID", "Search by Name"])
            if action == "View All": d.view_all()
            elif action == "View Schedule": d.view_schedule()
            elif action == "Search by ID": d.search_by_id()
            else: d.search_by_name()
        else:  # Nurse
            n = NurseOps()
            action = st.selectbox("Action", ["View All", "Search by ID", "Search by Name", "Search by Ward"])
            if action == "View All": n.view_all()
            elif action == "Search by ID": n.search_by_id()
            elif action == "Search by Name": n.search_by_name()
            else: n.by_ward()

if __name__ == "__main__":
    main()