rem run curl to test the web system
curl '127.0.0.1:5000/add_event?add_data={"event_title":"adesc", "event_date":"2091-01-01", "event_desc":"zzzzzzzzzzxxxxxxthisdesc"}'
curl '127.0.0.1:5000/get_events?start_date=2016-01-01&end_date=2016-12-31'
