#!python3

"""
we can retrieve text from the www and store it into variables using request page
"""

import requests, time

x = requests.get("https://sd.deltasd.bc.ca")
time.sleep(1)
print(x.text)

"""
This will retrieve the entire webpage!

"""