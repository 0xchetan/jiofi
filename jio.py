import requests
from bs4 import BeautifulSoup
import re

page = requests.get('http://jiofi.local.html/#')

soup = BeautifulSoup(page.text, 'html.parser')

batterylevel = soup.find("input", {"id": "batterylevel"})['value']
batterystatus = soup.find("input", {"id": "batterystatus"})['value']

print('Your Device: JioFi 4')
print("Battery Level: "+batterylevel)
print("Battery Status: "+batterystatus)

numbers = re.findall('\d+',batterylevel)

if int(numbers[0])<10 and batterystatus != "Charging":
    print("Please connect the charger")
elif int(numbers[0])==100:
    print("Device Fully Charged.")


