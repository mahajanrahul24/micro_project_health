# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 16:21:32 2018

@author: andrease
"""

import unittest
from calories import define_met

class MyTest(unittest.TestCase):
   def test_my_function(self):
        self.assertEqual(define_met('1'), 3.5)
        self.assertEqual(define_met('2'), 8)
        self.assertEqual(define_met('3'), 8.8)
        self.assertEqual(define_met('0'), 0)

        
if __name__ == '__main__':
    unittest.main()
    