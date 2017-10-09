# whoa that was sick cool! :%s!^\([^|]*|\)\{2\}\zs.*!!
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#System Administrator Role
System_Administrator(date, uname):
    # requests
    Date = date
    username = uname
    def __str__(self):
        return str(self.username)


#Doctor Role
class Doctor(models.Model):
    # requests
    Practice_Name = practice_name
    Practice_Address = address p_addr
    Recovery_Phrase = r_phase
    #username = uname
    username = uname
    #created_by =
    created_at = create_date
    def __str__(self):
        return self.Practice_Name

#Nurse Role
class Nurse(models.Model):
    # requests
    Practice_Name = practice_name
    Practice_Address = address p_addr
    Associated_Doctors = doc_colleagues
    username = uname
    created_at = create_date
    def __str__(self):
        return self.Practice_Name

#Medical Administrator Role
class Medical_Administrator(models.Model):
    # requests
    Practice_Name = practice_name
    Practice_Address = address p_addr
    Associated_Doctors = doc_colleagues
    Associated_Doctors = nurse_colleagues
    username = uname
    created_at = create_date
    def __str__(self):
        return self.Practice_Name

#Insurance Administrator Role
class Insurance_Administrator(models.Model):
    # requests
    Company_Name = ins_company
    Company_Address = address ins_address
    username = uname
    created_at = create_date
    def __str__(self):
        return self.Company_Name

#Patient Role
class Patient(models.Model):
    # requests
    SSN = ssn
    Address = address
    DOB = dob
    username = uname
    created_at = create_date
    def __str__(self):
        return self.SSN

#Record
class Record(models.Model):
    # requests
    Record_ID =
    lst =
    options =
    Record_Type =
    Record_Date = date
    Owner =
    Patient =
    Edit_Permissions =
    View_Permissions =
    created_at = create_date
    def __str__(self):
        return str(self.Record_ID)

#Doctor Exam Record
class Doctor_Exam_Record(models.Model):
    # requests
    Date = date
    Doctor =
    Notes =
    Record =
    created_at = create_date
    def __str__(self):
        return str(self.id)

#Diagnosis Record
class Diagnosis_Record(models.Model):
    # requests
    Date = date
    Doctor =
    Diagnosis =
    Record =
    created_at = create_date
    def __str__(self):
        return str(self.id)

#Test Results Record
class Test_Results_Record(models.Model):
    # requests
    Date = date
    Doctor =
    Lab =
    Notes =
    Record =
    created_at = create_date
    def __str__(self):
        return str(self.id)


#Insurance Claim Record
class Insurance_Claim_Record(models.Model):
    # requests
    Date = date
    Medical_Administrator =
    Amount =
    Status_Options =
    Status =
    Record =
    created_at = create_date
    def __str__(self):
        return str(self.id)


#Patient_Doctor_Correspondence_Record
class Patient_Doctor_Correspondence_Record(models.Model):
    # requests
    Doctor =
    Notes =
    Record =
    created_at = create_date
    def __str__(self):
        return str(self.id)

#Raw Record
class Raw_Record(models.Model):
    # requests
    Description =
    File =
    Record =
    created_at = create_date
    def __str__(self):
        return str(self.id)

#Note
class Note(models.Model):
    # requests
    Date = date
    Text =
    Patient_Doctor_Correspondence =
    created_at = create_date
    def __str__(self):
        return str(self.id)
