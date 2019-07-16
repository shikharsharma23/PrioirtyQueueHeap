# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 09:24:11 2019

@author: NEX2BZR
"""

class PatientRecord:
    def __init__(self, age, name, Pid):
        self.PatId = str(Pid) + str(age)
        self.name = name
        self.age = age
        self.left = None
        self.right = None
        
    def __gt__(self, other): # comparision based on age
        if self.age > other.age:
            return True
        else:
            return False
        
    def registerPatient(self, name, age): # register a new patient to linked list
        new_patient = PatientRecord(age, name, str(int(self.PatId[0:4] )+1)) # create auto incremnet id
        new_patient.right = self # latest patient is new head of theh linked list
        return new_patient
    
        
    def __str__(self):
        return 'Name : ' + self.name + ' Age :' + str(self.age) + ' Patient Id :' +  self.PatId
        
        