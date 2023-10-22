"""Script to seed database with pickleball data"""
from flask import Flask
import pandas as pd

import os
import model
import crud
import server


app = Flask(__name__)
app.secret_key = 'SECRETSECRETSECRET'
app.config['PRESERVE_CONTEXT_ON_EXCEPTION'] = True

os.system("dropdb workouts")
os.system("createdb workouts")
model.connect_to_db(server.app)
model.db.create_all()

"""Seed pickleball workout data from csv"""
data = pd.read_csv("pickleball.csv")

df = pd.DataFrame(data, columns=["startDate", "endDate", "activityType", "duration",
                                 "HKWeatherHumidity", "totalEnergyBurned", "HKWeatherTemperature"])
# print information about the data
# print(df.info())

df["startDate"] = pd.to_datetime(df["startDate"])
df["endDate"] = pd.to_datetime(df["endDate"])

for row in df.head(10):
    startDate = df["startDate"]
    print(startDate)
    print(type(startDate))

# iterate through the rows and use the .head() method to show all the rows
# parameter inside .head() should be the max number of rows
# assign each variable to its respective column


# for i, row in df.iterrows():
#     workout_record = crud.create_workout(row["startDate"], row["endDate"], row["activityType"],
#                                          row["duration"], row["HKWeatherHumidity"], row["totalEnergyBurned"],
#                                          row["HKWeatherTemperature"])


# model.db.session.add(workout_record)
# model.db.session.commit()
