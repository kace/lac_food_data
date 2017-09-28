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


## Reads CSV into Dicts
# TODO adds an entry into food[] for each entry in CSV, resulting in dupes. Need to grab entries by the unique 'RECORD ID'
#from setup import pullSource
#csv = pullSource()
#keys = [ key for key in csv[0].keys() if key not in ['VIOLATION CODE DESCRIPTION','VIOLATION CODE','COUNT','ROW ID','PROGRAM ELEMENT CODE','PROGRAM ELEMENT CODE','PROGRAM ELEMENT CODE DESCRIPTION','POINTS','ADDRESS']]
#food = []
#for entry in csv:
#    food.append({k:entry[k] for k in keys})

## An example of grouping violations from multiple rows into one list. To be added to each distinct dict. 
#food[0]['VIOLATIONS']=(sorted({entry['VIOLATION CODE DESCRIPTION'] for entry in csv if entry['RECORD ID'] == food[0]['RECORD ID'] }))



# An example of grouping
'''
import collections
by_year = collections.defaultdict(Counter)
for rec in food:
    by_year[rec['ACTIVITY DATE'][-4:]][rec['NAME'].upper().replace("'","").strip()] += 1
by_year['2016'].most_common(10)
'''
