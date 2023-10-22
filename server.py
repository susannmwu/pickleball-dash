from datetime import datetime
import pandas as pd
import matplotlib as plt

from flask import Flask, render_template
from jinja2 import StrictUndefined


app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


# df.columns = Index(['sep=', 'Unnamed: 1'], dtype='object')

# Read the .csv file using pandas
data = pd.read_csv("pickleball.csv")
# print(data)
df = pd.DataFrame(
    data, columns=["startDate", "duration.1", "activityType"])

# convert str => datetime
# df["startDate"] is currently a str type, need to convert to datetime obj
reformatted_date = []

for date in df["startDate"]:
    date_format = "%Y-%m-%d %H:%M:%S %z"
    date_obj = datetime.strptime(date, date_format)
    # print(date_obj)
    new_date = date_obj.strftime("%m-%d-%Y")

    reformatted_date.append(new_date)


@app.route("/")
def index():
    df.plot(x="startDate", y="duration.1", kind="bar")
    dates = plt.xlabel("Dates")
    minutes = plt.ylabel("Playtime (mins)")
    plt.title("Susan's pickleball workouts")

    plt.savefig("/static/images/plot.png")
    return render_template("plot.html", dates=dates, minutes=minutes)


# @app.route("/plot.png")
# def plot_png():

#     df.plot(x="startDate", y="duration.1", kind="bar")
#     plt.xlabel("Dates")
#     plt.ylabel("Playtime (mins)")
#     plt.title("Susan's pickleball workouts")

#     plt.savefig("/static/images/plot.png")

# pickleball workout plots


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
