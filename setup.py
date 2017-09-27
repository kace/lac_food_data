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

# Separate rows into separate inspections


#{ rec['RECORD ID'] for rec in csv }
#
#
#record = csv[0]
#keys = [key in record.keys() if not in ['VIOLATION CODE DESCRIPTION','VIOLATION CODE','COUNT','ROW ID','PROGRAM ELEMNT CODE','PROGRAM ELEMENT CODE']]
#keys += 'VIOLATIONS'
#
#pprint(sorted({rec['VIOLATION CODE DESCRIPTION'] for rec in csv if rec['RECORD ID'] == 'PR0002167' }))
#record
#pprint(sorted({rec['VIOLATION CODE DESCRIPTION'] for rec in csv if rec['RECORD ID'] == 'PR0002167' }))
#del(record['POINTS'])
#VIOLATIONS = (sorted({rec['VIOLATION CODE DESCRIPTION'] for rec in csv if rec['RECORD ID'] == 'PR0002167' }))
#del(record['VIOLATION CODE DESCRIPTION'])
#record
#del(record['VIOLATION CODE'])
#record
#del(record['COUNT'])
#del(record['ROW ID'])
#del(record['PROGRAM ELEMNT CODE'])
#del(record['PROGRAM ELEMENT CODE'])
#record
#record.['VIOLATIONS'] = VIOLATIONS
#record['VIOLATIONS'] = VIOLATIONS
#record
#pprint(record)
#keys = [ key for key in csv[0].keys() if key not in ['VIOLATION CODE DESCRIPTION','VIOLATION CODE','COUNT','ROW ID','PROGRAM ELEMENT CODE','PROGRAM ELEMENT CODE','PROGRAM ELEMENT CODE DESCRIPTION','POINTS','ADDRESS']]
#entry = {x:csv[0][x] for x in keys}
#food = []
#for entry in csv:
#    food.append({k:entry[k] for k in keys}
#    food += ['VIOLATIONS'](sorted({entry['VIOLATION CODE DESCRIPTION'] for entry in csv if rec['RECORD ID'] == 'PR0002167' }))



# An example of grouping
'''
import collections
by_year = collections.defaultdict(Counter)
for rec in food:
    by_year[rec['ACTIVITY DATE'][-4:]][rec['NAME'].upper().replace("'","").strip()] += 1
by_year['2016'].most_common(10)
'''
