"""
    targil1 MariaDB interface functions
"""
# import mysql.connector as mariadb     # mysqldb   # MySQLdb
# import mysqldb
import mysql.connector
import datetime
import CONS


def bld_query_sql(start_date, end_date, desc):
    """
    build the sql for query of events either by dates
    and or description
    """
    str_where = ""        # ("
    cnt = 0
    if start_date and end_date:
        str_where += "event_date >= '{}' and event_date <= '{}'".\
            format(start_date, end_date)
        cnt += 1
    elif start_date and not end_date:
        str_where += "event_date = '{}'".format(start_date)
        cnt += 1
    elif end_date:
        str_where += "event_date = '{}'".format(end_date)
        cnt += 1

    if desc:
        if cnt:
            str_where += " and "
        str_where += " event_desc = '{}'".format(desc)
        cnt += 1
 
    # if cnt:
    #    str_where += ")"

    sqlx_count = "select count(*) from {} where ({})".format(CONS.EVENTS_TABLE, str_where)
    sqlx = "select * from {} where ({}) order by {}".\
                 format(CONS.EVENTS_TABLE, str_where, CONS.DATE_COLUMN)
    return [sqlx, sqlx_count]


def bld_add_sql(title1, date1, desc1):
    """
    build the add event sql
    """
    insert_str = "insert into tg1_events (event_title, event_date, event_desc) \
        values('{}', '{}', '{}');".format(title1, date1, desc1)

    return insert_str


def add_event(sqlx):
    """
    process the add event
    """
    ap = db_create_connection()
    ap.sqlx = sqlx
    ap.op = 'insert'
    rmsg = ""
    try:
        db_exec_cur(ap)

    except Exception as e:
        rmsg =  ["error", "error adding event"]

    if not rmsg:
        rmsg = ["success", "event added succesfully"]
        db_commit(ap)

    db_close_con(ap)
    return rmsg


def bld_delete_sql(id, title1, date1, desc1):
    """
    build the delete event sql 
    """
    str_where = ""
    cnt = 0
    if id:
        str_where = " id = {}".format(str(id))
        cnt += 1
    else:
        if title1:
            str_where += "event_title = '{}'".format(title1)
            cnt += 1
        if date1:
            if cnt:
                str_where += " and "
            str_where += "event_date = '{}'".format(date1)
            cnt += 1
        if desc1:
            if cnt:
                str_where += " and "
            str_where += "event_desc = '{}'".format(desc1)
            cnt += 1

    if cnt:
        delete_str = "delete from tg1_events where ({});".format(str_where)
    else:
        delete_str = ""    # nothing to delete

    return delete_str


def delete_event(sqlx):
    """
    process the delete event
    """
    ap = db_create_connection()
    ap.sqlx = sqlx
    ap.op = 'delete'
    rmsg = ""
    try:
        db_exec_cur(ap)

    except Exception as e:
        rmsg =  ["error", "error deleting event"]

    if not rmsg:
        rmsg = ["success", "event deleted successfully"]
        db_commit(ap)

    db_close_con(ap)
    return rmsg


def save_new_diary():
    """
    process the save of new diary after the DB changed
    """
    ap = db_create_connection()
    sqlx = "SELECT * FROM {} INTO OUTFILE '{}'".format(CONS.EVENTS_TABLE, CONS.DIARY_FILE);
    ap.sqlx = sqlx
    ap.op = 'save_diary'
    rmsg = ""
    try:
        db_exec_cur(ap)

    except Exception as e:
        e2 = "error saving the diary " + str(e)
        # e1 = repr(e)
        # e3 = e.msg
        rmsg = ["error",  e2]

    if not rmsg:
        rmsg = ["success", "the diary was saved succesfully"]
        db_commit(ap)

    db_close_con(ap)
    return rmsg


def bld_update_sql(id1, title1, date1, desc1):
    """
    build the update event sql 
    """
    str_where = ""
    str_set = ""
    cnt = 0
    if id:
        str_where = " id = {}".format(str(id1))
        if title1:
            str_set += "event_title = '{}'".format(title1)
            cnt += 1
        if date1:
            if cnt:
                str_set += ", "
            str_set += "event_date = '{}'".format(date1)
            cnt += 1
        if desc1:
            if cnt:
                str_set += ", "
            str_set += "event_desc = '{}'".format(desc1)
            cnt += 1

        

    if cnt:
        update_str = "update tg1_events set {} where ({});".format(str_set, str_where)
    else:
        update_str = ""    # nothing to delete

    return update_str


def update_event(sqlx):
    """
    process the update event
    """
    ap = db_create_connection()
    ap.sqlx = sqlx
    ap.op = 'update'
    rmsg = ""
    try:
        db_exec_cur(ap)

    except Exception as e:
        rmsg =  ["error", "error updating event"]

    if not rmsg:
        rmsg = ["success", "event updating successfully"]
        db_commit(ap)

    db_close_con(ap)
    return rmsg


def get_events(sqlx, sqlx_count):
    """
    process the query of get events
    """
    ap = db_create_connection()
    ap.sqlx = sqlx_count
    ap.op = 'count'
    try:
        obj_count = {"count": -1}
        ap = db_exec_cur(ap)
        for t in ap.result:
            obj_count["count"] = t[0]

        ap.sqlx = sqlx
        ap.op = 'get_data'
        db_exec_cur(ap)
    except Exception as e:
        raise "error reading the database"

    rslt_list = convert_tuple(ap, obj_count)
    db_close_con(ap)
    return rslt_list


def convert_tuple(ap, obj_count):
    """
    convert the the result of the sql which is
    in tuple to jsons
    """
    a_result = [obj_count]
    for t in ap.result:
        cnt1 = -1
        uj = {}
        
        for fld1 in ap.desc:
            cnt1 += 1
            uj[fld1] = t[cnt1]
        a_result.append(uj)

    return ['ok', a_result]
    

def db_create_connection():
    """
   create the connection to Maria
   """
    ap = DBParms()

    ap.con = mysql.connector.connect(user=CONS.USER, password=CONS.PW,
                                     database=CONS.DB_NAME, host=CONS.HOST)
    ap.cur = ap.con.cursor()
    return ap


def db_commit(ap):
    """
   commit changes to database 
   """
    ap.con.commit()


def db_close_con(ap):
    """
    close the connection to the database
    """
    ap.con.close()


def db_exec_cur(ap):
    """
   execute the sql
   """
    ap.cur.execute(ap.sqlx)
    if ap.op == 'get_data' or ap.op == 'count':
        ap.result = ap.cur.fetchall()
        if ap.op == 'get_data':
            ap.desc = [x[0] for x in ap.cur.description]
    
    return ap


class DBParms(object):
    """
    Class which holds the parameters 
    to access the database 
    """
    con = None
    cur = None
    result = None
    desc = None
    sqlx = None
    op = None

