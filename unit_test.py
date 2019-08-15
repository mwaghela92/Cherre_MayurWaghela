#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 14:14:31 2019

@author: mayur
"""

import unittest
import sqlite3

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
        ('a',28),
        ('a',28),
        ('a',28),
        ('a',28),
        ('a',28),
        ('a',28)
        ]

my_list_3 = [
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

    def test_2_total_count(self):
        self.assertEqual(total_count(10,my_list_2), 7)
        
    def test_3_total_count(self):
        self.assertEqual(total_count(4,my_list_3), 4)

    def test_1_make_connection(self):
        self.assertEqual(len(make_connection()),2)
            


if __name__ == '__main__':
    unittest.main()



    

    
    
    
    
    
    
    
    
    
    