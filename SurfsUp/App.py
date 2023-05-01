# Import the dependencies.
import datetime as dt
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///C:/Users/Talon Mehta/OneDrive/Desktop/Data Analytics/Module 10 Challenge/Resources")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.stations

# Create our session (link) from Python to the DB
session = Session(engine)


#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################
@app.route("/")
def welcome():
    return(
        f"/api/v1.0/precipitation"
        f"<br/>"
        f"/api/v1.0/stations"
        f"<br/>"
        f"/api/v1.0/tobs"
        f"<br/>"
        f"/api/v1.0/<start>"
        f"<br/>"
        f"/api/v1.0/<start>/<end>"
    )

