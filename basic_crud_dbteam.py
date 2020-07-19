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
import datetime

import zenv

database = zenv.DB_LOCATION


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return None


''' DB TEAM WORK STARTED '''


def select_all_movies_1(conn):
    cur = conn.cursor()
    sql = ''' SELECT * FROM MOVIE '''

    try:
        cur.execute(sql)

    except sqlite3.IntegrityError as sqle:
        return("SQLite error : {0}".format(sqle))
    
    rows = cur.fetchall()
    print(rows)

def create_public_artist_table_schema(conn):
    cur = conn.cursor()
    sql = ''' CREATE TABLE "PUBLIC_ARTIST" (
	"AID"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"ARTIST_NAME"	TEXT NOT NULL UNIQUE,
	"ORIGINAL_NAME" TEXT,
	"DOB"	TEXT,
	"LOCATION"	TEXT,
	"COUNTRY" TEXT,
	"DESCRIPTION" TEXT,
	"PIC_LOCATION" TEXT );  '''

    try:
        cur.execute(sql)

    except sqlite3.IntegrityError as sqle:
        return("SQLite error : {0}".format(sqle))
    
    print("PAT created successfully")

    
def create_movie_artist_table_schema(conn):
    cur = conn.cursor()
    sql = ''' CREATE TABLE "MOVIE_ARTIST" (
	"MAID"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"MOVIE_ID"	TEXT NOT NULL,
	"ARTIST_ID"	INTEGER NOT NULL,
	"ARTIST_ROLE"	TEXT NOT NULL );  '''

    try:
        cur.execute(sql)

    except sqlite3.IntegrityError as sqle:
        return("SQLite error : {0}".format(sqle))
    
    print("MAT created successfully")


def create_coartist_bubble_table_schema(conn):
    cur = conn.cursor()
    sql = ''' CREATE TABLE "COARTIST_BUBBLE" (
	"CBID"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"ARTIST_ID"	TEXT NOT NULL,
	"ARTIST_CATEGORY" TEXT NOT NULL,
	"COARTIST_ID"	TEXT NOT NULL,
	"COARTIST_CATEGORY"	TEXT NOT NULL,
	"BUBBLE_SCORE"	INTEGER NOT NULL,
	"USER_IP" TEXT,
	"USERID" INT,
	"UPDATED_AT" TEXT ); '''

    try:
        cur.execute(sql)

    except sqlite3.IntegrityError as sqle:
        return("SQLite error : {0}".format(sqle))
    
    print("CAB created successfully")


def create_artist_score_table_schema(conn):
    cur = conn.cursor()
    sql = ''' CREATE TABLE "ARTIST_SCORE" (
	"ASID"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"ARTIST_ID"	TEXT NOT NULL,
	"YEAR"	INTEGER NOT NULL,
	"CRITIC_SCORE"	INTEGER NOT NULL,
	"AUDIENCE_SCORE"	INTEGER NOT NULL,
	"BOX_OFFICE_SCORE"	INTEGER NOT NULL,
	"USER_IP" TEXT,
	"USERID" INT,
	"UPDATED_AT" TEXT ); '''

    try:
        cur.execute(sql)

    except sqlite3.IntegrityError as sqle:
        return("SQLite error : {0}".format(sqle))
    
    print("AS created successfully")


'''SCHEMA ENDED '''

def get_actor_id(conn, actor_name):
    """
    Query all rows in the MOVIE table
    :param conn: the Connection object
    :return:
    """

    sql = """
    SELECT
	    PA.AID AS 'ARTIST_ID'
    FROM PUBLIC_ARTIST PA
    WHERE PA.ARTIST_NAME = :actor_name COLLATE NOCASE;
    """

    actor_obj = {
        'actor_name': actor_name
    }

    cur = conn.cursor()
    cur.execute(sql, actor_obj)

    rows = cur.fetchall()

    # print('rows count : '+str(len(rows)))

    if(len(rows) <= 0):
        print('No Data available')
        return -1

    for row in rows:
        # print(row)

        return row[0]

    return -1

def insert_into_artist_score(conn,artist_obj):
    print(artist_obj['name'])
    id = get_actor_id(conn,artist_obj['name'])

    cur = conn.cursor()

    artist_obj['id'] = id

    sql = ''' INSERT INTO ARTIST_SCORE (ARTIST_ID,YEAR,CRITIC_SCORE,AUDIENCE_SCORE,BOX_OFFICE_SCORE,USER_IP,USERID,UPDATED_AT) 
              VALUES (:id,:year,:c_score,:a_score,:b_score,:user_ip,:user_id,:updated_at) ''' 
    
    try:
        cur.execute(sql,artist_obj)

    except sqlite3.IntegrityError as sqle:
        return("SQLite error : {0}".format(sqle))
    
    print("AS Inserted successfully")


