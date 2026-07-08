import requests
import datetime as dt
from api_key import API_KEY

city = input("Enter City Name : ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

try:
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        
        print("================================")
        print(f"  🌤️  Weather Report — {city}")
        print("================================")
        print(f"Time         : {dt.datetime.now().strftime('%H:%M:%S')}")
        print(f"Date         : {dt.datetime.now().strftime('%d-%m-%Y')}")
        print(f"Temperature  : {data['main']['temp']}°C")
        print(f"Feels Like   : {data['main']['feels_like']}°C")
        print(f"Humidity     : {data['main']['humidity']}%")
        print(f"Condition    : {data['weather'][0]['description']}")
        print(f"Wind Speed   : {data['wind']['speed']} m/s")
        
        print("================================")
    else:
        if response.status_code ==404:
        	print(f"Error : City '{city}' not found. Check spelling and try again.")
        	
        elif response.status_code ==401:
        	print("Error : Invalid API Key.")
        	
        else:
        	print(f"Error: {response.status_code}")
        

except Exception as e:
    print(f"Error: {e}")