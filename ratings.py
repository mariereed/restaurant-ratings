def alphabetize_ratings_from_disk(filename):
    """ Takes a file of restaurants and ratings, returns the contents
    alphabetized.
    """

    # Opens a file
    your_file = open(filename)

    # Declares empty dict
    restaurants = {}

    # Loops through file lines and fills dict
    for line in your_file:
        line = line.rstrip()
        r_name, r_rating = line.split(':')
        restaurants[r_name] = restaurants.get(r_name, r_rating)

    return restaurants


def print_ratings(dictionary):
    """ Sorts and prints the contents of the dictionary.
    """

    print
    # Loops through dict and prints sorted, formatted key-value pairs
    for r_name, r_rating in sorted(dictionary.items()):
        print '{} is rated at {}.'.format(r_name, r_rating)


def add_restaurant_rating(rest_dict):
    """ User inputs restaurant name and rating, adds to existing dictionary.

    """
    restaurant_name = raw_input("Enter the restaurant name to rate: ")
    while True:
        restaurant_rating = raw_input("Enter the rating (1 to 5) for the restaurant: ")
        if restaurant_rating in '12345':
            break
        else:
            print "Sorry we only accept integers between 1 and 5 inclusively."

    rest_dict[restaurant_name] = restaurant_rating


def decide_user_actions():
    """ Processes data; user decides to view, add, or quit.
    """

    print
    rest_dict = alphabetize_ratings_from_disk('scores.txt')

    while True:
        decision = raw_input(
            "Press 'V' to View the list, "
            "'A' to Add to the list, "
            "or 'Q'" "to quit. ")
        if decision.upper() == 'Q':
            break
        elif decision.upper() == 'V':
            print_ratings(rest_dict)
        elif decision.upper() == 'A':
            add_restaurant_rating(rest_dict)
        else:
            print "I don't understand you. Please try again."

        print

decide_user_actions()
