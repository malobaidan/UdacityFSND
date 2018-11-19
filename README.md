### Project: Logs Analysis

About:
This is the first project of Udacity full stack course Nanodegree, in this project we build a python script and try to make a reporting tool to know what the blog readers like and if there is errors in the blog.

#### Requirements:
1- Python3.
- psycopg2.

2- Vagrant.

3- Virtualbox.

4- newsdata.sql file.

#### How to run:

``` Navigate to the diractory and open the terminal then run: $vagrant up, then $vagrant ssh,```

``` navigate to the shared folder by cd /vagrant```

```To load the data, use the terminal command psql -d news -f newsdata.sql to connect a database and run the necessary SQL statements```

``` then run the command in the terminal $python3 articals.py```

#### database tables:
- authors.
- articals.
- log.
