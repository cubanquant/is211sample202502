import argparse
import urllib.request
import logging
import datetime

def download_data(url):
    """
    Reads data from a URL and returns the data as a string

    :param url:
    :return: the content of the URL
    """
    # read the URL
    with urllib.request.urlopen(url) as response:
        response = response.read().decode('utf-8')

    # return the data
    return response


def processData(file_content):
    """
    takes the contents of the file as the first parameter, processes
    the file line by line, and returns a dictionary that maps a person’s ID to a tuple of the form (name, birthday).
    """
    file_lines = file_content.split("\n")

    result_dict = dict()
    for line in file_lines:
        # deal with empty line
        if len(line) == 0:
            continue
        # deal with the header
        if line.startswith("id"):
            continue
        
        elements = line.split(",")
        id = elements[0]
        name = elements[1]
        birthday_string = elements[2]
        try:
            # convert the birthday string to a date in format %d/%m/%Y
            birthday = datetime.datetime.strptime(birthday_string, "%d/%m/%Y")
            print(f"id = {id} | name = {name} | birthday = {birthday}")
            # add values to result_dict using id as key and the value will be (name, birthday)
        except Exception as e:
            # use the logging module to log error
            print(e)
            print(f"there was a problem with line {line}")

        # convert the birthday string to a date in format %d/%m/%Y
        
    return result_dict


def displayPerson(id, personData):
    pass


def main(url):
    print(f"Running main with URL = {url}...")

    url_data = download_data(url)
    person_dict = processData(url_data)
    
    # ask user for an ID and call displayPerson
    id = input("Enter an Id to search: ")
    displayPerson(id, person_dict)
    

if __name__ == "__main__":
    """Main entry point"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", help="URL to the datafile", type=str, required=True)
    args = parser.parse_args()
    main(args.url)