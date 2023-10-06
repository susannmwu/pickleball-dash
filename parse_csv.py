import csv
import re

with open("pickleball.csv", "r") as source:
    csv_reader = csv.reader(source)

    for line in csv_reader:
        print(line)


def remove_words(line):
    line = re.sub(r"<.*?>", "", line)


with open("pickleball.csv") as f:
    for line in f.readlines():
        print(remove_words(line))
