"""Functions to parse a file containing villager data."""

filename = 'villagers.csv'


def all_species(filename):
    """Return a set of unique species in the given file.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - set[str]: a set of strings
    """
    file = open(filename)  # Open the file

    species = set()

    # Iterate over each line in the file
    for line in file:
        # Remove trailing whitespace, create a list of strings
        villager = line.rstrip().split('|')

        # Add each species to the species set
        species.add(villager[1])

    return species


def get_villagers_by_species(filename, search_string="All"):
    """Return a list of villagers' names by species.

    Arguments:
        - filename (str): the path to a data file
        - search_string (str): optional, the name of a species

    Return:
        - list[str]: a list of names
    """
    search_string = search_string.title()

    file = open(filename)  # Open the file

    villagers = []

    # Iterate over each line in the file
    for line in file:
        # Remove trailing whitespace, create a list of strings
        villager = line.rstrip().split('|')

        # assign variable for names and species
        villager_name = villager[0]
        villager_species = villager[1]

        # if species matches or we search for all species, add name to list
        if search_string == "All" or search_string == villager_species:
            villagers.append(villager_name)

    return sorted(villagers)


def all_names_by_hobby(filename):
    """Return a list of lists containing villagers' names, grouped by hobby.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[list[str]]: a list of lists containing names
    """

    file = open(filename)

    # Initialize a dictionary of hobbies
    hobbies = {'fitness': [],
               'nature': [],
               'education': [],
               'music': [],
               'fashion': [],
               'play': []}

    # Iterate over each line of the file
    for line in file:
     # Remove trailing whitespace, create a list of strings
        villager = line.rstrip().split('|')

        # Assign meaningful variable names for name and hobby
        villager_name = villager[0]
        villager_hobby = villager[3].lower()

        # Add the villager's name to the list for their hobby
        hobbies[villager_hobby].append(villager_name)

    # Return a list of each sublist of names by hobby
    return list(hobbies.values())


def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (name, species, personality, hobby,
    saying).

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[tuple[str]]: a list of tuples containing strings
    """

    all_data = []

    # Open the file
    file = open(filename)

    # Iterate over each line of the file
    for line in file:
        # Remove trailiing whitespace, create a list of strings, make it a tuple
        villager_tuple = tuple(line.rstrip().split('|'))

        # Append the villager to the all_data list
        all_data.append(villager_tuple)

    return all_data


def find_motto(filename, villager_name):
    """Return the villager's motto.

    Return None if you're not able to find a villager with the
    given name.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name

    Return:
        - str: the villager's motto or None
    """

    # Open the file
    file = open(filename)

    # Iterate over each line of the file
    for line in file:
        # If the line begins with the given villager name
        if line.startswith(villager_name):
            # Strip the trailing whitespace, split the line into a list of strings
            # The villager's motto is the 4th element in that list of strings
            # Return that motto
            return line.rstrip().split('|')[4]

    # If no villagers match the given name, return None
    return None


def find_likeminded_villagers(filename, villager_name):
    """Return a set of villagers with the same personality as the given villager.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name

    Return:
        - set[str]: a set of names

    For example:
        >>> find_likeminded_villagers('villagers.csv', 'Wendy')
        {'Bella', ..., 'Carmen'}
    """

    # Initialize an empty dictionary of personalities, an empty string for the target personality
    villagers_by_personality = {}
    target_personality = ''

    # Open the file
    file = open(filename)

    # Iterate over each line of the file
    for line in file:
        # Strip the trailing whitespace, split the line into a list of strings
        villager = line.rstrip().split('|')

        # Set variables for name and personality
        name = villager[0]
        personality = villager[2]

        # Check if that personality is already a key in the dictionary. Add it the existing list, or creat a new key/list
        if personality in villagers_by_personality.keys():
            villagers_by_personality[personality].add(
                name)
        else:
            villagers_by_personality[personality] = {name}

        # Check if this is the given villager. If so, rememeber their personality
        if name == villager_name:
            target_personality = personality

    return villagers_by_personality[target_personality]
