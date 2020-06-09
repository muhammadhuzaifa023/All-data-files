# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 12:26:22 2020

@author: HASSAN ENTERPRISES
"""

import sqlite3
from sqlite3 import Error
def connect():
    try:
        con=sqlite3.connect("bb.db")
        print('connected')
    except Error:
        print(Error)
    finally:
        print('done')
        return con
connect() 
    