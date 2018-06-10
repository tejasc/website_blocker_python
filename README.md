## website_blocker_python

Python script to block website/urls during certain hours

# Run instructions
1. Using terminal: We need to run this script using sudo because hosts file needs admin permission to write.

      $ sudo python3 <pathToPythonFile>/website_blocker.py

2. Add this script to crontab table to execute when we start the computer.
  
      $ sudo crontab -e

      Add below to your crontab file at the end

      @reboot python3 <pathToPythonFile>/website_blocker.py

