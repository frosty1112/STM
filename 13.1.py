import urllib.request ( urllib.request module help to open URL that given by you)

import urllib.parse (urllib.parse module used for checking the url details by breaking into component then combine into base url)

import urllib.error ( this module handle the error that occur during requesting of URL)

import json (This allow to the access of JSON format file)

api_url=' https://maps.googleapis.com/maps/api/geocode/json?' (Here use your Google API)

while True:

city_location = input ("Enter your location here that you want to search: ")

if not city_location:

break

url= api_url + urllib.parse.urlencode({ ' Location ' : city_location} )

print ( " Retrieving Data", url )

url_read = url.request.urlopen(url)

data = url_read().decode()

print ( ' Retrieved ', len(data) , 'characters')
