#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3

def sqlite3_create_db():
    con = sqlite3.connect('./database.db')

    cur = con.cursor()

    cur.execute('CREATE TABLE IF NOT EXISTS bot_request(Question TEXT, '
                                                        'Contacts TEXT)')


    cur.close()
    con.commit()

def print_data_2d(columns_names, data):
    print(columns_names)
    for line in data:
        print(line)
    print('number of lines in db table is '+str(len(data)))


def sqlite3_read_db(data_base, table, column_name = None):
    con = sqlite3.connect('./database.db')

    cur = con.cursor()
    query_columns = 'pragma table_info('+table+')'
    cur.execute(query_columns)
    columns_description = cur.fetchall()
    columns_names = []
    for column in columns_description:
        columns_names.append(column[1])

    if column_name is None:
        query = 'SELECT * FROM '+table
        cur.execute(query)
        data = cur.fetchall()
    else:
        query = 'SELECT '+column_name+' FROM '+table
        cur.execute(query)
        data = cur.fetchall()
        new_data = []
        for element in data:
            new_data.append(element[0])
            data = new_data
            del(new_data)

    print_data_2d(columns_names, data)
    cur.close()
    con.close()

def sqlite3_add_record(data_base, data, table):
    con = sqlite3.connect(data_base)

    cur = con.cursor()
    query = 'INSERT INTO '+table+' VALUES(?, ?)'
    cur.execute(query, data)
    con.commit()
    cur.close()
    con.close()

def sqlite3_delete_table(data_base, table):
    con = sqlite3.connect(data_base)

    cur = con.cursor()
    query = 'DROP TABLE IF EXISTS '+table
    cur.execute(query)
    cur.close()
    con.close()

def sqlite3_delete_record(data_base, table, id_column, record_id):
    con = sqlite3.connect(data_base)

    cur = con.cursor()
    query = 'DELETE FROM '+table+' WHERE '+id_column+" = '"+record_id+"'"
    cur.execute(query)
    con.commit()
    cur.close()
    con.close()

def sqlite3_update_record(data_base, table, id_column, record_id, param_column, param_val):
    con = sqlite3.connect(data_base)

    cur = con.cursor()
    query = 'UPDATE '+table+' SET '+param_column+'='+str(param_val)+' WHERE '+id_column+" = '"+str(record_id)+"'"
    cur.execute(query)
    con.commit()
    cur.close()
    con.close()