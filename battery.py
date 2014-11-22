#!/usr/bin/env python

import commands
import pynotify
import os
from threading import Timer


def battery_state():

	battDir = "/proc/acpi/battery/BAT1/"

	if os.path.exists(battDir):
		rem = float(commands.getoutput("grep \"^remaining capacity\" /proc/acpi/battery/BAT1/state | awk '{ print $3 }'"))
		full = float(commands.getoutput("grep \"^last full capacity\" /proc/acpi/battery/BAT1/info | awk '{ print $4 }'"))
		state = commands.getoutput("grep \"^charging state\" /proc/acpi/battery/BAT1/state | awk '{ print $3 }'")
		rate = float(commands.getoutput("grep \"^present rate\" /proc/acpi/battery/BAT1/state | awk '{ print $3 }'"))

		time_left = rem / rate
		time_left = round(time_left, 2)
		percentage = int((rem/full) * 100)

		if state == "discharging":
			pynotify.init("Battery Alert!")
			notify = pynotify.Notification("Battery state: -> "+state,str(percentage)+"% "+ str(time_left)+" hours rem","/usr/share/icons/gnome/32x32/status/battery-low.png")
			notify.show()
		elif state == "charging":
			pynotify.init("Battery charging!")
			notify = pynotify.Notification("Battery "+state, str(percentage)+"%", "/usr/share/icons/gnome/32x32/status/weather-few-clouds-night-350.png")
			notify.show()
		

		if percentage == 100:
			notify = pynotify.Notification("Battery charged:)"+state, str(percentage)+"%", "/usr/share/icons/gnome/32x32/status/battery-full.png")
			notify.show()
			#cut current flow to PC
			pass
		elif percentage <= 10:
			notify = pynotify.Notification("Battery "+state, str(percentage)+"%", "/usr/share/icons/gnome/32x32/status/battery-empty.png")
			notify.show()
			#allow flow of current
			pass

		refreshRate = Timer(3.0, battery_state)
		refreshRate.start()

	else:
		rem = float(commands.getoutput("grep \"^remaining capacity\" /proc/acpi/battery/BAT0/state | awk '{ print $3 }'"))
		full = float(commands.getoutput("grep \"^last full capacity\" /proc/acpi/battery/BAT0/info | awk '{ print $4 }'"))
		state = commands.getoutput("grep \"^charging state\" /proc/acpi/battery/BAT0/state | awk '{ print $3 }'")

		percentage = int((rem/full) * 100)

		if state == "discharging":
			pynotify.init("Battery Alert!")
			notify = pynotify.Notification("Battery state: -> "+state,str(percentage)+"%","/usr/share/icons/gnome/32x32/status/battery-low.png")
			notify.show()
		elif state == "charging":
			pynotify.init("Battery charging!")
			notify = pynotify.Notification("Battery "+state, str(percentage)+"%", "/usr/share/icons/gnome/32x32/status/weather-few-clouds-night-350.png")
			notify.show()
		

		if percentage == 100:
			notify = pynotify.Notification("Battery charged:)"+state, str(percentage)+"%", "/usr/share/icons/gnome/32x32/status/battery-full.png")
			notify.show()
			#cut current flow to PC
			pass
		elif percentage <= 10:
			notify = pynotify.Notification("Battery "+state, str(percentage)+"%", "/usr/share/icons/gnome/32x32/status/battery-empty.png")
			notify.show()
			#allow flow of current
			pass

		refreshRate = Timer(3.0, battery_state)
		refreshRate.start()

if __name__ == "__main__": battery_state()

















