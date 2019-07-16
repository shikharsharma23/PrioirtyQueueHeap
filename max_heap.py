# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 12:38:22 2019

@author: NEX2BZR
"""

p5_out_file_name = 'outputPS5.txt' # file we will be writing results to
out_file = open(p5_out_file_name, 'w')
 
class MaxHeap(): # represents a max heap for patient problem
    
    def __init__(self): # intially no patients
        self._heap = []
        
    def enquePatient(self, value): # adds a patient to queue
        self._heap.append(value)
        heapify_after_insert(self._heap, len(self._heap) - 1)
        
    def nextPatient(self): # shows the patient next in line and then deletes it
        try:
            next_patient = self._heap[0]
            out_file.write('\nNext patient is ')
            out_file.write(str(next_patient))
            self._dequeuePatient()
        except IndexError:
            print('No patients in queue')
        
    def  _dequeuePatient(self): # deletes a patient from heap
        self._heap[-1], self._heap[0] = self._heap[0], self._heap[-1]  # swap elements
        deleted_element = self._heap.pop() # delete head
        heapify_after_deletion(self._heap, 0 ) # start heapifying from root
        return deleted_element
        
def heapify_after_insert(current_heap, index_to_heapify): # heapifies bottom to top
    parent_of_latest_child_index = (index_to_heapify - 1) // 2 # get parent
    if parent_of_latest_child_index < 0 :
        return # reached the root
    else:
        if current_heap[index_to_heapify] > current_heap[parent_of_latest_child_index]: # if parent is smaller
            temp = current_heap[index_to_heapify] # swap
            current_heap[index_to_heapify] = current_heap[parent_of_latest_child_index]
            current_heap[parent_of_latest_child_index] = temp
            heapify_after_insert(current_heap, parent_of_latest_child_index)  # recursively go down
            
def heapify_after_deletion(current_heap, index_to_heapify): # heapifies top to bottom
    first_child = 2 * index_to_heapify + 1 # get child
    second_child = 2 * index_to_heapify + 2
    if first_child >= len(current_heap):
        return
    elif second_child >= len(current_heap) : # only one child case
        if current_heap[first_child] > current_heap[index_to_heapify]:
            current_heap[first_child], current_heap[index_to_heapify] = current_heap[index_to_heapify], current_heap[first_child]
            heapify_after_deletion(current_heap, first_child)
    else: # both child
        if current_heap[first_child] > current_heap[second_child] and current_heap[first_child] > current_heap[index_to_heapify]:
            current_heap[first_child], current_heap[index_to_heapify] = current_heap[index_to_heapify], current_heap[first_child]
            heapify_after_deletion(current_heap, first_child)
        else:
            if current_heap[second_child] > current_heap[index_to_heapify]:
                current_heap[second_child], current_heap[index_to_heapify] = current_heap[index_to_heapify], current_heap[second_child]
                heapify_after_deletion(current_heap, second_child)

            



    
    
        