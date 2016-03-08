#!/usr/bin/env python
import os
import re
import sys
import json
import time
import urllib2
# import MySQLdb
import smtplib
import datetime
import requests
import mechanize
import subprocess
from datetime import date
from HTMLParser import HTMLParser
from email.mime.text import MIMEText
from htmlentitydefs import name2codepoint

cwd = os.getcwd()
requestJson = "request.json"
responseJson = "response.json"
# reservationUrl = "http://www.philippineairlines.com"
# reservationUrl = "https://onlinebooking.philippineairlines.com/flypal/AirFlightSearchForward.do"
# reservationUrl = "https://onlinebooking.philippineairlines.com/flypal/"
# reservationUrl = "https://www.southwest.com/flight/"
# reservationUrl = "https://onlinebooking.philippineairlines.com/palmobile/air-shopping"
# reservationUrl = "http://www.makemytrip.com/international-flights/philippine-airlines-pr.html"
# reservationUrl = "http://www.skyscanner.com/airline/airline-philippine-airlines-pr.html"
reservationUrl = "https://www.google.com/flights"
# reservationUrl = "http://www.skyscanner.com"

apiKey = "AIzaSyDdCgmwyPjb_z9E2T-eAetU-oIGLXQ399M"
qpxExpressApiUrl = "https://www.googleapis.com/qpxExpress/v1/trips/search?key=%s" % (apiKey)
curlCommand = "curl -s -d @request.json --header \"Content-Type: application/json\" %s > %s" % (qpxExpressApiUrl,responseJson)

adultCount = 1
origin = "SFO"
destination = "MNL"
departureDate = "2016-10-28"
returnDate = "2016-11-13"

request = {
	"request":{
		"passengers":{
			"adultCount":adultCount
		},
		"slice":[
		{	"origin":origin,
			"destination":destination,
			"date":departureDate
		},
		{	"origin":destination,
			"destination":origin,
			"date":returnDate
		}
		]
	}
}
request = json.dumps(request, sort_keys=True, indent=4)
print request

with open(requestJson, "w") as f:
	f.write(str(request))
	f.close()

# os.system(curlCommand)
# response = json.dumps(response, sort_keys=True, indent=4)
# with open(responseJson, "w") as f:
# 	f.write(str(response))
# 	f.close()

with open(responseJson, "r") as f:
	response = f.read()
	response = json.loads(response)
	# response = json.dumps(f.read(), sort_keys=True, indent=4)
	f.close()
# print response

# print json.dumps(response, sort_keys=True, indent=4)
print response.keys()
kind = response["kind"]
trips = response["trips"]
print trips.keys()
# print trips
tripOption = trips["tripOption"]
data = trips["data"]
requestId = trips["requestId"]
print tripOption.values()
# print data.keys()
# print data
city = data["city"]
tax = data["tax"]
airport = data["airport"]
aircraft = data["aircraft"]
carrier = data["carrier"]

# print city
# print tax
# print airport
# print aircraft
# print carrier

# # print tripOption
# # print requestId
# print data.keys()
# for key,value in trips.items():
# 	print key
# print trips
# for key in trips.keys():
# 	print key
# print trips.keys()

# for x in trips.values():
	# print x
# for key1,value1 in response.items():
# 	print key1
	# print value1
	# for key2,value2 in value1.items():
	# 	print key2
	# if "name" in key1:
	# 	print "%s : %s" % (key1,value1)

# print response["pricing"]