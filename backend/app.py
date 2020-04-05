#!flask/bin/python
# -*- coding: utf-8 -*-


from flask import Flask, jsonify, json, send_from_directory, url_for
from flask import request, Response, render_template
from flask import abort, make_response
from flask_httpauth import HTTPBasicAuth
from flask_cors import CORS

import psycopg2 as pg
import psycopg2.extras as pgext
import db_utils as ut
import os, sys
import datetime
import fake_news
import news_recommendation

auth = HTTPBasicAuth()
app = Flask(__name__)
app.debug = True
app.config['JSON_AS_ASCII'] = False
CORS(app)

config = json.load(open("config"))

#connect to postgres using psycopg2
db = config["postgresdb"]
conn_string = "dbname='{}' user='{}' password='{}' host='{}' port={}".format(db["database"],
                                                                             db["username"],
                                                                             db["password"],
                                                                             db["server"],
                                                                             db["port"]
                                                                            )


fn = fake_news.FakeNewsDetection(config["data"]["dataset"], config["data"]["model"])
fn.initialize()
rn = news_recommendation.NewsRecommendation(config["data"]["debunking_dataset"])
rn.pre_process()

@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)

@app.errorhandler(404)
def not_found():
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.route('/sams/api')
def main():
    return jsonify("Use the 'detect' or 'recommend' route and provide a text message via POST method")

@app.route('/')
def root():
    return jsonify("this is the API for hackathon SAMS project")


@app.route('/sams/api/detect_only', methods=["POST"])
def detect():
    req = json.loads(request.data.decode("utf-8"))
    if not req:
        res = jsonify({"error": "post message is not a valid json"})
        res.headers.add('Access-Control-Allow-Origin', '*')
        print(res, file=sys.stderr)
        return res
    print(str(req["text"]), file=sys.stderr)
    prediction = fn.predict([str(req["text"])])
    print(prediction, file=sys.stderr)
    label = "False" if prediction["prediction"] == "False" else "Real"
    prob = round(prediction["probability"], 2)
    res = jsonify({"OK": {"class": label, "probability": prob}})
    res.headers.add('Access-Control-Allow-Origin', '*')
    print(res, file=sys.stderr)
    return res

@app.route('/sams/api/recommend', methods=["POST"])
def recommend():
    req = json.loads(request.data.decode("utf-8"))
    if not req:
        res = jsonify({"error": "post message is not a valid json"})
        res.headers.add('Access-Control-Allow-Origin', '*')
        print(res, file=sys.stderr)
        return res
    text = str(req["text"])
    print(text, file=sys.stderr)
    result = rn.recommend(text)
    print(result, file=sys.stderr)
    threshold = 0.75
    if result["probability"] < threshold:
        res = jsonify({"OK": {"false": "Sorry, I did not find any recommendation from our database."}})
    else:
        res = jsonify({"OK": result})
    res.headers.add('Access-Control-Allow-Origin', '*')
    print(res, file=sys.stderr)
    return res

@app.route('/sams/api/detect', methods=["POST"])
def check_news():
    conn = pg.connect(conn_string)
    cur = conn.cursor(cursor_factory=pg.extras.RealDictCursor)
    req = json.loads(request.data.decode("utf-8"))

    if not req:
        res = jsonify({"error": "post message is not a valid json"})
        res.headers.add('Access-Control-Allow-Origin', '*')
        print(res, file=sys.stderr)
        return res

    # user_id, email_address, created_date, subject, description, status, source, process_status,
    date_now = str(datetime.datetime.now())
    req["dt"] = date_now

    insert_statement = "insert into queries "
    id, message = ut.insert_dict(conn, cur, insert_statement, req)
    if id:
        #res = jsonify({"OK": "News has been registered! \n Check the status on the NEWS section"})
        prediction = fn.predict([str(req["text"])])
        print(prediction, file=sys.stderr)
        fake = "False" if prediction["prediction"] == "False" else "Real"
        prob = round(prediction["probability"], 2)
        ut.update(conn, cur, "update queries set class='{0}', probability={2} where id={1}".format(fake, id, prob))
        res = jsonify({"OK": {"class": fake, "probability": prob}})
    else:
        res = jsonify({"error": message})
    conn.close()
    res.headers.add('Access-Control-Allow-Origin', '*')
    print(res, file=sys.stderr)
    return res

@app.route('/sams/api/get_news', methods=["GET"])
def get_tickets():
    conn = pg.connect(conn_string)
    cur = conn.cursor(cursor_factory=pg.extras.RealDictCursor)
    statement = """select * from queries where class !='';"""
    cur.execute(statement)
    res = cur.fetchall()
    conn.close()
    res = jsonify({"queries": res})
    res.headers.add('Access-Control-Allow-Origin', '*')
    return res

if __name__ == '__main__':
    app.run(threaded=True, debug=True, host='0.0.0.0', port=5310)


