import random

def generate_day_trip():
    destinations = ['Maui', 'Hong Kong', 'Sydney', 'Capetown', 'London', 'Fiji']
    restaurants = ['The Leaky Cauldron', 'The Inn of the Prancing Pony', 'Mos Isley Cantina', 'Ten Forward Lounge', 'Krabby Patty', 'Arbys']
    transportations = ['rickshaw', 'horseback', 'hoverboard', 'jetpack', 'piggyback', 'flying carpet']
    entertainments = ['bar hopping', 'skydiving', 'parasailing', 'snorkeling', 'spelunking', 'backpacking']

    destination = random.choice(destinations)
    restaurant = random.choice(restaurants)
    transportation = random.choice(transportations)
    entertainment = random.choice(entertainments)

    return [destination, restaurant, transportation, entertainment]


user_response = ''

while user_response != 'y':
    day_trip_list = generate_day_trip()
    
    # display the day trip to the user in the terminal (print each variable)
    print()
    print("Here's your day trip:")
    print(f"You'll be going to {day_trip_list[0]} by {day_trip_list[2]}.")
    print(f"You'll be dining at {day_trip_list[1]} after {day_trip_list[3]}.")
    print()

    # ask user if they're satisfied with the day trip (input function)
    user_response = input('Are you satisfied with your day trip? y/n ')


# --- if user's response is yes, complete trip (aka break the loop)
# --- if user's response is no, go back to step 1 (while loop, condition ???)