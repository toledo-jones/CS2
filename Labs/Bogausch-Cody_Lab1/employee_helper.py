# !/usr/bin/env python3
# coding: utf-8
"""
Name: Cody Bogausch
Description:   An employee’s total weekly pay equals the hourly wage
multiplied by the total number of regular hours plus any overtime pay.
Overtime pay equals the total overtime hours multiplied by 1.5 times the hourly wage.
Write a program that takes as inputs the hourly wage, total regular hours,
and total overtime hours and displays an employee’s total weekly pay.
"""


def main():
    # Entry point
    print("Hours Calculator v 1.00")
    try:
        # Get user input regarding wage, hours and over time. 
        # TODO: Refactor this to use total hours and automatically calculate overtime
        wage = float(input("Enter your hourly wage: "))
        regular_hours = float(input("Enter total regular hours:  "))
        overtime_hours = float(input("Total overtime hours: "))

        # Display total pay formatted to two decimal points
        # Total pay is returned from get_weekly_pay()
        print(f"Total pay this week is: ${"{:.2f}".format(get_weekly_pay(regular_hours, overtime_hours, wage))}")
    # Handle bad input by restarting 
    except Exception as e:
        # Show error
        print(f"Error: {e}")
        print("Rebooting...")

        # Recurse 
        main()


def get_weekly_pay(regular_hours: float, overtime_hours: float, wage: float):
    # Over time wage is 1.5 times standard wage. 
    overtime_wage = wage * 1.5

    # Calculate pay for normal hours
    regular_pay = regular_hours * wage

    # Calculate pay for over time hours
    overtime_pay = overtime_hours * overtime_wage

    # Send back result to main
    return regular_pay + overtime_pay


# If this script is executed run as main
if __name__ == '__main__':
    main()