def insert_into_public_artist(conn,public_artist_obj):
    print(artist_obj['name'])
    id = get_actor_id(conn,artist_obj['name'])

    cur = conn.cursor()

    artist_obj['id'] = id

    sql = ''' INSERT INTO PUBLIC_ARTIST (ARTIST_NAME,ORIGINAL_NAME,DOB,LOCATION,COUNTRY,DESCRIPTION,PIC_LOCATION) 
              VALUES (:name,:original-_name,:dob,:location,:country,:description,:pic_loc) ''' 
    
    try:
        cur.execute(sql,artist_obj)

    except sqlite3.IntegrityError as sqle:
        return("SQLite error : {0}".format(sqle))
    
    print("AS Inserted successfully")



''' DB TEAM WORK ENDED '''


def select_all(conn):
    """
    Query all rows in the MOVIE table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM MOVIE")

    rows = cur.fetchall()

    # return('rows count : '+str(len(rows)))

    if(len(rows) <= 0):
        return('No Data available')
    return rows
    # for row in rows:
    #     print(row)


def select_all_by_actor(conn, actor_name):
    """
    Query all rows in the MOVIE table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM COARTIST_BUBBLE WHERE ARTIST_NAME LIKE '%"+actor_name+"%'")

    rows = cur.fetchall()

    #print('rows count : '+str(len(rows)))

    if(len(rows) <= 0):
        return('No Data available')

    for row in rows:
        return(row)


def add_coartist_bubble(conn, bubble_obj):
    """
    Create a movie
    :param task:
    :return: task id
    """

    sql = ''' INSERT INTO COARTIST_BUBBLE (ARTIST_NAME, COARTIST_CATEGORY, COARTIST_NAME, BUBBLE_SCORE) 
            VALUES (:artist_name, :coartist_category, :coartist_name, :bubble_score) '''
    cur = conn.cursor()

    lastrowid = -1
    try:
        cur.execute(sql, bubble_obj)

        lastrowid = cur.lastrowid
    except sqlite3.IntegrityError as sqle:
        return("SQLite error : {0}".format(sqle))
    finally:
        conn.commit()

    return lastrowid


def update_movie(conn, bubble_obj):
    """
    Create a movie
    :param movie object:
    :return: None
    """

    sql = ''' UPDATE MOVIE
    SET MOVIE_NAME = :new_name, 
    STARRING = :starring,
    RELEASE_DATE = :release_date 
    WHERE MOVIE_NAME = :name '''
    cur = conn.cursor()

    try:
        cur.execute(sql, bubble_obj)

    except sqlite3.IntegrityError as sqle:
        return("SQLite error : {0}".format(sqle))
    finally:
        conn.commit()

    return('Updated')


def delete_movie(conn, name):
    """
    Delete a movie
    :param movie object:
    :return: None
    """

    sql = ''' DELETE FROM MOVIE    
    WHERE MOVIE_NAME = ?'''
    cur = conn.cursor()

    try:
        cur.execute(sql, (name,))

    except sqlite3.IntegrityError as sqle:
        return("SQLite error : {0}".format(sqle))
    finally:
        conn.commit()

    return('Deleted')


def delete_all_cities(conn):
    """
    Delete a movie
    :param movie object:
    :return: None
    """

    sql = ''' DELETE FROM MOVIE '''
    cur = conn.cursor()

    try:
        cur.execute(sql)

    except sqlite3.IntegrityError as sqle:
        return("SQLite error : {0}".format(sqle))
    finally:
        conn.commit()

    return('Delete')


def main():

    # create a database connection
    conn = create_connection(database)

    with conn:
        #print("TEST-select all movies ")
        #select_all_movies_1(conn)
        
        current_date = datetime.date.today()
        date = current_date.strftime("%d-%m-%Y")

        artist_obj = {
            'name': 'Dhanush',
            'year': 2022,
            'c_score': 85,
            'a_score': 90,
            'b_score': 88,
            'user_ip': '',
            'user_id': '',
            'updated_at': date
        }
        print("Insert stmt test")
        insert_into_artist_score(conn,artist_obj)

        


        # CREATE
        # :artist_name, :coartist_category, :coartist_name, :bubble_score
        #print('Create Coartist Bubble')
        #bubble_obj = { 'artist_name': 'Dhanush', 'coartist_category': 'actress', 'coartist_name': 'Kajal Agarwal','bubble_score': 70} 
        #'''result = add_coartist_bubble(conn, bubble_obj)
        #print(result)
        #print('---------------\n')

        # READ
        # print('Read Movie')
        # select_all(conn)
        # print('---------------\n')

        # READ by Name
        #print('Read Coartist Bubble by Name')
        #select_all_by_actor(conn, 'Dhanush')
        #print('---------------\n')

        # UPDATE
        # print('Update Movie')
        # city_new_obj = {
        #     'name' : 'Asuran',
        #     'new_name' : 'Asuran',
        #     'starring' : 'Dhanush, TeeJay, Ken Karunas',
        #     'release_date' : '4 Oct 2019'
        # }
        # update_movie(conn, city_new_obj)
        # print('---------------\n')

        # DELETE
        # print('Delete Movie')
        # delete_movie(conn, 'Kadal')
        # print('---------------\n') '''


if __name__ == '__main__':
    main()
