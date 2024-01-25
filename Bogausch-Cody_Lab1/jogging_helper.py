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
RATES = [(8, 15), (7, 12), (8, 15)]

# Starting time stored as a list [hours, minutes, "AM/PM"]
STARTING_TIME = [6, 52, "AM"]


def rate_to_seconds(rate: tuple):
    # Takes a rate stored as (minutes, seconds)
    # and converts it to seconds
    return rate[0] * 60 + rate[1]


def seconds_to_minutes(seconds):
    # Returns minutes in tuple form (minutes, seconds)
    return divmod(seconds, 60)


def main():
    # Calculate total seconds that passed on the run:
    # TODO: Make this more dynamic and accept input, etc.
    time_elapsed = 0
    for rate in RATES:
        time_elapsed += rate_to_seconds(rate)

    # Convert time elapsed from seconds to minutes (minutes, seconds)
    minutes_elapsed = seconds_to_minutes(time_elapsed)

    # Calculate the arrival time
    arrival_time_minutes = (STARTING_TIME[1] + minutes_elapsed[0])
    additional_arrival_time_hours = 0
    if arrival_time_minutes >= 60:
        # First value of div mod will be our hours value
        additional_arrival_time_hours = divmod(arrival_time_minutes, 60)[0]

    ARRIVAL_TIME = [STARTING_TIME[0] + additional_arrival_time_hours, arrival_time_minutes - 60, 'AM']
    print(f" If you leave at {STARTING_TIME} you will arrive home at {ARRIVAL_TIME}")


# If this script is executed run as main
if __name__ == '__main__':
    main()
