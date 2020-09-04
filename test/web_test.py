from flask import Flask, request
import json

app = Flask(__name__)


@app.route("/")
def welcome():
    print request.headers
    print request.url
    return json.dumps({'name': 'tt'})


if __name__ == "__main__":
    app.run()
