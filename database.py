import sqlite3

class Connect:
    def __init__(self):
        self.conn = sqlite3.connect(r"G:\My Drive\sqlite_database\Asclepius_I.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        print("Connected!")
        
        
    """-----------------------------------------------------------------ROOM-------------------------------------------------------------"""
    
    
    """booking room details"""
    def insert_room(self, r_id, doc, r_type, time, dept, p_id):
        self.cursor.execute("SELECT 1 FROM inpatient WHERE P_id = ?",(p_id,))
        if self.cursor.fetchone():
            self.cursor.execute("INSERT INTO room (Room_no,Doc_in,Room_type,Duration,Department,Patient_ID) VALUES (?, ?, ?, ?, ?, ?)", (r_id, doc, r_type, time, dept,p_id))
            self.conn.commit()
            print(f"Room assigned to {p_id} successfully.")
            return True
        else:
            print(f"Cannot insert: {p_id} is not in inpatient records.")
            return False
        
    """to get no of days stayed for inpatient billing"""
    def get_inpatient_days(self,p_id):
        self.cursor.execute("select Duration from room where Patient_ID = ?",(p_id,))
        result = self.cursor.fetchone()
        if result:
            return result[0]
        else:
            return False
        
    """to get room type"""
    def get_room_type(self,p_id):
        self.cursor.execute("select Room_type from room where Patient_ID = ?",(p_id,))
        result = self.cursor.fetchone()
        if result:
            return result[0]
        else:
            return False
        
    """-----------------------------------------------------------------ADMIN-------------------------------------------------------------"""
    
    
    """checking login info for admin"""
    def check_info(self,user):
        self.cursor.execute("select * from admin where Auser = ?;",(user,))
        return self.cursor.fetchone()
    
    """retrieve all values for admin"""
    def retrieve_admin(self,user):
        self.cursor.execute("select * from admin where Auser = ?",(user,))
        return self.cursor.fetchone()
    
    """login for admin"""
    def get_login_admin(self,user):
        self.cursor.execute("select Apass from Admin where Auser = ?;",(user,))
        result = self.cursor.fetchone()
        if result:
            return result[0]
    
    """to get id for updation of details"""
    def get_id_admin(self, email):
        self.cursor.execute("select Acode from admin where Email  = ?;",(email,))
        result = self.cursor.fetchone()
        if result:
            return result[0]
    
    """to update admin details"""
    def update_admin(self,e_id,name,dob,phone,gender,email,user,password):
        self.cursor.execute("update admin set Name = ?,DOB = ?,Phone = ?,Gender = ?, Email = ?, Auser = ?, Apass = ? where Acode =?;",(name,dob,phone,gender,email,user,password,e_id,))
        self.conn.commit()
    
    """to register admin details"""
    def insert_admin(self,e_id,name,salary,dob,phone,gender,email,user,password):
        self.cursor.execute("insert into admin values(?,?,?,?,?,?,?,?,?);",(e_id,name,salary,dob,phone,gender,email,user,password))
        self.conn.commit()
        print("Inserted successfully:", user)
        
    """to temporarily store admin user"""    
    def insert_admin_user(self,user):
        self.cursor.execute("insert into tempdata(Adminuser) values(?);",(user,))
        self.conn.commit()
        
    """-----------------------------------------------------------------------DOCTOR--------------------------------------------------------------"""
        
    """to register doctor details"""
    def insert_doctor(self,code,name,salary,dob,phone,email,gender,user,password):
        self.cursor.execute("insert into Doctor(Dcode,Name,Salary,DOB,Phone,Email,Gender,Duser,Dpass) values(?,?,?,?,?,?,?,?,?);",(code,name,salary,dob,phone,email,gender,user,password,))
        self.conn.commit()
        
    """to temporarily store doctor user"""   
    def insert_doctor_user(self,user):
        self.cursor.execute("insert into tempdata(Doctoruser) values(?);",(user,))
        self.conn.commit()
        
    """to insert field of doctor"""
    def insert_field_doctor(self,field,code):
        self.cursor.execute("update Doctor set Field = ? where Dcode = ?;",(field,code,))
        self.conn.commit()
        
    """to update doctor details"""
    def update_doctor(self,code,name,dob,phone,email,gender,user,password):
        self.cursor.execute("update Doctor set Name = ?, DOB = ?, Phone = ?,Email = ?,Gender = ?, Duser = ?, Dpass = ? where Dcode = ?;",(name,dob,phone,email,gender,user,password,code,))
        self.conn.commit()
    
    """to get doctor details"""
    def retrieve_doctor(self,user):
        self.cursor.execute("select Dcode,Name,Field,Salary,DOB,Phone,Email,Gender,Duser,Dpass from Doctor where Duser = ?",(user,))
        return self.cursor.fetchone()
    
    """to get doctor id"""
    def get_id_doctor(self,email):
        self.cursor.execute("select Dcode from Doctor where Email = ?;",(email,))
        result = self.cursor.fetchone()
        if result:
            return result[0]
        
    """to get all doctors"""
    def get_doctors(self):
        self.cursor.execute("select Name, Field from Doctor")
        return self.cursor.fetchall()
    
    """login for doctor"""
    def get_login_doc(self,user):
        self.cursor.execute("select Dpass from Doctor where Duser = ?;",(user,))
        result = self.cursor.fetchone()
        if result:
            return result[0]
        
    """----------------------------------------------------------------------NURSE------------------------------------------------------------------"""
        
    """to register nurse details"""
    def insert_nurse(self,code,name,salary,dob,phone,user,password,email,gender):
        self.cursor.execute("insert into Nurse values(?,?,?,?,?,?,?,?,?);",(code,name,salary,dob,phone,user,password,email,gender))
        self.conn.commit()
        
    """to update nurse details"""
    def update_nurse(self,code,name,dob,phone,user,password,email,gender):
        self.cursor.execute("update Nurse set Name = ?, DOB = ?, Phone = ?, Nuser = ?, Npass = ?, Email = ?,Gender = ? where Ncode = ?;",(name,dob,phone,user,password,email,gender,code,))
        self.conn.commit()
        
    """to get nurse details"""
    def retrieve_nurse(self,user):
        self.cursor.execute("select * from Nurse where Nuser = ?;",(user,))
        return self.cursor.fetchone()
        
    """to get nurse id"""
    def get_id_nurse(self,email):
        self.cursor.execute("select Ncode from Nurse where Email = ?;",(email,))
        result = self.cursor.fetchone()
        if result:
            return result[0]
        
    """login for nurse""" 
    def get_login_nurse(self,user):
        self.cursor.execute("select Npass from Nurse where Nuser = ?;",(user,))
        result = self.cursor.fetchone()
        if result:
            return result[0]
        
    """------------------------------------------------------------------INPATIENT---------------------------------------------------------------------"""
    
    """to get inpatient name"""
    def get_inpatient_name(self,p_id):
        self.cursor.execute("select P_name from inpatient where P_id = ?",(p_id,))
        return self.cursor.fetchone()
    
    """to get all inpatient ids"""
    def inpatient_ids(self):
        self.cursor.execute("select P_id from inpatient")
        return self.cursor.fetchall()
    
    """get all details for inpatient billing"""
    def get_inpatient(self,p_id):
        self.cursor.execute("select P_id,P_name,Date_of_admission,Condition from inpatient where P_id = ?",(p_id,))
        return self.cursor.fetchone()
    
    """inpatient details"""
    def insert_inpatient(self,ticket_no,name,gender,dob,phone,date,doc,email,condition):
        self.cursor.execute("insert into inpatient values(?,?,?,?,?,?,?,?,?);",(ticket_no,name,gender,dob,phone,date,doc,email,condition,))
        self.conn.commit()
        
    """to update inpatient details"""    
    def update_inpatient(self,name,gender,dob,phone,date,doc,email,condition,ticket_no):
        self.cursor.execute("update inpatient set P_name = ?, Gender = ?, DOB = ?,Phone = ?,Date_of_admission = ?,Doc_in = ?,Email = ?,Condition = ? where P_id = ?;",(name,gender,dob,phone,date,doc,email,condition,ticket_no,))
        self.conn.commit()
    
    """to get intpatient id for updation"""
    def get_inpatient_id(self,email):
        self.cursor.execute("select P_id from inpatient where Email = ?;",(email,))
        result = self.cursor.fetchone()
        if result:
            return result[0]
        
    """--------------------------------------------------------------------OUTPATIENT-----------------------------------------------------------------"""
        
    """outpatient details"""
    def insert_outpatient(self,name,gender,dob,phone,date,email,ticket_no):
        self.cursor.execute("insert into outpatient (P_name,Gender,DOB,Phone,Date_of_admission,Email,Tno) values(?,?,?,?,?,?,?);",(name,gender,dob,phone,date,email,ticket_no,))
        self.conn.commit()
    
    """to get outpatient id for updation"""
    def get_outpatient_id(self,email):
        self.cursor.execute("select Tno from Outpatient where Email = ?;",(email,))
        result = self.cursor.fetchone()
        if result:
            return result[0]
    """to get outpatient name"""
    def get_outpatient_name(self,p_id):
        self.cursor.execute("select P_name from outpatient where Tno = ?",(p_id,))
        return self.cursor.fetchone()
        
    """to get all existing outpatient ids"""
    def get_outpatient_ids(self):
        self.cursor.execute("SELECT Tno FROM outpatient")
        result = self.cursor.fetchall()
        # Flatten the list of tuples into a list of integers
        return [row[0] for row in result] if result else []
        
    """to update outpatient details in patient registration(BY ADMIN)"""    
    def update_outpatient(self,name,gender,dob,phone,date,doc,email,condition,ticket_no):
        self.cursor.execute("update outpatient set P_name = ?, Gender = ?, DOB = ?,Phone = ?,Date_of_admission = ?,Email = ? where Tno = ?;",(name,gender,dob,phone,date,email,ticket_no,))
        self.conn.commit()
          
    """to update outpatient details in outpatient booking(BY PATIENT)"""    
    def update_outpatient_self(self,doc,condition,dept,tno):
        self.cursor.execute("update outpatient set Doc_in = ?,Condition = ?, Department = ? where Tno = ?;",(doc,condition,dept,tno))
        self.conn.commit()
    """to get outpatient details for outbilling"""
    def get_outpatient(self,p_id):
        self.cursor.execute("select P_name,Condition,Tno from outpatient where Tno = ?",(p_id,))
        return self.cursor.fetchone()
        