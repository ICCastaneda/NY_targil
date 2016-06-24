This system manipulate the EVENTS database.
adding, deleting, updating and listing the events.
The sytem creat a new diary file on every cahnge of events
and take backup of the database as neede, or will be intgrated
in a night backup process.

The API
the api to all the web interface are dict(json) in the form of:
{["ID":"id",] "event_title":"title", "event_date":"date", "event_desc":"desc"}

The Api to the get_events are: start_date and or end_date and or event_desc

@app.route('/add_event', methods=["GET"]) 
def add_event():

@app.route('/delete_event', methods=["GET"])
def delete_event():

@app.route('/update_event', methods=["GET"])
def update_event():

@app.route('/get_events', methods=["GET"])
def get_events():

Motivation

The project was cread as an exercise to maintain and manipulate diary database

Installation

Clone the system from GitHub and follow the instruction to run it in the scripts folder

API Reference

See the above explanations

Tests

Run the test as describe in the scripts folder file run_TestEvents.bat

Contributors

This is a small project and done by me


General remarks
.- Testing of the database interface was done thru the test_targil1 system. 


Packages
-----------------
MySQL / MariaDB connector - http://dev.mysql.com/downloads/connector/python/

.- How to create the Database on MariaDB
-----------------------------------------
.- create database targil1 character set utf8 collate utf8_general_ci;

.- create table tg1_events (id int(11) not null auto_increment, event_title varchar(30) default null, event_date datetime default null, event_desc varchar(50), primary key (id) ) ENGINE=InnoDB DEFAULT CHARSET=utf8;

.- Choose the user and pw replacing the '*****'
.- GRANT ALL PRIVILEGES on targil1.* to ******@'%' IDENTIFIED BY '******' with grant option;
.- GRANT ALL PRIVILEGES on *.* to ******@localhost IDENTIFIED BY '******' with grant option;


.- Small sample of the database
-----------------------
MariaDB [targil1]> select * from tg1_events;
+----+---------------+---------------------+----------------------------+
| id | event_title   | event_date          | event_desc                 |
+----+---------------+---------------------+----------------------------+
| 18 | bbbbb         | 2016-10-11 00:00:00 | bbbbdesc                   |
| 19 | ccccc         | 2016-10-12 00:00:00 | cccccesc                   |
| 20 | ddddd         | 2016-10-13 00:00:00 | dddddesc                   |
| 21 | eeeee         | 2016-10-14 00:00:00 | eeeeedesc                  |
| 22 | kkkkkddddd    | 2016-10-15 00:00:00 | kkkdddddesc                |
| 24 | team2 meeting | 2016-07-12 00:00:00 | meeting for cake           |
| 25 | team3 meeting | 2016-07-13 00:00:00 | meeting for movie          |
| 26 | team4 meeting | 2016-07-14 00:00:00 | meeting hanging out        |
| 28 | team6 meeting | 2016-07-16 00:00:00 | learning python            |
| 29 | team7 meeting | 2016-07-17 00:00:00 | debate emacs or vim        |
| 30 | team8 meeting | 2016-07-18 00:00:00 | discussing falsk vs Django |
| 32 | team2 meeting | 2016-07-12 00:00:00 | meeting for cake           |
| 33 | team3 meeting | 2016-07-13 00:00:00 | meeting for movie          |
| 34 | team4 meeting | 2016-07-14 00:00:00 | meeting hanging out        |
| 36 | team6 meeting | 2016-07-16 00:00:00 | learning python            |
| 37 | team7 meeting | 2016-07-17 00:00:00 | debate emacs or vim        |
| 38 | team8 meeting | 2016-07-18 00:00:00 | discussing falsk vs Django |
| 39 | curl1         | 2016-06-22 00:00:00 | aaaadesc                   |
+----+---------------+---------------------+----------------------------+
18 rows in set (0.00 sec)

The folowing tesings were done using cURL:
-------------------------------------------
.- get_events - curl '127.0.0.1:5000/get_events?start_date=2016-01-01&end_date=2016-12-31'

.- add event (worked) - curl '127.0.0.1:5000/add_event?add_data={"event_title":"adesc", "event_date":"2091-01-01", "event_desc":"zzzzzzzzzzxxxxxxthisdesc"}'
     .- add_event (w/get-worked) - @app.route('/add_event', methods=["GET"])  #worked

.- delete_event (worked w/get) - curl '127.0.0.1:5000/delete_event?delete_data={"event_title":"aaaadesc"}'

Results of cURL add_event
-------------------------
StatusCode        : 200
StatusDescription : OK
Content           : {
                      "add_event successeded": "event added succesfully"
                    }

RawContent        : HTTP/1.0 200 OK
                    Content-Length: 57
                    Content-Type: application/json
                    Date: Wed, 22 Jun 2016 10:59:48 GMT
                    Server: Werkzeug/0.11.10 Python/2.7

                    {
                      "add_event successeded": "event added succesfully"
                    ...
Forms             : {}
Headers           : {[Content-Length, 57], [Content-Type, application/json], [Date, Wed, 22 Jun 2016 10:59:48 GMT],
                    [Server, Werkzeug/0.11.10 Python/2.7]}
Images            : {}
InputFields       : {}
Links             : {}
ParsedHtml        : mshtml.HTMLDocumentClass
RawContentLength  : 57


Results of cURL delete_event
-----------------------------
StatusCode        : 200
StatusDescription : OK
Content           : {
                      "delete_event successeded": "event deleted successfully"
                    }

RawContent        : HTTP/1.0 200 OK
                    Content-Length: 63
                    Content-Type: application/json
                    Date: Wed, 22 Jun 2016 10:57:26 GMT
                    Server: Werkzeug/0.11.10 Python/2.7

                    {
                      "delete_event successeded": "event deleted successf...
Forms             : {}
Headers           : {[Content-Length, 63], [Content-Type, application/json], [Date, Wed, 22 Jun 2016 10:57:26 GMT],
                    [Server, Werkzeug/0.11.10 Python/2.7]}
Images            : {}
InputFields       : {}
Links             : {}
ParsedHtml        : mshtml.HTMLDocumentClass
RawContentLength  : 63

result of get_events
---------------------
StatusCode        : 200
StatusDescription : OK
Content           : {
                      "events_details": [
                        {
                          "count": 19
                        },
                        {
                          "event_date": "Tue, 12 Jul 2016 00:00:00 GMT",
                          "event_desc": "meeting for cake",
                          "event_title": "team2 meeting",
                        ...
RawContent        : HTTP/1.0 200 OK
                    Content-Length: 3086
                    Content-Type: application/json
                    Date: Wed, 22 Jun 2016 10:41:56 GMT
                    Server: Werkzeug/0.11.10 Python/2.7

                    {
                      "events_details": [
                        {
                          "count": 19
                        }...
Forms             : {}
Headers           : {[Content-Length, 3086], [Content-Type, application/json], [Date, Wed, 22 Jun 2016 10:41:56 GMT],
                    [Server, Werkzeug/0.11.10 Python/2.7]}
Images            : {}
InputFields       : {}
Links             : {}
ParsedHtml        : mshtml.HTMLDocumentClass
RawContentLength  : 3086