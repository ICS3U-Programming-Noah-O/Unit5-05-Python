#!/usr/bin/env python3
# Created By: Noah Ouellette
# Date: Jan. 25, 2022
# This program accepts an address from a
# user and then formats it nicely


def format_address(name, street_num, street,
                   city, province, postal, apartment_num=None):

    # This function organizes the address
    address = name

    # If the user inputted the apartment number print a different outcome
    if apartment_num is not None:
        address = address + " \n" + apartment_num + "-" + street_num + \
                 " " + street + " \n" + city + " " + province + " " + postal
    else:
        address = address + " \n" + street_num + " " + street + \
                 " \n" + city + " " + province + " " + postal

    # Return the final address to the main function
    return address


def main():
    # this gets the user input and then calls the function

    apartment_number = None
    print("This program can format your address nicely.")
    print(" ")
    print(" ")

    # Get the various user inputs and ask the user if they're in an apartment
    user_name = input("Please enter your full name: ")
    user_answer = input("Do you live in an apartment? y/n: ")
    if user_answer.upper() == "Y" or user_answer.upper() == "YES":
        apartment_number = input("Enter your apartment number: ")
    print(" ")
    street_address = input("Enter your street address number: ")
    street_name = input("Enter the name of your street " +
                        "and type of street (ex: Ave.): ")
    city_name = input("Enter the name of your city: ")
    province_name = input("Enter the name of your province " +
                          "(As an abbreviation): ")
    postal_code = input("Enter your postal code: ")
    print(" ")

    # Detect if the user lives in an apartment
    # Call the function based on whether or not the user lives in an apartment
    if apartment_number is not None:
        final_address = format_address(user_name,
                                       street_address,
                                       street_name,
                                       city_name,
                                       province_name,
                                       postal_code,
                                       apartment_number)
    else:
        final_address = format_address(user_name,
                                       street_address,
                                       street_name,
                                       city_name,
                                       province_name,
                                       postal_code,
                                       apartment_number)
    # Print the final organized address
    print(final_address)


if __name__ == "__main__":
    main()
