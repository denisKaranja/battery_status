import sys
from time import sleep

batt_state_file = "/proc/acpi/battery/BAT1/state"

print "Monitoring battery status. Press <Ctrl>+C to exit."

try:
  with open(batt_state_file) as state:
    while True:
      state.seek(0)
      for line in state:
        data = line.split(":")[1].strip().split(" ")[0]
	if "present rate" in line:
	  rate = int(data)
	elif "remaining" in line:
	  remaining = int(data)
     
      time_left = (remaining * 0.1) / state
      hours = int(time_left)
      minutes = int((time_left - hours) * 60)
      print "\rRemaining time left: %d hours %d minutes." % (hours, minutes)

      sys.stdout.flush()
      sleep(1)

except KeyboardInterrupt:
  print "\nCtrl+C presses. Exiting..."
