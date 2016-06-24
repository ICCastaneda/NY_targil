"""
Test the Targil1 database access
and other features of the system
"""
# import os
# import json
# from flask.helprs import jsonify, send_file
import sys
import subprocess
import traceback      #   os.path, time
import DBAccess
import Tg1Srvr

FLAG_DO_ADD = True        # flags to control the test process
FLAG_DO_DELETE = True     # will be change to be part of the config file
FLAG_DO_UPDATE = True
FLAG_DO_GET_EVENTS = True

# will be converter to use python argparse and ConfigParser
ev1 = {"event_title": "team1 meeting", "event_date": "2016-07-11", "event_desc":"meeting for falafel1"}
ev2 = {"event_title": "team2 meeting", "event_date": "2016-07-12", "event_desc":"meeting for cake"}
ev3 = {"event_title": "team3 meeting", "event_date": "2016-07-13", "event_desc":"meeting for movie"}
ev4 = {"event_title": "team4 meeting", "event_date": "2016-07-14", "event_desc":"meeting hanging out"}
ev5 = {"event_title": "team5 meeting", "event_date": "2016-07-15", "event_desc":"running to the sea"}
ev6 = {"event_title": "team6 meeting", "event_date": "2016-07-16", "event_desc":"learning python"}
ev7 = {"event_title": "team7 meeting", "event_date": "2016-07-17", "event_desc":"debate emacs or vim"}
ev8 = {"event_title": "team8 meeting", "event_date": "2016-07-18", "event_desc":"discussing falsk vs Django"}
LIST_ADD_EVENTS = [ev1, ev2, ev3, ev4, ev5, ev6, ev7, ev8]
evd3 = {"id": "119",}
LIST_DELETE_EVENTS = [ev1, ev5, evd3]

eg1 = {"start_date": "2016-10-11", "end_date": "2016-10-17"}
eg2 = { "event_desc":"meeting for movie"}
LIST_GET_EVENTS = [eg1, eg2]

eu1 = {"id": "18", "event_date": "2077-01-01"}
eu2 = {"id": "19", "event_title": "THE START OF TIME", "event_date": "2098-12-31", "event_desc": "A NEW WORLD RISE"}
eu3 = {"id": "20", "event_title": "ONCE IN ISRAEL", "event_desc": "THERE WAS A GOOD WITCH"}
LIST_UPDATE_EVENTS = [eu1, eu2, eu3]


def do_all_tests():
    """
    main test process, 
    code that i think should be added: ArgParse to pass the config file to the program
    and ConfigParser to get the parms to test from a config external file
    instead being build in the program.
    """
    try:

        _MockDoCurlCmds()    # not implmented yet

        _mock_save_diary()     # save the diary for tests

        if FLAG_DO_ADD:
            for evx in LIST_ADD_EVENTS:
                _MockAddEvent(evx)
                _MockCheckAddEvent(evx)      # the check functions haven't been implmented yet

        if FLAG_DO_UPDATE:
            for evx in LIST_UPDATE_EVENTS:
                _MockUpdateEvents(evx)
                _MockCheckUpdateEvents(evx)

        if FLAG_DO_DELETE:
           
            for evx in LIST_DELETE_EVENTS:
                evx = _MockGetIdToDelete(evx)
                _MockDeleteEvent(evx)
                _MockCheckDeleteEvent(evx)

        if FLAG_DO_GET_EVENTS:
            for evx in LIST_GET_EVENTS:

                sd = ed = desc1 = ""
                if "start_date" in evx:
                    sd = evx["start_date"]
                if "end_date" in evx:
                    ed = evx["end_date"]
                if "event_desc" in evx:
                    desc1 = evx["event_desc"]

                _MockGetEvents(sd, ed, desc1)

        print "tests events system ended"

    except Exception as e:
        print "error in MockTestEvents"
        print "error:", str(e)
        print "------------"
        traceback.print_exc(file=sys.stderr)
        raise e


def _mock_save_diary():
    """
    test saving the diary
    """
    rmsg = DBAccess.save_new_diary()
    print 'mock_save_diary: ended: ' , rmsg


def _MockGetEvents(start_date, end_date, desc):
    """
    test the web url "/get_events" 
    """
    sqlx, sqlx_count = DBAccess.bld_query_sql(start_date, end_date, desc)
    
    list_result = DBAccess.get_events(sqlx, sqlx_count)
    if list_result[0] == 'error':
        sj = {"events_error": list_result[1]}
    else:
        sj = {"events_details": list_result[1]}
    print sj
    print "MockGetEvent ended"


def _MockGetIdToDelete(evx):
    """
       read the database to get d to delete into the evx
       dict, not implmented yet
    """
    return evx


def _MockCheckUpdateEvents(data_json):
    """
    Check the update results, not implmented yet
    """
    return 'ok'
    


def _MockUpdateEvents(data_json):
    """
    test the web url "/update_event" 
    """
    id1, title1, date1, desc1 = Tg1Srvr.get_events_values(data_json, idp='yes')
    sqlx = DBAccess.bld_update_sql(id1, title1, date1, desc1)

    list_result = DBAccess.update_event(sqlx)
    if list_result[0] == 'error':
        sj = {"update_event_error": list_result[1]}
    else:
        sj = {"update_event succeded": list_result[1]}
    print sj
    print "mock_update_event ended"


def _MockCheckDeleteEvent(data_json):
    """
    Check the delete results, not implmented yet
    """
    return 'ok'
    

def _MockDeleteEvent(data_json):
    """
    test the web url "/delete_event" 
    """
     
    id1, title1, date1, desc1 = Tg1Srvr.get_events_values(data_json, idp='yes')
    sqlx = DBAccess.bld_delete_sql(id1, title1, date1, desc1)

    list_result = DBAccess.delete_event(sqlx)
    if list_result[0] == 'error':
        print "MockDeleteEvent: error - {}".format(list_result[1])
    else:
        print "MockDeleteEvent: succeded - {}".format(list_result[1])
    return list_result[0]
    

def _MockCheckAddEvent(data_json):
    """
    check the add event, not implmented yet
    """
    return 'ok'


def _MockAddEvent(data_json):
    """
    test the web url "/add_event" 
    """
    title1, date1, desc1 = Tg1Srvr.get_events_values(data_json)
    sqlx = DBAccess.bld_add_sql(title1, date1, desc1)

    list_result = DBAccess.add_event(sqlx)
    if list_result[0] == 'error':
        print "MockAddEvent: error - {}".format(list_result[1])
    else:
        print "MockAddEvent: success - {}".format(list_result[1])
    return list_result[0]
    

def _MockDoCurlCmds():
    """
    not implmented yet
    """
    return 'ok'


if __name__ == '__main__':
    print 'In MockTestEvents - main'
    do_all_tests()
