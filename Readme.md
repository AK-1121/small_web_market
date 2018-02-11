
<h1>Small web market (SWM)</h1>
Here is a small web-stores agregator that is written on Flask (Python3). As database it uses Sqlite. It supports hierarhical structure of products by product types and sub types.
It displays product haracteristics, photo and offers in different web stores. Also it show raitings for products and stores.
SWM - runs on all main operating system (cross-platform project).

<h2>Getting started</h2>
1. Clone project from Github: git clone: https://github.com/AK-1121/small_web_market
2. Install Python3 it you don't have it on your PC or laptop
3. install required Python3 libraries from requirements.txt
4. Set in config file (config.py in main directory of the project) paths to templates directory, directory for static files, path to sqlite3 db-file.
5. Run market with command: python3 app.py
(after the start it creates new database file if it is not exists)
6. CRUD data in the market with the help of cli-tool: sqlite3. Also bulk operations can be performed with using text files with SQL-queries:
sqlite3 data.db < insert_test_data.sql

<Author>
Alexey Kuznetsov. Here will be my contacts:...

<h2>License</h2>
This project is licensed under the MIT License - see the LICENSE.md file for details

<h2>Notes</h2>
1. Static files (images of products) are in static directory. Web service not convert (resized) it on-flight so
it will be better to prepare images before using (make fixed dimentions).
2. For preparing images may use utility
Example: 
sudo apt-get install imagemagick
convert -resize 1024X768  source.png dest.jpg 
3. insert_test_data.sql - example with inserting queries to DB
4. in default directory for static files there are images for test data from insert_test_data.sql
