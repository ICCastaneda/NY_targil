import os
import json
from flask import Flask, request
# from flask.helprs import jsonify, send_file
from flask import jsonify, send_file
import CONS
# import ms
import DBAccess

tf_port = int(CONS.PORT)
app = Flask(__name__, static_folder='www', template_folder='www')


@app.route('/')
def main_index_html():
    req = request     # debug only
    args = req.args   # debug only
    return send_file("www/templates/index.html")


@app.route('/add_event', methods=["GET"])   # "POST"
def add_event():
    title = request.args.get('title')
    date1 = request.args.get('date')
    desc = request.args.get('desc')
    sqlx = DBAccess.bld_add_sql(title, date1, desc)

    list_result = DBAccess.add_event(sqlx)
    if list_result[0] == 'error':
        sj = jsonify({"add_event_error": list_result[1]})
    else:
        sj = jsonify({"add_event successeded": list_result[1]})
    return sj


@app.route('/delete_event', methods=["GET"])    # "POST"
def delete_event():
    title1 = request.args.get('title')
    date1 = request.args.get('date')
    desc1 = request.args.get('desc')
    sqlx = DBAccess.bld_delete_sql(title1, date1, desc1)

    list_result = DBAccess.delete_event(sqlx)
    if list_result[0] == 'error':
        sj = jsonify({"delete_event_error": list_result[1]})
    else:
        sj = jsonify({"delete_event successeded": list_result[1]})
    return sj


@app.route('/get_events', methods=["GET"])
def get_events():
    req = request
    start_date = request.args.get("start_date")
    end_date = request.args.get("end_date")
    desc = request.args.get("desc")
    sqlx, sqlx_count = DBAccess.bld_query_sql(start_date, end_date, desc)
    
    list_result = DBAccess.get_events(sqlx, sqlx_count)
    if list_result[0] == 'error':
        sj = jsonify({"events_error": list_result[1]})
    else:
        sj = jsonify({"events_details": list_result[1]})
    return sj




if __name__ == '__main__':
    ms1 = "port number is {}".format(tf_port)
    print ms1

    app.run(host="0.0.0.0",
            threaded=True,
            debug=True,
            use_reloader=False,
            use_debugger=False,
            port=tf_port)
