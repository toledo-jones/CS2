# !/usr/bin/env python3
# coding: utf-8
"""
Name: Cody Bogausch
Description:  Suppose the cover price of a book is $24.95,
 but bookstores get a 40% discount.
 Shipping costs $3 for the first copy and 75 cents for each additional copy.
 What is the total wholesale cost for 60 copies?
"""

BOOK_PRICE = 24.95
BOOKSTORE_DISCOUNT = .40


def get_wholesale_cost(copies):
    # Calculate the cost for a bookstore to buy n number of books
    initial_price = BOOK_PRICE * copies

    # Apply wholesale discount
    discounted_price = apply_discount(initial_price)

    # Add shipping cost
    final_price = calculate_shipping_cost(copies) + discounted_price
    return final_price


def apply_discount(price):
    # Remove discount from the price 
    return price - price * BOOKSTORE_DISCOUNT


def calculate_shipping_cost(copies):
    # Shipping Cost is $3 for the first copy and .75 for each additional copy
    return .75 * copies + 3.0


def main():
    # Entry point
    print("Bookstore Calculator v 1.00")
    try:
        # Get input from user
        copies = int(input("Enter the number of books you want to buy:  "))

        # Display results
        print(f"Total Cost is: ${"{:.2f}".format(get_wholesale_cost(copies))}")

        # Handle bad input by restarting
    except Exception as e:
        # Show error
        print(f"Error: {e}")
        print("Rebooting...")

        # Recurse 
        main()


# If this script is executed run as main
if __name__ == '__main__':
    main()
