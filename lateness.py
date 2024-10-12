import os
from dotenv import load_dotenv
import requests
import time
import datetime
import pytz

load_dotenv()

api_key = os.getenv("GMAP_TOKEN")


def get_time_away(origin: str, destination: str) -> int:
    url = f"https://maps.googleapis.com/maps/api/distancematrix/json?units=metric&origins={origin}&destinations={destination}&key={api_key}"
    response = requests.get(url)
    return response.json()["rows"][0]["elements"][0]["duration"][
        "value"
    ]  # Returns time in seconds


def get_distance_away(origin: str, destination: str) -> int:
    url = f"https://maps.googleapis.com/maps/api/distancematrix/json?units=metric&origins={origin}&destinations={destination}&key={api_key}"
    response = requests.get(url)
    return response.json()["rows"][0]["elements"][0]["distance"][
        "value"
    ]  # Returns distance in meters


# Coordinates for New York City and Los Angeles
destination = "47.66670626052332, -122.29287218150294"
person1 = "47.67514355986064, -122.31578292886068"
person2 = "47.65665093968562, -122.31093714852052"
person3 = "47.7869048884025, -122.34105805217644"
person4 = "34.0522,-118.2437"
person5 = "45.527008403811664, -122.54439188826156"

curr_time = time.time()  # Current time in epoch

year = int(input("Year? "))
month = int(input("Month? "))
day = int(input("Day? "))
hour = int(input("Hour? "))
minute = int(input("Minute? "))

goal_time = datetime.datetime(year, month, day, hour, minute)


print(f"Current time: {curr_time}")
print(f"Goal time (in epoch): {goal_time}")
print(f"Time difference (in minutes): {(goal_time - curr_time) / 60}")

people_list = [person1, person2, person3, person4, person5]

for i, person in enumerate(people_list):
    arrival_time = curr_time + get_time_away(
        person, destination
    )  # Add travel duration in seconds

    lateness_num = arrival_time - goal_time

    if lateness_num < 0:
        print(f"Person {i + 1} is going to be on time")
    else:
        print(
            f"Person {i + 1} is going to be late by {lateness_num / 60} minutes"
        )
