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
    pass


def displayPerson(id, personData):
    pass


def main(url):
    print(f"Running main with URL = {url}...")

    url_data = download_data(url)
    person_dict = processData(url_data)
    
    # ask user for an ID and call displayPerson
    id = 5
    displayPerson(id, person_dict)
    

if __name__ == "__main__":
    """Main entry point"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", help="URL to the datafile", type=str, required=True)
    args = parser.parse_args()
    main(args.url)