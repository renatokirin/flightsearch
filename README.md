# FlightSearch
FlightSearch is a conceptual flight search application, used to add, edit, delete and filter flights.
![alt text](https://raw.githubusercontent.com/renatokirin/flightsearch/main/screenshot.png)

## Features
* Add a new flight
* Edit an existing flight
* Delete an existing flight
* Filter flights by origin, destination, day and month

## Running the backend

*This app requires docker to run*

#### Creating a docker image
```sh
cd Backend
docker build -t flightsearch .
```

#### Running the docker image
```sh
docker run -p 8080:8080 flightsearch
```

## Running the frontend
Navigate to the frontend folder and run *index.html* with a web browser.
