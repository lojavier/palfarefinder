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
# print request

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
tripOption = trips["tripOption"]
print json.dumps(tripOption[0], sort_keys=True, indent=4)
for x in range(0,len(tripOption)-1):
# for x in range(0,1):
	print "************************************************************************************"
	saleTotal 		= tripOption[x]["saleTotal"].replace("USD","$")
	print "Price: %s" % (saleTotal)

	carrier 		= tripOption[x]["slice"][0]["segment"][0]["flight"]["carrier"]
	number			= tripOption[x]["slice"][0]["segment"][0]["flight"]["number"]
	origin 			= tripOption[x]["slice"][0]["segment"][0]["leg"][0]["origin"]
	destination 	= tripOption[x]["slice"][0]["segment"][0]["leg"][0]["destination"]
	departureTime24 = tripOption[x]["slice"][0]["segment"][0]["leg"][0]["departureTime"]
	departureTime12 = datetime.datetime.strptime(departureTime24[:16], "%Y-%m-%dT%H:%M").strftime('%m-%d-%Y %I:%M%p')
	arrivalTime24 	= tripOption[x]["slice"][0]["segment"][0]["leg"][0]["arrivalTime"]
	arrivalTime12 = datetime.datetime.strptime(arrivalTime24[:16], "%Y-%m-%dT%H:%M").strftime('%m-%d-%Y %I:%M%p')
	durationMinutes = tripOption[x]["slice"][0]["segment"][0]["leg"][0]["duration"]
	duration 		= "%dH:%02dM" % (durationMinutes/60,durationMinutes%60)
	print "%s - Flight %s" % (carrier,number)
	print "%s [%s] -> [%s] %s / %s" % (departureTime12,origin,destination,arrivalTime12,duration)

	try:
		carrier 		= tripOption[x]["slice"][0]["segment"][1]["flight"]["carrier"]
		number			= tripOption[x]["slice"][0]["segment"][1]["flight"]["number"]
		origin 			= tripOption[x]["slice"][0]["segment"][1]["leg"][0]["origin"]
		destination 	= tripOption[x]["slice"][0]["segment"][1]["leg"][0]["destination"]
		departureTime24 = tripOption[x]["slice"][0]["segment"][1]["leg"][0]["departureTime"]
		departureTime12 = datetime.datetime.strptime(departureTime24[:16], "%Y-%m-%dT%H:%M").strftime('%m-%d-%Y %I:%M%p')
		arrivalTime24 	= tripOption[x]["slice"][0]["segment"][1]["leg"][0]["arrivalTime"]
		arrivalTime12 = datetime.datetime.strptime(arrivalTime24[:16], "%Y-%m-%dT%H:%M").strftime('%m-%d-%Y %I:%M%p')
		durationMinutes = tripOption[x]["slice"][0]["segment"][1]["leg"][0]["duration"]
		duration 		= "%dH:%02dM" % (durationMinutes/60,durationMinutes%60)
		print "%s - Flight %s" % (carrier,number)
		print "%s [%s] -> [%s] %s / %s" % (departureTime12,origin,destination,arrivalTime12,duration)
	except:
		print ""
	print ""

	carrier 		= tripOption[x]["slice"][1]["segment"][0]["flight"]["carrier"]
	number			= tripOption[x]["slice"][1]["segment"][0]["flight"]["number"]
	origin 			= tripOption[x]["slice"][1]["segment"][0]["leg"][0]["origin"]
	destination 	= tripOption[x]["slice"][1]["segment"][0]["leg"][0]["destination"]
	departureTime24 = tripOption[x]["slice"][1]["segment"][0]["leg"][0]["departureTime"]
	departureTime12 = datetime.datetime.strptime(departureTime24[:16], "%Y-%m-%dT%H:%M").strftime('%m-%d-%Y %I:%M%p')
	arrivalTime24 	= tripOption[x]["slice"][1]["segment"][0]["leg"][0]["arrivalTime"]
	arrivalTime12 = datetime.datetime.strptime(arrivalTime24[:16], "%Y-%m-%dT%H:%M").strftime('%m-%d-%Y %I:%M%p')
	durationMinutes = tripOption[x]["slice"][1]["segment"][0]["leg"][0]["duration"]
	duration 		= "%dH:%02dM" % (durationMinutes/60,durationMinutes%60)
	print "%s - Flight %s" % (carrier,number)
	print "%s [%s] -> [%s] %s / %s" % (departureTime12,origin,destination,arrivalTime12,duration)

	try:
		carrier 		= tripOption[x]["slice"][1]["segment"][1]["flight"]["carrier"]
		number			= tripOption[x]["slice"][1]["segment"][1]["flight"]["number"]
		origin 			= tripOption[x]["slice"][1]["segment"][1]["leg"][0]["origin"]
		destination 	= tripOption[x]["slice"][1]["segment"][1]["leg"][0]["destination"]
		departureTime24 = tripOption[x]["slice"][1]["segment"][1]["leg"][0]["departureTime"]
		departureTime12 = datetime.datetime.strptime(departureTime24[:16], "%Y-%m-%dT%H:%M").strftime('%m-%d-%Y %I:%M%p')
		arrivalTime24 	= tripOption[x]["slice"][1]["segment"][1]["leg"][0]["arrivalTime"]
		arrivalTime12 = datetime.datetime.strptime(arrivalTime24[:16], "%Y-%m-%dT%H:%M").strftime('%m-%d-%Y %I:%M%p')
		durationMinutes = tripOption[x]["slice"][1]["segment"][1]["leg"][0]["duration"]
		duration 		= "%dH:%02dM" % (durationMinutes/60,durationMinutes%60)
		print "%s - Flight %s" % (carrier,number)
		print "%s [%s] -> [%s] %s / %s" % (departureTime12,origin,destination,arrivalTime12,duration)
	except:
		print ""
	print "************************************************************************************"
	print "####################################################################################"

print ""

data = trips["data"]
requestId = trips["requestId"]
city = data["city"]
tax = data["tax"]
airport = data["airport"]
aircraft = data["aircraft"]
carrier = data["carrier"]
