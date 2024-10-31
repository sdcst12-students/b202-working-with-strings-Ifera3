#!python3
"""
##### Problem 2
Retrieve the contents of the sd.deltasd.bc.ca webpage.
Remove all of the HTML and display just the real contents of the page.
"""
import requests, time

pageHTML = requests.get("https://sd.deltasd.bc.ca/")
time.sleep(1)

#not reatrning anything past halfawy throgh the styles, no real contents of page returned

print(pageHTML.text)