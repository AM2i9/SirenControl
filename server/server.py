from flask import Flask
import threading
from sirens.steady import steady
from sirens.yelp import yelp

siren_yelp = None
siren_steady = None
stop = False

app = Flask(__name__)

@app.route("/yelp")
def yelpRequest():
    global siren_yelp, siren_steady, stop
    off()
    stop=False
    siren_yelp = threading.Thread(target=yelp,args=(lambda : stop,))
    siren_yelp.start()
    return "yelp"

@app.route("/steady")
def steadyRequest():
    global siren_yelp, siren_steady, stop
    off()
    stop=False
    siren_steady = threading.Thread(target=steady,args=(lambda : stop,))
    siren_steady.start()
    return "steady"

@app.route("/off")
def off():
    global siren_yelp, siren_steady, stop
    stop = True
    if siren_steady:
        siren_steady.join()
        siren_steady = None
    if siren_yelp:
        siren_yelp.join()
        siren_yelp = None

    return "off"

if __name__ == "__main__":
    app.run(debug=True,port=90,host='0.0.0.0')