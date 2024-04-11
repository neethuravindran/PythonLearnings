
#Create a script called weather that return the environmental parameters (temperature
#(min, max), windspeed, humidity, cloud, pressure, sunrise and sunset) of any location you
#want; after passing arguments (like user api and city id).


from bs4 import BeautifulSoup
import urllib3
import requests
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
 
 
def weather(city):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    city = city.replace(" ", "+")
    res = requests.get(
        f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8', headers=headers, verify=False)
    print("Searching...\n")
    soup = BeautifulSoup(res.text, 'html.parser')
    print(soup.select('#wob_loc')
    
    location = soup.select('#wob_loc')[0].getText().strip()
    time = soup.select('#wob_dts')[0].getText().strip()
    info = soup.select('#wob_dc')[0].getText().strip()
    weather = soup.select('#wob_tm')[0].getText().strip()
    print(location)
    print(time)
    print(info)
    print(weather+"°C")
 
 
city = input("Enter the Name of City ->  ")
city = city+" weather"
weather(city)


