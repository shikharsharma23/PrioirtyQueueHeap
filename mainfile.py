# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 09:21:01 2019

@author: NEX2BZR
"""

### the program simulates doctor appointment system
### It uses a linked list to store info about patients
### It uses a max heap to represent priority queue for patients basd on age
### A new patient record is stored in linked list ( Patient Record)
### current consultiations are present in a max heap
### Program first loads patients from inputPS5a.txt and then follows commands in inputPS5b.txt
### Output is stored the releveant out file
### Assumptions and clarifications
### 1) As in requirments we need to show queue after each operation, we make a copy of heap and pop it to display queue
### 2) Heap stores whole patient record. if we were to only store patient id, then to display name we would have to everytime 
### search linked list and it would have been unoptimized 
### 3) We check that if no patient in queue ( heap ) and a nextPatient (pop) called then we should flag error
### 4) We assume no upper limit for patient count and hence can oush multiple patients
### 5) The design makes assumptions on th instructions to optimize the solution wherevre possible
### 6) In linked list , each new registered patient is stored as the head , O(1))
### 7) In deque, we dont need patient id as it is by default dequeud from top of the heap

from max_heap import * # gets the max heap implementation for patient
from PatientRecord import * # the patient linked list storing patients
import copy

p5_a_file_name = 'inputPS5a.txt' # relevent files
p5_b_file_name = 'inputPS5b.txt'
p5_out_file_name = 'outputPS5.txt'


def create_ll(name, age): # creates the starting element of linked list
    patient_ll = PatientRecord(int(age), name,  1000)
    return patient_ll



def create_and__enque_patient_ll(p5_a_file_name): # this creates the linked list and push patients from the input file
    patient_ll = None
    f = open(p5_a_file_name) # open file
    while(1):
        line = f.readline().replace('\n','') # read line of patient info
        if len(line) == 0: # check if this is eof
            break
        else:
            line_split = line.replace('\n','').split(',')
            name = line_split[0] # parse patient info
            age = line_split[1].replace(' ','')
            if not patient_ll:
                patient_ll  = create_ll(name, int(age)) # if no patients, create one
            else:
                patient_ll = patient_ll.registerPatient(name, int(age)) # register a new patient
    return patient_ll
                
def print_queue(patient_queue): # prints the priority queue
    out_file.write('\n----------- Queue-----------------')
    out_file.write('\nNumber of Patients added : ' + str(len(patient_queue._heap)))
    while(len(patient_queue._heap) > 0): # until empty
        deleted_patient = patient_queue._dequeuePatient() # pop an elemnet
        out_file.write('\n'+str(deleted_patient)) # write to file
    out_file.write('\n----------------------------------------')
    
def execute_commands(max_heap, patient_ll): # parses the second input file for commannds to process
    f = open(p5_b_file_name)
    while(1):
        line = f.readline().replace('\n','') # read command
        if line=='':
            break
        else:
            out_file.write('\nCommand recived is : ')
            out_file.write(line)
            line_split = line.split(':')
            if len(line_split)==1: # its a nextPatient Command:
                max_heap.nextPatient() # call to nextPatient

            else: # its a new patient command
                age = line_split[-1].split(',')[-1]
                name = line_split[-1].split(',')[-2] # get new patient info

                patient_ll = patient_ll.registerPatient(name,int(age)) # put in linked list
                max_heap.enquePatient(patient_ll) # add patient to heap
                out_file.write('\nNew Patient Added ')
                out_file.write('\n' + str(patient_ll))
                out_file.write('\nRefreshed Queue is')
                print_queue(copy.deepcopy(max_heap)) # print refreshed queue
    f.close()
                
                
if __name__ == "__main__": 
    out_file.write('\n---------------------------------- Program Starts ----------------------------------')
    patient_ll = create_and__enque_patient_ll(p5_a_file_name) # create linked list from intial patient list
    out_file.write('\nLoading Patients From File')
    patient_ll_head = copy.deepcopy(patient_ll) # keep track of head
    max_heap = MaxHeap() # maka a max heap
    while(patient_ll):
        max_heap.enquePatient(patient_ll) # add each element of linked list to max heap
        patient_ll = patient_ll.right
    ## above completes part 1, making linked list, putting initial patients in heap and displaying queue
    patient_ll= patient_ll_head # restore the first elment of linked list 
    print_queue(copy.deepcopy(max_heap)) # print the queue
    execute_commands(max_heap,patient_ll) # performs commands provided by user in inputPS5b.txt
    out_file.close()
    
