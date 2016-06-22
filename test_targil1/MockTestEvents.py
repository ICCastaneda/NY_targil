"""
Test the Targil1 database access
and other features of the system
"""
import os
import json
# from flask.helprs import jsonify, send_file
import DBAccess

FLAG_DO_ADD = True
FLAG_DO_DELETE = True
FLAG_DO_GET_EVENTS = True

# will be converter to use python argparse and ConfigParser
ev1 = {"title": "team1 meeting", "datee": "2016-07-11", "desc":"meeting for falafel1"}
ev2 = {"title": "team2 meeting", "datee": "2016-07-12", "desc":"meeting for cake"}
ev3 = {"title": "team3 meeting", "datee": "2016-07-13", "desc":"meeting for movie"}
ev4 = {"title": "team4 meeting", "datee": "2016-07-14", "desc":"meeting hanging out"}
ev5 = {"title": "team5 meeting", "datee": "2016-07-15", "desc":"running to the sea"}
ev6 = {"title": "team6 meeting", "datee": "2016-07-16", "desc":"learning python"}
ev7 = {"title": "team7 meeting", "datee": "2016-07-17", "desc":"debate emacs or vim"}
ev8 = {"title": "team8 meeting", "datee": "2016-07-18", "desc":"discussing falsk vs Django"}
LIST_ADD_EVENTS = [ev1, ev2, ev3, ev4, ev5, ev6, ev7, ev8]
LIST_DELETE_EVENTS = [ev1, ev5]

eg1 = {"start_date": "2016-10-11", "end_date": "2016-10-17"}
eg2 = { "desc":"meeting for movie"}
LIST_GET_EVENTS = [eg1, eg2]


def do_all_tests():

    try:

        if FLAG_DO_ADD:
            for evx in LIST_ADD_EVENTS:
                MockAddEvent(evx["title"], evx["datee"], evx["desc"])

        if FLAG_DO_DELETE:
            for evx in LIST_DELETE_EVENTS:
                MockDeleteEvent(evx["title"], evx["datee"], evx["desc"])

        if FLAG_DO_GET_EVENTS:
            for evx in LIST_GET_EVENTS:

                sd = ed = desc1 = ""
                if "start_date" in evx:
                    sd = evx["start_date"]
                if "end_date" in evx:
                    ed = evx["end_date"]
                if "desc" in evx:
                    desc1 = evx["desc"]

                MockGetEvents(sd, ed, desc1)


        print "tests events system ended"

    except Exception as e:
        print "error in MockTestEvents"
        raise e

def MockGetEvents(start_date, end_date, desc):
"""
    test the web url "/get_events" 
"""     
    sqlx, sqlx_count = DBAccess.bld_query_sql(start_date, end_date, desc)
    
    list_result = DBAccess.get_events(sqlx, sqlx_count)
    if list_result[0] == 'error':
        sj = {"events_error": list_result[1]}
    else:
        sj = {"events_details": list_result[1]}
    print "MockGetEvent ended"
    print sj


def MockDeleteEvent(title1, date1, desc1):
"""
    test the web url "/delete_event" 
"""     
     
    sqlx = DBAccess.bld_delete_sql(title1, date1, desc1)

    list_result = DBAccess.delete_event(sqlx)
    if list_result[0] == 'error':
        print "MockDeleteEvent: error - {}".format(list_result[1])
    else:
        print "MockDeleteEvent: success - {}".format(list_result[1])
    return list_result[0]
    


def MockAddEvent(title1, datee, desc1):
"""
    test the web url "/add_event" 
"""     
    sqlx = DBAccess.bld_add_sql(title1, datee, desc1)

    list_result = DBAccess.add_event(sqlx)
    if list_result[0] == 'error':
        print "MockAddEvent: error - {}".format(list_result[1])
    else:
        print "MockAddEvent: success - {}".format(list_result[1])
    return list_result[0]
    

if __name__ == '__main__':
    print 'In MockTestEvents - main'
    do_all_tests()



# list_events = MockGetEventsByTitle(title="title1")"
# list_events = MockGetEventsByDates(start_date="20160101", end_date="20160215")
# list_events = MockGetEventsByDatesAndTitle(start_date, end_date, title)
# new_event = MockUpdateEvent(event_date="20160831")
# del_event = MockDeleteEvent(event_date, event_title)
