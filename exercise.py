#!/usr/bin/python
# -*- coding: utf-8 -*-
# importing a PostrgeSQL database to use with Python

import psycopg2
import sys


con = None

try:
     
    con = psycopg2.connect(database='dilling_bihomework_one', user='dilling') 
    cur = con.cursor()
    cur.execute('SELECT version()')          
    ver = cur.fetchone()
    print ver    
    

except psycopg2.DatabaseError, e:
    print 'Error %s' % e    
    sys.exit(1)
    
    
finally:
    
    if con:
        con.close()

#This creates a python object with the value from the query - return top 20 values
#Which 20 languages had the highest total number of requests?
question1 = plpy.execute("SELECT language, SUM(requests) FROM dilling_bihomework_one GROUP BY language ORDER BY SUM(requests)DESC, 20")


#sort for all entries with top 20 lang, create new table 
question1a = plpy.execute("SELECT language, page_name, requests, bytes FROM dilling_bihomework_one WHERE language = 'en', or 'ja', or 'ru', or 'de', or 'fr', or 'es', or 'it', or 'pl', or 'pt', or 'zh', or 'nl', or 'tr', or 'sv', or 'ar', or 'ko', or 'uk', or 'cs', or 'id', or 'fi', or 'no'")

CREATE TABLE question1a (language text, page_name text, requests integer, bytes integer)

#Which language had the highest median page size (bytes sent per request)?
question2 = plpy.execute("SELECT language, SUM(requests) FROM question1a GROUP BY language ORDER BY SUM(requests)DESC")


#How many total requests were made to pages with names containing the substring “Obama”?
question3 = plpy.execute("SELECT SUM(requests) AS TotalRequests FROM question1a WHERE page_name LIKE '%Obama%';")


#Other than English, which language had the most Obama pages and how many pages did it have?
question4 = plpy.execute("SELECT SUM(requests) AS TotalRequests FROM question1a WHERE page_name LIKE '%Obama%'GROUP BY language, 2;")


#How many English pages have the same name as a Spanish page?
# Select english data
question5 = plpy.execute("SELECT language, page_name, requets, bytes FROM question1a GROUP BY language = 'en'")

#create table of "en" entries (Name english)
CREATE TABLE english (language text, page_name text, requests integer, bytes integer)

#create spanish data
question5a = plpy.execute("SELECT language, page_name, requests, bytes FROM question1a GROUP BY language = 'es'") 

#create table of "es" entries (Name spanish)
CREATE TABLE spanish (language text, page_name text, requests integer, bytes integer)

question5b = plpy.execute("SELECT COUNT page_name AS Requests FROM english INNER JOIN spanish ON english.page_name=spanish.page_name;")

#Which of those pages had the most total English and Spanish bytes sent?

question5c = plpy.execute("SELECT COUNT page_name AS Requests FROM english INNER JOIN spanish ON english.page_name=spanish.page_name ORDER BY bytes DESC;")

#Construct one or more data visualizations which shows the relationship between the number of words in a page title (where words are underscore delimited), and the number of requests.

question6 = plpy.execute("SELECT requests, page_name(regexp_count(col, '_')) + 1 AS word_count FROM question1a ORDER BY requests DESC;")
