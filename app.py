# Importing Flask
from flask import Flask, redirect, jsonify

#Importing dependencies
import numpy as np
import datetime as dt
import json

#Importing SQL
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

#####Database Setup#####
engine = create_engine("sqlite:///hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)

###Reference the tables###
Measurement = Base.classes.measurement
Station = Base.classes.station

###Create Session###
session = Session(engine)
###Flask Setup###
app = Flask(__name__)
###Begin routes with Flask###
@app.route("/")
def home():
    return "Welcome to the SQlalchemy Challenge: Surf's Up API"

###List all the routes
@app.route("/welcome")
def welcome():
    return (
        f"Welcome to the SQLalchemy Challenge: Surf's Up API<br>"
        f"List of Routes:<br/>"
        f"/api/v1.0/precipation,<br/>"
        f"/api/v1.0/stations,<br/>"
        f"/api/v1.0/tobs,<br/>"
        f"/api/v1.0/YYYY-MM-DD,<br/>"
        f"/api/v1.0/YYYY-MM-DD to YYYY-MM-DD<br/>"
    )
###Route recipitation
@app.route("/api/v1.0/precipitation")
def precipitation():
    results = session.query(Measurement).all()
    session.close()
    #Create dict using date as key and prcp as value
    year_prcp = []
    for result in results:
        year_prcp_dict = {}
        year_prcp_dict["date"] = result.date
        year_prcp_dict["prcp"] = result.prcp
        year_prcp.append(year_prcp_dict)
    #JSON representation of dict
    return jsonify(year_prcp)

###Route stations
@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)
    results = session.query(Station.station).all()
    session.close()
    all_stations = list(np.ravel(results))
    #JSON summary of list
    return jsonify(all_stations)

###Route tobs
@app.route("/api/v1.0/tobs")
def temperature():
    session = Session(engine)
    #Database ended 2017-08-23, 12-months is 2016-08-23
    results = session.query(Measurement.date, Measurement.tobs).\
            filter(Measurement.date>="2016-08-23").\
            filter(Measurement.date<="2017-08-23").all()

    session.close()

    temperature_dict = list(np.ravel(results))
    #JSON summary of dict
    return jsonify(temperature_dict)
###Start Route

###Start and End Route
if __name__ == "__main__":
    app.run(debug=True)  

