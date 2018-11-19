#!/usr/bin/env python3

import psycopg2

db = psycopg2.connect("dbname=news")

cursor = db.cursor()

results = []

q1 = [("1-", "What are the most popular three articles of all time?")]

results.append(q1)

cursor.execute("SELECT \
(SELECT articles.title \
FROM articles \
where articles.slug = substring(log.path,10,55)) AS ArticleTitle,\
COUNT(log.id) \
FROM log\
 WHERE log.path like '%article%' \
 GROUP BY log.path \
 ORDER BY COUNT(log.id) DESC LIMIT 3 ")

results.append(cursor.fetchall())

cursor.execute("SELECT \
(SELECT authors.name FROM authors WHERE authors.id IN \
(SELECT articles.author \
FROM articles \
WHERE articles.slug  = substring(log.path,10,50))) As Author,\
count(log.id) \
FROM log  \
WHERE log.path LIKE'%article%' \
AND status like '%200%' \
GROUP BY Author ORDER BY count(log.id) DESC")

q2 = [("2-", "Who are the most popular article authors of all time?")]

results.append(q2)

results.append(cursor.fetchall())

cursor.execute("SELECT count_table.percentage, count_table.date FROM ( \
SELECT \
sum((SELECT count(*)  \
FROM log \
WHERE log.id = logs.id AND log.status like '%404%')) \
/ sum((SELECT count(*) FROM log WHERE log.id = logs.id ))*100 AS percentage,\
date(time) AS Date \
FROM log logs \
GROUP BY date(time) ORDER BY percentage desc)count_table WHERE percentage >1")

q3 = [("3-", "On which days did more than 1% of requests lead to errors?")]

results.append(q3)

results.append(cursor.fetchall())

for row in results:
    for r in row:
        if str(r[1]).endswith("?"):
            print(r[0], str(r[1]))
        elif "-" in str(r[1]):
            print(r[0], str(r[1])+" Errors")
        else:
            print(r[0], str(r[1])+" -- Views")
db.close()
