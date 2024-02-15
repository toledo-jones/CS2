# !/usr/bin/env python3
# coding: utf-8
"""
Name: Cody Bogausch
Description:  If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile),
 then 3 miles at tempo (7:12 per mile) and 1 mile at easy pace again,
 what time do I get home for breakfast?
"""
# TODO: Learn how to store times in python better / this is definitely my worst one. Haha. 
# Running rates are stored as a list of tuples (minutes, seconds)
RATES = [(8, 15), (7, 12)]

# Starting time stored as a list [hours, minutes, "AM/PM"]
STARTING_TIME = [6, 52, "AM"]


# Get the seconds value for each rate
SECONDS = 2 * RATES[0][1] + 3 * RATES[1][1]
minutes, seconds = divmod(SECONDS, 60)
# Get the minutes falue for each rate
MINUTES = 2 * RATES[0][0] + 3 * RATES[1][0] + minutes
hours, minutes = divmod(MINUTES, 60)
HOURS = 6 + hours
print(f"Got Home at: {HOURS}:{MINUTES}:{SECONDS}")

# closer ^^^^ not perfect still but... moving on...