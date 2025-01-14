#!usr/bin/python3

from api.v1.views import app_views

@app_views.route("/status", strict_slashes=False, methods=["GET"])
def status():
    '''route that returns the status of the API, a JSON 
    '''
    return {
        "status": "OK",
    }
