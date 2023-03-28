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

def display_day_trip(day_trip_options):
    print()
    print("Here's your day trip:")
    print(f"You'll be going to {day_trip_options[0]} by {day_trip_options[2]}.")
    print(f"You'll be dining at {day_trip_options[1]} after {day_trip_options[3]}.")
    print()
    

def confirm_trip():
    user_response = ''

    while user_response != 'y':
        day_trip_list = generate_day_trip()   
        display_day_trip(day_trip_list)
        user_response = input('Are you satisfied with your day trip? y/n ')
    print()
    print('Enjoy your trip! Goodbye...')


confirm_trip()