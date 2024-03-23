# function to validate user input
def get_valid_input(prompt, valid_options=None, input_type=str):
    while True:
        # prompts user for input and converts input to lower case
        user_input = input(prompt).lower()
        try:
            # attempts to convert user input into specified data type
            user_input = input_type(user_input)
            # If valid options are provided (destinations list) 
            # and user input is not in the list of valid options, raise a ValueError
            if valid_options is not None and user_input not in valid_options:
                raise ValueError("Invalid option.")
            return user_input
        except ValueError:
            # If conversion fails or user input is not valid, prompt the user to try again
            print("Invalid input. Please try again.")

# function to calculate plane costs 
def plane_cost(city_flight):
    return costs_dic[city_flight]['plane_cost']
    

# function to calculate hotel costs 
def hotel_cost(city_flight, num_nights):
    return costs_dic[city_flight]['hotel_cost'] * num_nights


# function to calculate car rental costs 
def car_rental(city_flight, rental_days):
    return costs_dic[city_flight]['rental_cost'] * rental_days


# function to calculate total holiday costs 
def holiday_cost ():
    return plane_cost(city_flight) + hotel_cost(city_flight, num_nights) + car_rental(city_flight, rental_days)

#=========MAIN PROGRAMME==========

print("""Hello and welcome to the holiday calculator!
Here's a list of our destinations:
1. Paris
2. Madrid
3. Milan
4. Lisbon
5. Prague
6. Berlin""")

# list of destinations to validate correct input
destinations = ["paris", "madrid", "milan", "lisbon", "prague", "berlin"]

# dictionary containing the associated costs
costs_dic = {
    "paris": {"plane_cost": 180, "hotel_cost": 200, "rental_cost": 80},
    "madrid": {"plane_cost": 110, "hotel_cost": 190, "rental_cost": 70},
    "milan": {"plane_cost": 195, "hotel_cost": 210, "rental_cost": 75},
    "lisbon": {"plane_cost": 150, "hotel_cost": 140, "rental_cost": 45},
    "prague": {"plane_cost": 100, "hotel_cost": 130, "rental_cost": 60},
    "berlin": {"plane_cost": 90, "hotel_cost": 110, "rental_cost": 75}
}

# get user input, validate if correct input using predefined function  
city_flight = get_valid_input("Please enter your destination: ", destinations)
num_nights = get_valid_input("Please enter the number of nights you'll be staying: ", input_type=int)
rental_days = get_valid_input("Please enter the number of days you'll be hiring a car: ", input_type=int)


# output summary of holiday and costs using predefined functions
try: 
    total_cost = holiday_cost(city_flight, num_nights, rental_days)
    print(f"""\nYou've chosen on a trip to {city_flight.capitalize()}!  
The cost breakdown is as follows: 
Flight: £{plane_cost(city_flight)} 
Hotel stay for {num_nights} nights: £{hotel_cost(city_flight, num_nights)}
Car hire for {rental_days} days: £{car_rental(city_flight, rental_days)}
---------------------------------------------------
The total cost for the holiday is: £{holiday_cost()}
""")
except KeyError:
    print("Error: Destination not found.")
except Exception as e:
    print("An error occurred:", e)