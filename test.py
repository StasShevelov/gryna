from pytube import YouTube
import requests
from bs4 import BeautifulSoup

session = requests.Session()

# get the page that contains the video
url = 'https://www.youtube.com/watch?v=8O4uvi8vZnI'
page = session.get(url)

# parse the page and extract the age restricted token
soup = BeautifulSoup(page.text, 'html.parser')
token = soup.find('input', {'name': 'xsrftoken'})['value']

# log in to youtube using your credentials and the session object
login_data = {
    'session_token': token,
    'action_login': 'Log In',
    'username': 'your_username',
    'password': 'your_password',
}
session.post('https://accounts.google.com/signin/challenge/sl/password',
             data=login_data)

# create a YouTube object and pass the session cookies
yt = YouTube(url, cookies=session.cookies.get_dict())

# print available video streams
print(yt.streams.filter(progressive=True))