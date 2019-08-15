#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 17:34:24 2019

@author: mayur
"""

import flask
import sqlite3
from sqlite3 import Error
import numpy as np
import sys

sys.stdout.flush()

def make_connection():
    """
    This function mskes a connection to a database and 
    returns connection and cursor
    """
    
    try:
        conn = sqlite3.connect(
                '/usr/local/bin/testdb.db')
        c = conn.cursor()
    except Error as e:
            print(e)
    
    print('connected to database', flush=True)
    
    return (conn,c)




def total_count(n, people_list): 
    """
    This function calculates the total number of records
    to be fetched when a user has requested n top records
    and there is a tie at the nth record
    """
    
    if n< len(people_list):
        j = 0  
        for i in range(n,len(people_list),1):
            if people_list[i][1] == people_list[i-1][1]:
                j = j +1
            else:
                break 
        n = n + j 
    else:
        n = len(people_list)
        
    return n


def insertinto_frequest_browsers(c, conn, sql, people_list,n):
    """
    This function is used to insert data into frequest_browsers table.
    The logic used in this function is as follows:
    
    1. make a string of names whose record is to be inserted to 
    check their existence in the database (check_list_text)
    
    2. execute two queries to fetch all the names (duplicate_list)and 
    their site visit counts (duplicate_list_sites)
    
    3. IF duplicate_list is empty:
        then insert all the values in the database
    Else 
        for loop for all duplicate list entries which
        - fetches the number of sites visited by the
        person
        - checks if the count in db is less (can check for not equal depending
        on logic we decide)
        - if yes, then updates the record
        
    4.Since all duplicate entries are updates, we find people_tobe_added
    i.e. names of people different from the duplicate listand their 
    site visit count
    
    5. Add people_tobe_added records in db
    
    
    """
    
    check_list = list()
    for i in range(len(people_list)):
        check_list.append(people_list[i][0])
    check_list_text = '''('%s')''' % "','".join(str(m) for m in check_list)
    
    print('check list' + check_list_text, flush=True)
    
    try:
        c.execute(
                  """
                  select person_id 
                  from frequent_browsers
                  where person_id in 
                  """ + 
                  check_list_text
                  )
        
        duplicate_list = c.fetchall()
        
    except sqlite3.IntegrityError as e:
      print('sqlite error: ', e.args[0])
      
    try:
        c.execute(
                  """
                  select num_sites_visited 
                  from frequent_browsers
                  where person_id in 
                  """ + 
                  check_list_text
                  )
        
        duplicate_list_sites = c.fetchall()
        
    except sqlite3.IntegrityError as e:
      print('sqlite error: ', e.args[0])
    
    if len(duplicate_list) == 0:
        try:
            sql = '''INSERT INTO frequent_browsers 
                      (person_id, num_sites_visited) VALUES (?, ?)'''
            c.executemany(sql, people_list[:n])
        except sqlite3.IntegrityError as e:
            print('sqlite error: ', e.args[0]) 
        
    
    else:
        for i in range(len(duplicate_list)):
            try:
                c.execute(
                        """
                        select num_sites_visited 
                        from frequent_browsers
                        where person_id = '""" + str(duplicate_list[i][0]) + "'"
                        )
            except sqlite3.IntegrityError as e:
                print('sqlite error: ', e.args[0])
                
            actual_record = c.fetchall()
            
            if actual_record[0][0] < duplicate_list_sites[i][0]:
                try:
                    c.execute(
                        """
                        update frequent_browsers
                        set num_sites_visited = '
                        """ + str(duplicate_list[i][1]) + "'"
                        """
                        where person_id = 
                        """
                        + str(duplicate_list[i][0])
                        )
                except sqlite3.IntegrityError as e:
                    print('sqlite error: ', e.args[0])
                    
                    
        people_tobe_added = np.setdiff1d(check_list,duplicate_list)
        people_tobe_added_text = '''('%s')''' % "','".join(
                str(m) for m in people_tobe_added)
        try:
            c.execute(
                  """
                  select person_id 
                  from frequent_browsers
                  where person_id in 
                  """ + 
                  people_tobe_added_text
                  )
        except sqlite3.IntegrityError as e:
            print('sqlite error: ', e.args[0])
    conn.commit()
            
                
 
"""
Till here we have upated the db, now we will write an api to 
expose the result to the world i.e. on a web browser
"""
app = flask.Flask('__name__')
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])

def home():  
    conn,c = make_connection()
    c.execute('''
              select p.first_name || ' ' ||  p.last_name, count(v.siteID)
              as Count_visits
              from visits v inner join people p
              on v.personID = p.id
              group by personID
              order by Count_visits desc
              ''')
    
    people_list=(c.fetchall())
    print(people_list)
    
    n = 10
    n = total_count(n, people_list)
    
    people_list = people_list[:n]
    
    ## just to ensure its my first insertion
    ## c.execute(''' delete from frequent_browsers ''') 
    
    sql = '''INSERT INTO frequent_browsers 
                  (person_id, num_sites_visited) VALUES (?, ?)'''
    
    insertinto_frequest_browsers(c, conn, sql, people_list,n)
    #people_list = dict(people_list)
    
    display_list = '\n'.join(str(m) for m in people_list)
    
    return display_list


if __name__ == '__main__':
    app.run(host='0.0.0.0')

print('committed \n Code fully executed')


"""

The below code has been kept to have a refernce of db and
help in better explanation during discussion

c.execute('''SELECT name FROM sqlite_master 
             WHERE type='table' 
             ORDER BY name;
          ''')
available_table=(c.fetchall())

names = list(map(lambda x: x[0], c.description))
names = [description[0] for description in c.description]



visits = personID, siteID, time_visited
people = id, first_name, last_name
sites = id, url
frequemt_browsers = person_id, num_sites_visited
sqlite_sequence = name, seq

c.execute('''
          select * from frequent_browsers
          ''')

c.execute('''
          select * from visits
          ''')
exit
"""