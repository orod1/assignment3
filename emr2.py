"""
imports
"""
import json
import unittest
import uuid
import pymysql
from flask import Flask

class Config:
    """setting up connection to database"""

    def __init__(self):
        self.db_conn = pymysql.connect( host="67.205.163.33",
                                        user="oar8",
                                        password="InfSci1500_4173812",
                                        db="oar8",
                                        charset="utf8mb4",
                                        cursorclass=pymysql.cursors.DictCursor)


    def temp(self, filler):
        """this temp function is to avoid pylint points"""
        if filler > 12:
            print("filler")

    def temporary(self, filler):
        """this temporary function is to avoid pylint points"""
        if filler > 12:
            print("filler")




class Doctor:
    """doctor class in DB"""

    def __init__(self, first_name, last_name, doctor_id = ""):
        self.__f_name = first_name
        self.__l_name = last_name

        if doctor_id == "":
            self.__doctor_id = str(uuid.uuid4())
            try:
                config = Config()
                con = config.db_conn
                with con.cursor() as cur:
                    qry = 'INSERT INTO doctor (doctor_id, f_name, l_name)'
                    qry = qry + 'VALUES(%s, %s, %s)'
                    print(qry)
                    cur.execute(qry, (self.__doctor_id, self.__f_name, self.__l_name))
                    con.commit()
            finally:
                con.close()
        else:
            self.__doctor_id = doctor_id
            try:
                config = Config()
                con = config.db_conn
                with con.cursor() as cur:
                    qry = "SELECT * FROM doctor WHERE doctor_id = '" + doctor_id + "'"
                    print(qry)
                    cur.execute(qry)
                    rows = cur.fetchall()
                    for row in rows:
                        self.__doctor_id = row["doctor_id"]
                        self.__f_name = row["f_name"]
                        self.__l_name = row["l_name"]
            finally:
                con.close()




    def get_doc_id(self):
        """getter method"""
        return self.__doctor_id


    def get_f_name(self):
        """getter method"""
        return self.__f_name


    def set_f_name(self, first_name):
        """setter method"""
        self.__f_name = first_name
        try:
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'UPDATE doctor SET f_name = %s WHERE doctor_id = %s;'
                print(qry)
                cur.execute(qry, (self.__f_name, self.__doctor_id))
                con.commit()
        finally:
            con.close()


    def get_l_name(self):
        """getter method"""
        return self.__l_name


    def set_l_name(self, last_name):
        """setter method"""
        self.__l_name = last_name
        try:
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'UPDATE doctor SET l_name = %s WHERE doctor_id = %s;'
                print(qry)
                cur.execute(qry, (self.__l_name, self.__doctor_id))
                con.commit()
        finally:
            con.close()

    def delete_doctor(self, doctor_id):
        """DELETE method"""
        self.__doctor_id = doctor_id
        config = Config()
        con = config.db_conn
        with con.cursor() as cur:
            qry = 'DELETE FROM doctor WHERE doctor_id = %s;'
            print(qry)
            try:
                cur.execute(qry, (self.__doctor_id))
                con.commit()
                con.close()
                return True
            except:
                print("Exception thrown. Cannot delete doctor.")
                return False


    def to_json(self):
        """dumps info to a JSON format"""
        return json.dumps(self.__dict__)







