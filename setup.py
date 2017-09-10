#!/usr/bin/env python
#setup.py

import csv
import urllib2

def updateSource():
    ''' Downloads the most recent source csv '''
    url = 'https://data.lacounty.gov/api/views/b9ey-v6ni/rows.csv?accessType=DOWNLOAD'
    source = urllib2.urlopen(url)
    with open('LOS_ANGELES_COUNTY_RESTAURANTS_AND_MARKETS_VIOLATIONS.csv','wb') as output:
        output.write(source.read())

def loadSource():
    ''' Reads from the CSV into a list of dictionaries '''
    return list(csv.DictReader(open('LOS_ANGELES_COUNTY_RESTAURANTS_AND_MARKETS_VIOLATIONS.csv')))

def pullSource():
    ''' Pulls the most recent CSV into memory and reads it into a list of dictionaries '''
    url = 'https://data.lacounty.gov/api/views/b9ey-v6ni/rows.csv?accessType=DOWNLOAD'
    source = urllib2.urlopen(url)
    # DictReader requires an iterable to create a Dict from CSV
    return list(csv.DictReader(source.read().splitlines()))
