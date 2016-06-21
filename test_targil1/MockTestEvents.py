"""
Test the Targil1 database access
and other features of the system
"""
import os
import json
# from flask.helprs import jsonify, send_file
import DBAccess

# can convert later to config file
ev1 = {"title": "team1 meeting", "datee": "2016-07-11", "desc":"meeting for cake"}
ev2 = {"title": "team2 meeting", "datee": "2016-07-17", "desc":"meeting for falafel"}
LIST_ADD_EVENTS = [ev1, ev2]

eg1 = {"start_date": "2016-10-11", "end_date": "2016-10-15"}
eg2 = { "desc":"bbbbdesc"}
LIST_GET_EVENTS = [eg1, eg2]


def do_all_tests():

    try:

        # for evx in LIST_ADD_EVENTS:

            # MockAddEvent(evx["title"], evx["datee"], evx["desc"])
            # MockDeleteEvent(evx["title"], evx["datee"], evx["desc"])

        for evx in LIST_GET_EVENTS:

            sd = ed = desc1 = ""
            if "start_date" in evx:
                sd = evx["start_date"]
            if "end_date" in evx:
                ed = evx["end_date"]
            if "desc" in evx:
                desc1 = evx["desc"]

            MockGetEvents(sd, ed, desc1)

            # list_events = MockGetEventsByTitle(title="title1")"
            # list_events = MockGetEventsByDates(start_date="20160101", end_date="20160215")
            # list_events = MockGetEventsByDatesAndTitle(start_date, end_date, title)
            # new_event = MockUpdateEvent(event_date="20160831")
            # del_event = MockDeleteEvent(event_date, event_title)

        print "tests events system ended"

    except Exception as e:
        print "error in MockTestEvents"
        raise e

def MockGetEvents(start_date, end_date, desc):
     
    sqlx, sqlx_count = DBAccess.bld_query_sql(start_date, end_date, desc)
    
    list_result = DBAccess.get_events(sqlx, sqlx_count)
    if list_result[0] == 'error':
        sj = {"events_error": list_result[1]}
    else:
        sj = {"events_details": list_result[1]}
    print "MockGetEvent ended"
    print sj


def MockDeleteEvent(title1, date1, desc1):
     
    sqlx = DBAccess.bld_delete_sql(title1, date1, desc1)

    list_result = DBAccess.delete_event(sqlx)
    if list_result[0] == 'error':
        print "MockDeleteEvent: error - {}".format(list_result[1])
    else:
        print "MockDeleteEvent: success - {}".format(list_result[1])
    return list_result[0]
    


def MockAddEvent(title1, datee, desc1):
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