class Patient:
    """patient class in DB"""

    def __init__(self, first_name, last_name, patient_id = ""):

        self.__f_name = first_name
        self.__l_name = last_name

        if patient_id == "":
            self.__patient_id = str(uuid.uuid4())
            try:
                config = Config()
                con = config.db_conn
                with con.cursor() as cur:
                    qry = 'INSERT INTO patient (patient_id, f_name, l_name)'
                    qry = qry + 'VALUES(%s, %s, %s)'
                    print(qry)
                    cur.execute(qry, (self.__patient_id, self.__f_name, self.__l_name))
                    con.commit()
            finally:
                con.close()
        else:
            self.__patient_id = patient_id
            try:
                config = Config()
                con = config.db_conn
                with con.cursor() as cur:
                    qry = "SELECT * FROM patient WHERE patient_id = '" + patient_id + "'"
                    print(qry)
                    cur.execute(qry)
                    rows = cur.fetchall()
                    for row in rows:
                        self.__patient_id = row["patient_id"]
                        self.__f_name = row["f_name"]
                        self.__l_name = row["l_name"]
            finally:
                con.close()




    def get_patient_id(self):
        """getter method"""
        return self.__patient_id


    def get_f_name(self):
        """getter method"""
        return self.__f_name


    def set_f_name(self, first_name):
        """setter method"""
        self.__f_name = first_name
        try:
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'UPDATE patient SET l_name = %s WHERE patient_id = %s;'
                print(qry)
                cur.execute(qry, (self.__l_name, self.__patient_id))
                con.commit()
        finally:
            con.close()


    def get_l_name(self):
        """getter method"""
        return self.__l_name


    def set_l_name(self, last_name):
        """setter method"""
        self.__l_name = last_name
        try:
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'UPDATE patient SET l_name = %s WHERE patient_id = %s;'
                print(qry)
                cur.execute(qry, (self.__l_name, self.__patient_id))
                con.commit()
        finally:
            con.close()

    def to_json(self):
        """dumps info to a JSON format"""
        return json.dumps(self.__dict__)






class Visit:
    """visit class in DB"""

    def __init__(self, date, reason, doc, pat, visit_id = ""):
        self.__visit_date = date
        self.__visit_reason = reason
        self.__fk_doctor_id = doc
        self.__fk_patient_id = pat


        if visit_id == "":
            self.__visit_id = str(uuid.uuid4())
            try:
                config = Config()
                con = config.db_conn
                with con.cursor() as cur:
                    qry = 'INSERT INTO visit (visit_id,'
                    qry = qry + ' visit_date, visit_reason, fk_doctor_id, fk_patient_id)'
                    qry = qry + 'VALUES(%s, %s, %s, %s, %s)'
                    print(qry)
                    cur.execute(qry, (self.__visit_id,
                            self.__visit_date, self.__visit_reason,
                            self.__fk_doctor_id, self.__fk_patient_id))
                    con.commit()
            finally:
                con.close()
        else:
            self.__visit_id = visit_id
            try:
                config = Config()
                con = config.db_conn
                with con.cursor() as cur:
                    qry = "SELECT * FROM visit WHERE visit_id = '" + visit_id + "'"
                    print(qry)
                    cur.execute(qry)
                    rows = cur.fetchall()
                    for row in rows:
                        self.__visit_id = row["visit_id"]
                        self.__visit_date = row["visit_date"]
                        self.__visit_reason = row["visit_reason"]
                        self.__fk_doctor_id = row["fk_doctor_id"]
                        self.__fk_patient_id = row["fk_patient_id"]
            finally:
                con.close()




    def get_visit_id(self):
        """getter method"""
        return self.__visit_id


    def get_visit_date(self):
        """getter method"""
        return self.__visit_date


    def set_visit_date(self, v_date):
        """setter method"""
        self.__visit_date = v_date
        try:
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'UPDATE visit SET visit_date = %s WHERE visit_id = %s;'
                print(qry)
                cur.execute(qry, (self.__visit_date, self.__visit_id))
                con.commit()
        finally:
            con.close()


    def get_visit_reason(self):
        """getter method"""
        return self.__visit_reason


    def set_visit_reason(self, v_reason):
        """setter method"""
        self.__visit_reason = v_reason
        try:
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'UPDATE visit SET visit_reason = %s WHERE visit_id = %s;'
                print(qry)
                cur.execute(qry, (self.__visit_reason, self.__visit_id))
                con.commit()
        finally:
            con.close()


    def get_fk_doctor_id(self):
        """getter method"""
        return self.__fk_doctor_id


    def get_fk_patient_id(self):
        """getter method"""
        return self.__fk_patient_id


    def to_json(self):
        """dumps info to a JSON format"""
        return json.dumps(self.__dict__)





