import time
from datetime import datetime as dt

#host_path = "/etc/hosts"

hostfile_temp ="hostsfile_test"

redirect = "127.0.0.1"

website_list = ["https://facebook.com/", "https://www.linkedin.com/", "https://coinmarketcap.com/"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 15):
        print("Working hours...")
        with open(hostfile_temp, 'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+website+"\n")

    else:
        with open(hostfile_temp, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("Fun hours")
    time.sleep(5)



