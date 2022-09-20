# Thomas Wong, tsw8626
from datetime import datetime
import pytz
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello world!'

# Adding code for the new "/time" path here. When the server is running, visiting
# "127.0.0.1:8000/time" returns the current time (NY time zone)
@app.route("/time")
def get_time():
    nyTimeZone = pytz.timezone("America/New_York")
    return datetime.now(nyTimeZone).strftime("%H:%M:%S")

app.run(host='0.0.0.0',
        port=8080,
        debug=True)
