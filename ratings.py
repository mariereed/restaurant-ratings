def alphabetize_ratings(filename):
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

    # Loops through dict and prints sorted, formatted key-value pairs
    for r_name, r_rating in sorted(restaurants.items()):
        print '{} is rated at {}.'.format(r_name, r_rating)


alphabetize_ratings('scores.txt')
