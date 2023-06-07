from pony.orm.serialization import to_dict
from pony import orm
DB = orm.Database()


class Flight(DB.Entity):
    id = orm.PrimaryKey(int, auto=True)
    airline = orm.Required(str)
    origin = orm.Required(str)
    destination = orm.Required(str)
    departure_date = orm.Required(str)
    departure_time = orm.Required(str)
    arrival_time = orm.Required(str)
    price = orm.Required(float)


DB.bind(provider="sqlite", filename="database.sqlite", create_db=True)
DB.generate_mapping(create_tables=True)



def add_flight(airline, origin, destination, departure_date, departure_time, arrival_time, price):
    try:
        with orm.db_session:
            day, month = departure_date.split()
            if int(day) > 31 or int(month) > 12:
                return {"response": "Fail"}

            Flight(airline=airline,
                   origin=origin,
                   destination=destination,
                   departure_date=departure_date,
                   departure_time=departure_time,
                   arrival_time=arrival_time,
                   price=price)
            return {"response": "Success"}
    except Exception as e:
        raise Exception(
            "An error occurred while adding a flight: {}".format(str(e)))



def edit_flight(flight_id, airline, origin, destination, departure_date, departure_time, arrival_time, price):
    try:
        with orm.db_session:
            print('EDITED: ', flight_id, airline, origin, destination, departure_date, departure_time, arrival_time, price)
            flight = Flight.get(id=flight_id)
            if not flight:
                return {"response": "Fail"}
            setattr(flight, 'airline', airline)
            setattr(flight, 'origin', origin)
            setattr(flight, 'destination', destination)
            setattr(flight, 'departure_date', departure_date)
            setattr(flight, 'departure_time', departure_time)
            setattr(flight, 'arrival_time', arrival_time)
            setattr(flight, 'price', price)
            orm.commit()
            return {"response": "Success"}
    except Exception as e:
        raise Exception(
            "An error occurred while editing a flight: {}".format(str(e)))



def remove_flight(flight_id):
    try:
        with orm.db_session:
            flight = Flight.select(id=flight_id)
            if not flight:
                return {"response": "Fail"}
            flight.delete()

            return {"response": "Success"}
    except Exception as e:
        raise Exception(
            "An error occurred while removing a flight: {}".format(str(e)))


def get_flights(origin=None, destination=None, departure_date=None):
    try:
        with orm.db_session:
            flights = Flight.select()

            if origin:
                flights = flights.filter(origin=origin)
            if destination:
                flights = flights.filter(destination=destination)
            if departure_date:
                flights = flights.filter(departure_date=departure_date)

            flights_list = [f.to_dict() for f in flights]
            return flights_list
    except Exception as e:
        raise Exception(
            "An error occurred while retrieving flights: {}".format(str(e)))



