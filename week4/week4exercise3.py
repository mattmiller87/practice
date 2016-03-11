'''
III. Create a program that converts the following uptime strings to a time in seconds.

uptime1 = 'twb-sf-881 uptime is 6 weeks, 4 days, 2 hours, 25 minutes'
uptime2 = '3750RJ uptime is 1 hour, 29 minutes'
uptime3 = 'CATS3560 uptime is 8 weeks, 4 days, 18 hours, 16 minutes'
uptime4 = 'rtr1 uptime is 5 years, 18 weeks, 8 hours, 23 minutes'

For each of these strings store the uptime in a dictionary using the device name as the key.

During this conversion process, you will have to convert strings to integers.  For these string to integer conversions use try/except to catch any string to integer conversion exceptions.

For example:
int('5') works fine
int('5 years') generates a ValueError exception.

Print the dictionary to standard output.
'''

import re

MINUTE_SECONDS = 60
HOUR_SECONDS = 60 * MINUTE_SECONDS
DAY_SECONDS = 24 * HOUR_SECONDS
WEEK_SECONDS = 7 * DAY_SECONDS
YEAR_SECONDS = 365 * DAY_SECONDS

uptime1 = 'twb-sf-881 uptime is 6 weeks, 4 days, 2 hours, 25 minutes'
uptime2 = '3750RJ uptime is 1 hour, 29 minutes'
uptime3 = 'CATS3560 uptime is 8 weeks, 4 days, 18 hours, 16 minutes'
uptime4 = 'rtr1 uptime is 5 years, 18 weeks, 8 hours, 23 minutes'

list_of_uptime = [uptime1, uptime2, uptime3, uptime4]

time_dict = {}
for uptime in list_of_uptime: #loop through list_of_uptime
	hostname,time_with_words = uptime.split(" uptime is ")
	time_with_words_split = time_with_words.split(",")

	uptime_seconds = 0
	for time in time_with_words_split:
		if "year" in time:
			(year,unneeded_info) = time.split(" year")
			try:
				uptime_seconds += int(year) * YEAR_SECONDS
			except ValueError as e:
				print "Error: Year was not an integer"
		elif "week" in time:
			(week,unneeded_info) = time.split(" week")
			try:
				uptime_seconds += int(week) * WEEK_SECONDS
			except ValueError as e:
				print "Error: Week was not an integer"
		elif "day" in time:
			time_split = time.split(" day")
			day,unneeded_info = time_split
			try:
				uptime_seconds += int(day) * DAY_SECONDS
			except ValueError as e:
				print "Error: Day was not an integer"
		elif "hour" in time:
			time_split = time.split(" hour")
			hour,unneeded_info = time_split
			try:
				uptime_seconds += int(hour) * HOUR_SECONDS
			except ValueError as e:
				print "Error: Hour was not an integer"
		elif "minute" in time:
			time_split = time.split(" minute")
			minute,unneeded_info = time_split
			try:
				uptime_seconds += int(minute) * MINUTE_SECONDS
			except ValueError as e:
				print "Error: Minute was not an integer"
			
	time_dict[hostname] = uptime_seconds

print time_dict
