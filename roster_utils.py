from csv import DictReader, DictWriter
# a couple of functions that will read and write to a CSV file

# function that will read and return a list of the roster
def get_roster(filepath):
    data = []
    with open(filepath, 'r', newline='\n') as the_file:
        reader = DictReader(the_file)
        for row in reader:
            data.append(row)
    return data

def get_next_id(filepath):
    data = 0
    current_data = get_roster(filepath)
    data = int(current_data[-1]['id'])
    return data + 1


# function that will add a new entry to the list of the roster (at the end)
def add_to_roster(filepath, first_name, last_name):
    new_addition = {"id": get_next_id(filepath), "first_name": first_name, "last_name": last_name}
    with open(filepath, 'a', newline='\n') as the_file:
        writer = DictWriter(the_file, fieldnames=["id", "first_name", "last_name"])
        writer.writerow(new_addition)
    return new_addition


if __name__ == "__main__":
    FILEPATH = './roster.csv'
    # the_roster = get_roster(FILEPATH)
    # print(the_roster)

    # print(get_next_id(FILEPATH))

    # add_to_roster(FILEPATH, "Bernie", "Matthews")