import requests
from bs4 import BeautifulSoup as b4
def weather_check(city):
    headers = {
      
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
    }
    
    res = requests.get(
        f"https://www.google.com/search?q={city}&oq={city}&aqs=chrome..69i57j0i10i512j0i10i457i512j0i10i512l7.5116j1j7&sourceid=chrome&ie=UTF-8",
        headers=headers
    )
    soup = b4(res.text, "html.parser")
    time = soup.select("#wob_dts")[0].getText().strip()
    rain = soup.select("#wob_pp")[0].getText().strip()
    weather = soup.select("#wob_tm")[0].getText().strip()
    sun = soup.select("#wob_dc")[0].getText().strip()
    print(f"""
    ВРЕМЯ: {time}\n
    ОСАДКИ: {rain}\n
    ПОГОДА: {weather} градусов цельсия
        {sun}""")



city = input("ВВЕДИ ГОРОД: ")
weather_check(f"{city} погода")