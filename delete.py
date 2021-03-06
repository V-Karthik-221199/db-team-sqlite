#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 

Course work: 

@author:

Source:
    
'''
import sqlite3
import random
from sqlite3 import Error

import zenv

database = zenv.DB_LOCATION

def start():
    """
    Query all rows in the CITY table
    :param conn: the Connection object
    :return:
    """    
    conn = None
    
    try:
        conn = sqlite3.connect(database)        
    except Error as e:
        return (e)
    
    sql = ''' DELETE FROM MOVIE
    WHERE MOVIE_NAME = :name 
    '''
    cur = conn.cursor()
    
    try:
        cur.execute(sql, ('Asuran',))       
    except sqlite3.IntegrityError as sqle:
        return ("SQLite error : {0}".format(sqle))
    finally:        
        conn.commit()
    
    return('Deleted!')

if __name__ == '__main__':
    start()        