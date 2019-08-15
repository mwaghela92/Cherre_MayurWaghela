#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 14:14:31 2019

@author: mayur
"""

import unittest
from Cherre01 import total_count
from Cherre01 import make_connection


## other edge cases: not sorted
## not checking names for repetition


my_list_1 = [
        ('a',28),
        ('a',28),
        ('a',28),
        ('a',28),
        ('a',28),
        ('a',28),
        ('a',28)
        ]

my_list_2 = [
        ('a',28),
        ('a',26),
        ('a',23),
        ('a',22),
        ('a',20),
        ('a',19),
        ('a',16)
        ]

class MyTest(unittest.TestCase):
    
    def test_1_total_count(self):
        self.assertEqual(total_count(5,my_list_1), 7)
    # Asking for 5 values, but the list has 7 equal values, hence 
    # the function should return 7

    def test_2_total_count(self):
        self.assertEqual(total_count(10,my_list_1), 7)
    # asking for 10 values, but the list has 7 entries, so the 
    # function should return 7 
        
    def test_3_total_count(self):
        self.assertEqual(total_count(4,my_list_2), 4)
    # asking for 4 values, so the function should return 4 values
    # as all entries have different values

    def test_1_make_connection(self):
        self.assertEqual(len(make_connection()),2)
    # checks if the fuction is returning 2 values (we expect one 
    # connection and one cursor) so checks if the length is 2
            


if __name__ == '__main__':
    unittest.main()



    

    
    
    
    
    
    
    
    
    
    
    