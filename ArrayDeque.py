# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 18:34:01 2023

@author: Juan Brasdefer, Fabian Pawelczyk
"""

class Empty(Exception): 
    pass

class ArrayDequeMaxlen:

    initial_capacity = 20

    #initialize our lovely deque
    def __init__(self, initial_capacity):
        #with typical initial capacity size
        self._data = [None] * ArrayDequeMaxlen.initial_capacity
        #and our front index and size measures
        self._front = 0
        self._size = 0


    #add an element to the beginning of our deque
    def add_first(self, e):
        #easy resize if we are already at capacity
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        #reassign position of existing front item
        self._front = (self._front - 1) % len(self._data)
        self._data[self._front] = e
        self._size += 1

    #add an element to the end of the deque
    def add_last(self, e):
        #easy resize if we are already at capacity
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        pos = (self._front + self._size) % len(self._data)
        self._data[pos] = e
        self._size += 1


    #delete the first entry of the deque
    def delete_first(self):
        #check first to see if the deque is empty
        if self.is_empty():
            raise Empty("Deque is empty my friend!!")
        result = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        #resize to keep us healthy and fit and slim 
        self._size -= 1
        #but also resize the other way if we get too fit and slim
        if self._size < len(self._data) // 4:
            self._resize(len(self._data) // 2)
        return result


    #return the first element of the deck
    def first(self):
        if self.is_empty():
            raise Empty("Deque is empty my friend!!")
        return self._data[self._front]

    #return the last element of the deck
    def last(self):
        if self.is_empty():
            raise Empty("Deque is empty my friend!!")
        return self._data[self._front + self._size - 1]
    
    #check length of deque by calling the attribute _size
    def __len__(self):
        return self._size

    #quick true or false to check whether deque is empty
    def is_empty(self):
        return self._size == 0

    #resizes array by creating a new array when array is empty
    def _resize(self, cap):
        #copying the elements from the old array to the new array in the correct order,
        old = self._data
        self._data = [None] * cap
        #browse just iterates over the array
        browse = self._front
        for k in range(self._size):
            self._data[k] = old[browse]
            browse = (browse + 1) % len(old)
        #and updating the front and rear indices.
        self._front = 0
        
        
   