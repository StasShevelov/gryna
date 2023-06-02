from bs4 import BeautifulSoup
import requests
def link_name(l):

    
    response = requests.get(l)
    soup = BeautifulSoup(response.text, 'html.parser')
    try:
        return soup.title.text
    except:
        return soup.title

