from flask import Flask
app = Flask(__name__)
import logging

@app.route("/")
def hello():
    app.logger.info('Main Request Successful')
    return "Hello World!"

@app.route("/status")
def status():
    app.logger.info('Status Request Successful')
    return {
        "status": 200,
        "result": 'Ok - healthy'
    }

@app.route("/metrics")
def metrics():
    app.logger.info('Metrics Request Successful')
    return {
        "status": 200,
        "data": {
            "UserCount": 200,
            "UserCountActive": 25
        }
    }




if __name__ == "__main__":
    logging.basicConfig(filename='app.log', level=logging.DEBUG)
    app.run(host='0.0.0.0')
