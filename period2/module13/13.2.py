import json
import mariadb
from flask import Flask, Response

connection = mariadb.connect(
        user="root",
        password="123456",
        # host defines the computer the connection is made to.
        # When the server runs on the same computer where the Python program is run,
        # the address is 127.0.0.1 or alternatively localhost.
        host="localhost",
        # port determines the port number the server is listening to.
        # The default port number of MariaDB is 3306.
        port=3306,
        # database is the name of the database that we want to connect ot get data
        database="flight_game",
        autocommit = True
    )

app = Flask(__name__)
@app.route('/airport/<code>')
def get_airport_info_from_code(code):
    try:
        sql = "SELECT name, municipality FROM airport"
        sql += " WHERE airport.ident = '" + code + "'"
        cursor = connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchone()
        if cursor.rowcount > 0:
            name = result[0]
            location = result[1]
            response = {
                "ICAO": code,
                "Name": name,
                "Location": location,
            }
        else:
            response = {}

        return response
    except ValueError:
        print(ValueError)
        response = {
            "message": "Invalid number as addend",
            "status": 400
        }
        json_response = json.dumps(response)
        http_response = Response(response=json_response, status=400, mimetype="application/json")
        return http_response

@app.errorhandler(404)
def page_not_found(error_code):
    response = {
        "message": "Invalid endpoint",
        "status": 404
    }
    json_response = json.dumps(response)
    http_response = Response(response=json_response, status=404, mimetype="application/json")
    return http_response

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000, debug=True)