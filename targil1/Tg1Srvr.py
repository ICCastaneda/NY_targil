"""
Targil1 Flask server, support various options
to access the targil1 database
"""
# import os
import json
from flask import Flask, request
# from flask.helprs import jsonify, send_file
from flask import jsonify, send_file
import CONS
import DBAccess

tf_port = int(CONS.PORT)
app = Flask(__name__, static_folder='www', template_folder='www')


@app.route('/')
def main_index_html():
    """
    On start of the web page send the index.html page
    which will later will be manipulate by the client side
    """
    # req = request     # debug only
    return send_file("www/templates/index.html")



@app.route('/add_event', methods=["GET"]) 
def add_event():
    """
    Add event function
    """
    data_json = json.loads(request.args.get('add_data'))
    title, date1, desc = get_events_values(data_json)
    sqlx = DBAccess.bld_add_sql(title, date1, desc)

    list_result = DBAccess.add_event(sqlx)
    if list_result[0] == 'error':
        sj = jsonify({"add_event_error": list_result[1]})
    else:
        sj = jsonify({"add_event successeded": list_result[1]})
    return sj


@app.route('/delete_event', methods=["GET"])    # "POST"
def delete_event():
    """
    Delete event function
    """
    data_json = json.loads(request.args.get('delete_data'))
    id1, title, date1, desc = get_events_values(data_json, idp='yes')
    sqlx = DBAccess.bld_delete_sql(id1, title1, date1, desc1)

    list_result = DBAccess.delete_event(sqlx)
    if list_result[0] == 'error':
        sj = jsonify({"delete_event_error": list_result[1]})
    else:
        sj = jsonify({"delete_event successeded": list_result[1]})
    return sj


@app.route('/update_event', methods=["GET"])
def update_event():
    """
    Update event function
    """
    data_json = json.loads(request.args.get('update_data'))
    id1, title, date1, desc = get_events_values(data_json, idp='yes')
    sqlx = DBAccess.bld_update_sql(id1, title1, date1, desc1)

    list_result = DBAccess.update_event(sqlx)
    if list_result[0] == 'error':
        sj = jsonify({"update_event_error": list_result[1]})
    else:
        sj = jsonify({"update_event successeded": list_result[1]})
    return sj


@app.route('/get_events', methods=["GET"])
def get_events():
    """
    Get events function, either by dates and or description
    """
    req = request
    start_date = request.args.get("start_date")
    end_date = request.args.get("end_date")
    desc = request.args.get("event_desc")
    sqlx, sqlx_count = DBAccess.bld_query_sql(start_date, end_date, desc)
    
    list_result = DBAccess.get_events(sqlx, sqlx_count)
    if list_result[0] == 'error':
        sj = jsonify({"events_error": list_result[1]})
    else:
        sj = jsonify({"events_details": list_result[1]})
    return sj


def get_events_values(data_json, idp='no'):
    id1 = title = date1 = desc = ""
    rl = []
    if idp == 'yes':          # check for id if in json
        if "id" in data_json:
           id1 = data_json["id"]
    if "event_title" in data_json:
        title = data_json['event_title']
    if "event_date" in data_json:
        date1 = data_json['event_date']
    if "event_desc" in data_json:
        desc = data_json['event_desc']
    if idp == 'yes':
        rl.append(id1)
    rl += [title, date1, desc]
    return rl


if __name__ == '__main__':
    """
    targil1 flask server, main
    """
    ms1 = "port number is {}".format(tf_port)
    print ms1    # will be converter to use python logging

    app.run(host="0.0.0.0",
            threaded=True,
            debug=True,
            use_reloader=False,
            use_debugger=False,
            port=tf_port)
