from db_connector import add_flight, get_flights, remove_flight, edit_flight
from flask import Flask, jsonify, make_response, request
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*", "methods": ["GET", "POST", "PATCH", "DELETE"]}})


@app.route("/flights", methods=["GET"])
def route_get_flights():
    try:
        origin = request.args.get('origin')
        destination = request.args.get('destination')

        departure_date = request.args.get('departure_date')
        if departure_date:
            departure_date = departure_date.replace('_', ' ')

        response = get_flights(origin, destination,
                               departure_date)
        return make_response(jsonify(response), 200)
    except Exception as e:
        print(e)
        return make_response(jsonify({'response': 'Fail'}), 500)


@app.route("/flights", methods=["POST"])
def route_add_flight():
    try:
        add_flight(
            request.json['airline'],
            request.json['origin'],
            request.json['destination'],
            request.json['departure_date'],
            request.json['departure_time'],
            request.json['arrival_time'],
            request.json['price']
        )
        response = {"response": "Success"}
        return make_response(jsonify(response), 201)

    except Exception as e:
        print(e)
        return make_response(jsonify({'response': 'Fail'}), 500)
    

@app.route("/flights", methods=["PATCH"])
def route_edit_flight():
    try:
        edit_flight(
            request.json['flight_id'],
            request.json['airline'],
            request.json['origin'],
            request.json['destination'],
            request.json['departure_date'],
            request.json['departure_time'],
            request.json['arrival_time'],
            request.json['price']
        )
        response = {"response": "Success"}
        return make_response(jsonify(response), 201)

    except Exception as e:
        print(e)
        return make_response(jsonify({'response': 'Fail'}), 500)


@app.route("/flights", methods=["DELETE"])
def route_remove_flight():
    try:
        status = remove_flight(request.json['flight_id'])
        if status['response'] == "Success":
            return make_response(jsonify({"response": "Success"}), 201)
        return make_response(jsonify({"response": "Fail"}), 401)
 
    except Exception as e:
        print(e)
        return make_response(jsonify({'response': 'Fail'}), 500)



if __name__ == "__main__":
    app.run(port=8080, host='0.0.0.0', debug=True)