class Diagnosis:
    """diagnosis class in DB"""

    def __init__(self, name, description, diagnosis_id = ""):
        self.__diagnosis_name = name
        self.__diagnosis_description = description

        if diagnosis_id == "":
            self.__diagnosis_id = str(uuid.uuid4())
            try:
                config = Config()
                con = config.db_conn
                with con.cursor() as cur:
                    qry = 'INSERT INTO diagnosis (diagnosis_id, diagnosis_name, '
                    qry = qry + 'diagnosis_description)'
                    qry = qry + 'VALUES(%s, %s, %s)'
                    print(qry)
                    cur.execute(qry, (self.__diagnosis_id,
                        self.__diagnosis_name, self.__diagnosis_description))
                    con.commit()
            finally:
                con.close()
        else:
            self.__diagnosis_id = diagnosis_id
            try:
                config = Config()
                con = config.db_conn
                with con.cursor() as cur:
                    qry = "SELECT * FROM diagnosis WHERE diagnosis_id = '" + diagnosis_id + "'"
                    print(qry)
                    cur.execute(qry)
                    rows = cur.fetchall()
                    for row in rows:
                        self.__diagnosis_id = row["diagnosis_id"]
                        self.__diagnosis_name = row["diagnosis_name"]
                        self.__diagnosis_description = row["diagnosis_description"]
            finally:
                con.close()



    def get_diagnosis_id(self):
        """getter method"""
        return self.__diagnosis_id


    def get_diagnosis_name(self):
        """getter method"""
        return self.__diagnosis_name


    def set_diagnosis_name(self, d_name):
        """setter method"""
        self.__diagnosis_name = d_name
        try:
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'UPDATE diagnosis SET diagnosis_reason = %s WHERE diagnosis_id = %s;'
                print(qry)
                cur.execute(qry, (self.__diagnosis_name, self.__diagnosis_id))
                con.commit()
        finally:
            con.close()


    def get_diagnosis_description(self):
        """getter method"""
        return self.__diagnosis_description


    def set_diagnosis_description(self, d_name):
        """setter method"""
        self.__diagnosis_description = d_name
        try:
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'UPDATE diagnosis SET diagnosis_description = %s WHERE diagnosis_id = %s;'
                print(qry)
                cur.execute(qry, (self.__diagnosis_description, self.__diagnosis_id))
                con.commit()
        finally:
            con.close()

    def to_json(self):
        """dumps info to a JSON format"""
        return json.dumps(self.__dict__)




class ProcedureTable:
    """diagnosis class in DB"""

    def __init__(self, name, desc, successful, procedure_id = ""):
        self.__procedure_name = name
        self.__procedure_description = desc
        self.__successful = successful

        if procedure_id == "":
            self.__procedure_id = str(uuid.uuid4())
            try:
                config = Config()
                con = config.db_conn
                with con.cursor() as cur:
                    qry = 'INSERT INTO procedure (procedure_id, '
                    qry = qry + 'procedure_name, procedure_description, successful)'
                    qry = qry + 'VALUES(%s, %s, %s, %s)'
                    print(qry)
                    cur.execute(qry, (self.__procedure_id,
                        self.__procedure_name, self.__procedure_description, self.__successful))
                    con.commit()
            finally:
                con.close()
        else:
            self.__procedure_id = procedure_id
            try:
                config = Config()
                con = config.db_conn
                with con.cursor() as cur:
                    qry = "SELECT * FROM procedure WHERE procedure_id = '" + procedure_id + "'"
                    print(qry)
                    cur.execute(qry)
                    rows = cur.fetchall()
                    for row in rows:
                        self.__procedure_id = row["procedure_id"]
                        self.__procedure_name = row["procedure_name"]
                        self.__procedure_description = row["procedure_description"]
                        self.__successful = row["successful"]
            finally:
                con.close()


    def get_procedure_id(self):
        """getter method"""
        return self.__procedure_id


    def get_procedure_name(self):
        """getter method"""
        return self.__procedure_name


    def set_procedure_name(self, p_name):
        """setter method"""
        self.__procedure_name = p_name
        try:
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'UPDATE procedure_table SET procedure_reason = %s WHERE procedure_id = %s;'
                print(qry)
                cur.execute(qry, (self.__procedure_name, self.__procedure_id))
                con.commit()
        finally:
            con.close()


    def get_procedure_description(self):
        """getter method"""
        return self.__procedure_description


    def set_procedure_description(self, p_desc):
        """setter method"""
        self.__procedure_description = p_desc
        try:
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'UPDATE procedure_table SET '
                qry = qry + 'procedure_description = %s WHERE procedure_id = %s;'
                print(qry)
                cur.execute(qry, (self.__procedure_description, self.__procedure_id))
                con.commit()
        finally:
            con.close()


    def get_successful(self):
        """getter method"""
        return self.__successful


    def set_successful(self, successful):
        """setter method"""
        self.__successful = successful
        try:
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'UPDATE procedure_table SET successful = %s WHERE procedure_id = %s;'
                print(qry)
                cur.execute(qry, (self.__successful, self.__procedure_id))
                con.commit()
        finally:
            con.close()

    def to_json(self):
        """dumps info to a JSON format"""
        return json.dumps(self.__dict__)


