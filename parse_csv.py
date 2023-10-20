import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

# df.columns = Index(['sep=', 'Unnamed: 1'], dtype='object')

# Read the .csv file using pandas
data = pd.read_csv("pickleball.csv")
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


# pickleball workout plots
df.plot(x="reformatted_date", y="converted_duration", kind="bar")
plt.xlabel("Dates")
plt.ylabel("Playtime (mins)")
plt.title("Susan's pickleball workouts")
plt.ion
plt.show()
