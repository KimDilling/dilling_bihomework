# dilling_bihomework

I listed my notes and discussion here in the README for review. I reviewed the data through a SQL lens before incorporating into Python. I have never used the two together but it seemed to be the best approach for this particular data set.  


# BI_exercise

	Setting a PostrgeSQL database within Python for more efficient data manipulation.

	Check if the PostgreSQL server is running. If not, start the server.

	$ sudo service postgresql start
	 * Starting PostgreSQL 9.1 database server 

	Use the service postgresql stop command to stop the PostgreSQL server.

	$ sudo apt-get install python-psycopg2

	Create a new role in the PostgreSQL system.   Note that this works only on localhost.

	$ sudo -u postgres createdb **dilling_bihomework_one -O dilling

1. Which 20 languages had the highest total number of requests? For the remainder of this assignment, only use data from these 20 languages.

Confirmed via SQL code:
SELECT language, SUM(requests) FROM dilling_bihomework_one
GROUP BY language
ORDER BY SUM(requests)DESC
LIMIT 20;

"en";9388430
"ja";1803179
"ru";1614173
"de";1598937
"fr";1127308
"es";906771
"it";826731
"pl";749191
"pt";528600
"zh";436694
"nl";355134
"tr";237259
"sv";198231
"ar";163671
"ko";138486
"uk";127681
"cs";124883
"id";111638
"fi";108501
"no";91683


2. Which language had the highest median page size (bytes sent per request)?

SELECT language, AVG(requests/bytes) FROM question1a
GROUP BY language
ORDER BY AVG(requests/bytes)DESC
LIMIT 1;

3. How many total requests were made to pages with names containing the substring “Obama”?

SELECT SUM(requests) AS TotalRequests FROM question1a
WHERE page_name LIKE '%Obama%';

4. Other than English, which language had the most Obama pages and how many pages did it have?

SELECT SUM(requests) AS TotalRequests FROM question1a
WHERE page_name LIKE '%Obama%'
GROUP BY language
LIMIT 2;

5. How many English pages have the same name as a Spanish page? 

SELECT language, page_name, bytes FROM question1a
WHERE language = "en" 
#create table of "en" entries (Name english)

SELECT language, page_name, bytes FROM question1a
WHERE language = "es" 
#create table of "es" entries (Name spanish)

SELECT COUNT page_name
FROM english
INNER JOIN spanish
ON english.page_name=spanish.page_name;

Which of those pages had the most total English and Spanish bytes sent?

SELECT page_name, bytes
FROM english
INNER JOIN spanish
ON english.page_name=spanish.page_name
ORDER BY bytes DESC;

6. Construct one or more data visualizations which shows the relationship between the number of words in a page title (where words are underscore delimited), and the number of requests.

SELECT regexp_count(col, '_') + 1
  from table 

7. Please include any other interesting analyses and/or visualizations that you have produced.

I am interested in incorporating building charts directly from Python as a new skill. I have limited experience with this but have been working on some exercises for this functionality. 


8. Please note here any bugs you may have found in the data or assignment instructions.

Using the SQL search capabilities within Python scripting makes it easy to search for LIKE matches without having to code several use cases (lowercase, upppercase, contains, etc). It also helps with the processing of large sets of data that would become cumbersome as dictionaries within one large python piece. Ideally I should have used the SQLite that is normally associated with Python. However, I had Postgres on my laptop and unstable WiFi so it was better to progress with what I had available.

It is obvious that some of the page_name(s) are either encoded or translated. For example - "%E3%83%A9%E3%83%B3%E3%83%87%E3%82%A3%E3%83%BB%E3%82%A6%E3%82%A7%E3%83%AB%E3%82%BA" will not readily translate into searchable text for analysis. This would require another iteration through the data to remove these listings and account for the percentage that could not be included in any calculations.


***
