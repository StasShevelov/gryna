import requests
from bs4 import BeautifulSoup
import parser2

def search(m):
    url = "https://www.google.com/search"
    params = {"q": m}  # add "hl":"en" to get english results
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0"
    }
    soup = BeautifulSoup(
        requests.get(url, params=params, headers=headers).content, "html.parser"
    )

    results = []
    for a in soup.select("a:has(h3)"):
        href_link = a["href"] 
        print(href_link)
        if "search?q=" in a["href"]:
            print("no")
        else:
            results.append(f"""<div class="result-item"><h2 class='result-title' >{parser2.link_name(href_link)}</h2>
                            <a href= '{href_link}' class="result-url" style="color: white">{href_link}</a>
                            </div>""")
    
        
            
    return "".join(results)

