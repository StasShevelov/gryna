import requests
from bs4 import BeautifulSoup as b4
def search(p):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
    }
    res = requests.get(
        
        headers=headers
    )
    soup = b4(res.text, "html.parser")
    time = soup.select("#wob_dts")[0].getText().strip()
    rain = soup.select("#wob_pp")[0].getText().strip()
    weather = soup.select("#wob_tm")[0].getText().strip()
    sun = soup.select("#wob_dc")[0].getText().strip()
    results = {"time": time, "rain": rain, "weather": weather, "sun": sun}
    return results