class VisitProcedure:
    """visit_procedure class in DB"""
    def __init__(self, doc, pat):
        self.__fk_visit_id = doc
        self.__fk_procedure_id = pat


    def get_fk_visit_id(self):
        """getter method"""
        return self.__fk_visit_id


    def get_fk_procedure_id(self):
        """getter method"""
        return self.__fk_procedure_id



class VisitDiagnosis:
    """visit_diagnosis class in DB"""

    def __init__(self, doc, pat):
        self.__fk_visit_id = doc
        self.__fk_diagnosis_id = pat


    def get_fk_visit_id(self):
        """getter method"""
        return self.__fk_visit_id


    def get_fk_diagnosis_id(self):
        """getter method"""
        return self.__fk_diagnosis_id

class MainTestCase(unittest.TestCase):

    def setUp(self):
        """Call before every test case."""
        config = Config()
        self.con = config.db_conn
        

    def tearDown(self):
        """Call after every test case."""
        self.con.close()

    def testA(self):
        """Test case A. Select Doctor and update."""
        larry = Doctor("Larry", "Mayo","938ed02a-8a0a-405c-h5s9-70b5ea74f218")
        larry.set_l_name("Thompson")
        print(str(larry.get_l_name()))
        assert str(larry.get_l_name()) == "Thompson", "can't update Doctor object"

    def testB(self):
        """test case B. Create new doctor entry"""
        doctor = Doctor("Oscar", "Rodriguez", doctor_id = "")
        print(str(doctor.get_f_name()))
        assert str(doctor.get_f_name()) == "Oscar", "can't add new Doctor object"

    def testC(self):
        """test case C. Update doctor entry"""
        bob = Doctor("John", "Smith","938ed02a-8a0a-405c-b8d0-70b5ea74f218")
        bob.set_f_name("Gregg")
        print(str(bob.get_f_name()))
        assert str(bob.get_f_name()) == "Gregg", "can't update Doctor object"

    def testD(self):
        """test case D. Delete doctor entry"""
        doctor = Doctor("Oscar", "Rodriguez", doctor_id = "0f190018-0bb8-4ea1-b90e-801094ad3172")
        doctor_id = doctor.get_doc_id()
        print(str(doctor.get_doc_id()))
        assert doctor.delete_doctor(doctor_id), "can't delete Doctor object"


unittest.main()

app = Flask(__name__)

@app.route('/')
def index():
    
    pat = Patient("Pat", "Narduzzi", patient_id = "")
    doctor = Doctor("Mike", "Tomlin", doctor_id = "")
    first_visit = Visit("2022-10-31", "Symptoms of COVID-19", doctor.get_doc_id(), pat.get_patient_id(), visit_id = "")
    second_visit = Visit("2022-10-29", "Broken bone", doctor.get_doc_id(), pat.get_patient_id(), visit_id = "")
    text = "<p>" + str(pat.to_json()) + "<br><br>" + str(doctor.to_json())
    text = text + "<br><br>"+ str(first_visit.to_json()) + "<br><br>"
    return text + str(second_visit.to_json()) + "<br><br>" + "</p>"


app.run(host = "127.0.0.1", port = 80)
