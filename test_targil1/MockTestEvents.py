"""
Test the Targil1 database access
and other features of the system
"""
import DBAccess

# can convert later to config file
ev1 = {"title": "team1 meeting", "datee": "2016-07-11", "desc":"meeting for cake"}
ev2 = {"title": "team2 meeting", "datee": "2016-07-17", "desc":"meeting for falafel"}
LIST_ADD_EVENTS = [ev1]


def do_all_tests():

    for evx in LIST_ADD_EVENTS:

        # MockAddEvent(evx["title"], evx["datee"], evx["desc"])
        MockDeleteEvent(evx["title"], evx["datee"], evx["desc"])

    # list_events = MockGetEventsByTitle(title="title1")"
    # list_events = MockGetEventsByDates(start_date="20160101", end_date="20160215")
    # list_events = MockGetEventsByDatesAndTitle(start_date, end_date, title)
    # new_event = MockUpdateEvent(event_date="20160831")
    # del_event = MockDeleteEvent(event_date, event_title)

    print "tests events system ended"


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
