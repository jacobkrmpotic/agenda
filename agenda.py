import sys
from time import time
from getpass import getuser

user = getuser()
if (user == "root"):
	print("It is not recommended to run this program as root.")
	print("An agenda file has been created for the root user; /root/.agenda")
	agenda_file = "/root/.agenda"
else:
	agenda_file = "/home/" + user + "/.agenda"

try:
	f = open(agenda_file, "r")
	text = f.read()
	f.close()
except FileNotFoundError:
	print("File: %s created" % agenda_file)
	f = open(agenda_file, "x")
	text = ""
	f.close()


# takes the current time in seconds and a past time in seconds (int)
# then returns a regular string like "5 seconds ago", "2 weeks ago", etc.
def time_ago(current, past):
	if (past > current): # if the variables are mixed up
		current, past = past, current

	t = int(current - past)
	if (t // 315360000 > 0):
		t //= 315360000
		st = "decades"
		if (t == 1): st = "decade"
		return "%d %s ago" % (t, st)
	elif (t // 31536000 > 0):
		t //= 31536000
		st = "years"
		if (t == 1): st = "year"
		return "%d %s ago" % (t, st)
	elif (t // 2592000 > 0):
		 t //= 2592000
		 st = "months"
		 if (t == 1): st = "month"
		 return "%d %s ago" % (t, st)
	elif (t // 604800 >	0):
		t //= 604800
		st = "weeks"
		if (t == 1): st = "week"
		return "%d %s ago" % (t, st)
	elif (t // 86400 > 0):
		t //= 86400
		st = "days"
		if (t == 1): st = "day"
		return "%d %s ago" % (t, st)
	elif (t // 3600 > 0):
		t //= 3600
		st = "hours"
		if (t == 1): st = "hour"
		return "%d %s ago" % (t, st)
	elif (t // 60 > 0):
		t //= 60
		st = "minutes"
		if (t == 1): st = "minute"
		return "%d %s ago" % (t, st)
	elif (t // 4 > 0):
		return "%d seconds ago" % t
	return "just now"
