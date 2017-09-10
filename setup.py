#!/usr/bin/env python
#setup.py

import csv
import urllib2

url = 'https://data.lacounty.gov/api/views/b9ey-v6ni/rows.csv?accessType=DOWNLOAD'
csv = urllib2.urlopen(url)
#food = list(csv.DictReader(open('LOS_ANGELES_COUNTY_RESTAURANTS_AND_MARKETS_VIOLATIONS.csv')))
#food = list(csv.DictReader(csv))
