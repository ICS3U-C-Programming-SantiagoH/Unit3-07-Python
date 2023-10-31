#!/usr/bin/env python3
# Created by: Santiago Hewett
# Created on: Oct 30, 2023
# This program will ask the user
# for their age and tell them if
# they can date my grandchild


def main():
    # Get the user integer
    print("This program will ask the user for their age")
    print("then it will display if you are eligible to date my grandchild.")

    user_age_string = input("Please enter your age: ")

    # initialize variable
    user_age_integer = None

    # Try catch statement
    try:
        user_age_integer = int(user_age_string)

        # Check if the user guess as int meets my requirements

        if user_age_integer > 25 and user_age_integer < 40:
            # Display if the user can date
            print("\nCongratulations, you can date my grandchild")

        else:
            # Display if user age is not reasonable

            if user_age_integer < 0 or user_age_integer > 120:
                print("\n{} is not a valid age.".format(user_age_integer))

            # Display if user is too young

            elif user_age_integer < 25:
                print("\nYou are too young to date my grandchild")

            # Display if user age as int is too old

            else:
                print("\nYou are too old to date my grandchild")

    # Checking it the if the input is a string and if it is then telling user
    except Exception:
        print("\n{} is not a valid age".format(user_age_string))

    # Always display this to user
    finally:
        print("\nThanks for playing!")


if __name__ == "__main__":
    main()
