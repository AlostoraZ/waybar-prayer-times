#!/usr/bin/env python3
import requests
from datetime import date, datetime

def to_minutes(tstr):
    h, m = map(int, tstr.split(":"))
    return h * 60 + m

baseUrl = "https://api.aladhan.com/v1/timingsByAddress/"

def getPrayerTimes(currentDate, address):
    url = f"{baseUrl}{currentDate}?address={address}&method={method}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("API error:", response.status_code)
        return None

currentDate = date.today().strftime("%d-%m-%Y")
currentMinutes = to_minutes(datetime.now().strftime("%H:%M"))

address = "Dubai,UAE" # Add your location in the following format "City,Country"
method = "3"          # Choode your calculation method based on your location
times = getPrayerTimes(currentDate,address)

if times:
    prayers = [
        ("Fajr",    times["data"]["timings"]["Fajr"]),
        ("Dhuhr",   times["data"]["timings"]["Dhuhr"]),
        ("Asr",     times["data"]["timings"]["Asr"]),
        ("Maghrib", times["data"]["timings"]["Maghrib"]),
        ("Isha",    times["data"]["timings"]["Isha"]),
    ]

    # find next prayer
    next_prayer = None
    for name, tstr in prayers:
        if currentMinutes < to_minutes(tstr):
            next_prayer = (name, tstr)
            break

    # if none left → (past Isha), next is Fajr next day
    if not next_prayer:
        next_prayer = ("Fajr", prayers[0][1])

    name, tstr = next_prayer

    # Convert output to 12h format
    t12 = datetime.strptime(tstr, "%H:%M").strftime("%I:%M")

    print(f"{name}: {t12}")

else:
    print("Error")
