import pandas as pd
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re


def main():
    request = open("FlightRequest.txt", 'r')
    flight_info = request.read()
    url = "https://www.flightstats.com/v2/flight-tracker/" + str(flight_info[0:2]) + "/" + str(flight_info[2:])
    website = urlopen(url)

    parser = BeautifulSoup(website, 'lxml')
    create_data(parser)


def create_data(parser):
    print(parser.find_all('div', {'class': 'text-helper__TextHelper-s8bko4a-0 blQyiG'}))


if __name__ == "__main__":
    main()
