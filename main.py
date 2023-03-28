import random

destinations = ['Maui', 'Hong Kong', 'Sydney', 'Capetown', 'London', 'Fiji']
restaurants = ['The Leaky Cauldron', 'The Inn of the Prancing Pony', 'Mos Isley Cantina', 'Ten Forward Lounge', 'Krabby Patty', 'Arbys']
transportations = ['rickshaw', 'horseback', 'hoverboard', 'jetpack', 'piggyback', 'flying carpet']
entertainments = ['bar hopping', 'skydiving', 'parasailing', 'snorkeling', 'spelunking', 'backpacking']


# (15 points): As a user, I want to be able to randomly re-select a destination, restaurant, mode of transportation, 
# and/or form of entertainment if I don’t like one or more of those things.

user_response = ''

while user_response != 'y':
    # generate/regenerate the day trip
    destination = random.choice(destinations)
    restaurant = random.choice(restaurants)
    transportation = random.choice(transportations)
    entertainment = random.choice(entertainments)
    
    # display the day trip to the user in the terminal (print each variable)
    print()
    print("Here's your day trip:")
    print(f"You'll be going to {destination} by {transportation}.")
    print(f"You'll be dining at {restaurant} after {entertainment}.")
    print()

    # ask user if they're satisfied with the day trip (input function)
    user_response = input('Are you satisfied with your day trip? y/n ')


# --- if user's response is yes, complete trip (aka break the loop)
# --- if user's response is no, go back to step 1 (while loop, condition ???)