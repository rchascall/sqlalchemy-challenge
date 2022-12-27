#--------------#
# Dependencies #
#--------------#

import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#----------------#
# Database Setup #
#----------------#
#engine = create_engine("sqlite:///hawaii.sqlite")
engine = create_engine("sqlite:///sqlalchemy-challenge/SurfsUp/Resources/hawaii.sqlite")


# Reflect an existing database into a new model
Base = automap_base()

# Reflect the tables
Base.prepare(autoload_with=engine)

# View all of the classes that automap found
Base.classes.keys()

# Save reference to both tables
Measurement = Base.classes.measurement
Station = Base.classes.station

#-------------#
# Flask setup #
#-------------#
app = Flask(__name__)

#--------------#
# Flask Routes #
#--------------#

@app.route("/")
def home():
    return (
        f"Welcome to the Climate App!<br/>"
        f"Available endpoints:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():

    return "Welcome to the Precipitation Page"

@app.route("/api/v1.0/stations")
def stations():
    # Create session (link) from Python to the database
    session = Session(engine)

    ## return "Welcome to the Stations Page"

    # Query all stations
    results = session.query(Station.name).all()

    session.close()

    # Convert list of tuples into a normal list
    all_stations = list(np.ravel(results))

    return jsonify(all_stations)

@app.route("/api/v1.0/tobs")
def tobs():
    return "Welcome to the Temperature Observations Page"

# Main behavior
if __name__ == "__main__":
    app.run(debug=True)