import csv
import re

with open("pickleball.csv", "r") as source:
    csv_reader = csv.reader(source)

    for line in csv_reader:
        print(line)

    with open("new_pickleball.csv", "w") as result:
        csv_writer = csv.writer(result)
        for r in csv_reader:
            # r[0], r[1], r[2], r[3]
            csv_writer.writerow((r[1]))
