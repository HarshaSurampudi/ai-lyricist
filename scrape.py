import pandas as pd
import requests
from bs4 import BeautifulSoup
import urllib.parse
from tqdm import tqdm
import time

def scrape_lyrics(lyrics_page_url):
    response = requests.get(lyrics_page_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # h6 tag with id 'telguText'
    lryics = soup.find('h6', {'id': 'telguText'}).text.strip()
    # h6 tag with id 'englishText'
    lryics_en = soup.find('h6', {'id': 'englishText'}).text.strip()
    # span tag with id 'song_name'
    song_name = soup.find('span', {'id': 'song_name'}).text.strip()
    # span tag with id 'lyricistname'
    lyricist = soup.find('span', {'id': 'lyricistname'}).text.strip()
    # span tag with id 'signarname'
    singer = soup.find('span', {'id': 'signarname'}).text.strip()
    return {
        'song': song_name,
        'lyricist': lyricist,
        'singer': singer,
        'lyrics': lryics,
        'lyrics_en': lryics_en,
        'url': lyrics_page_url
    }


def get_albums(lyricist_page_url):
    response = requests.get(lyricist_page_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    #all a tags with href starting with 'https://www.lyricstape.com/album/'
    urls = [str(a['href']).strip() for a in soup.find_all('a', href=True) if a['href'].startswith('https://www.lyricstape.com/album/')]
    filtered_urls = [url for url in urls if len(urllib.parse.urlparse(url).path.split("/")) == 5]
    return filtered_urls


def get_songs(album_page_url):
    response = requests.get(album_page_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    #all a tags with href starting with 'https://www.lyricstape.com/album/'
    urls = [str(a['href']).strip() for a in soup.find_all('a', href=True) if a['href'].startswith('https://www.lyricstape.com/album/')]
    filtered_urls = [url for url in urls if len(urllib.parse.urlparse(url).path.split("/")) == 5]
    return filtered_urls


def scrape_album_lyrics(album_page_url):
    songs = get_songs(album_page_url)
    lyrics = []
    for song in songs:
        time.sleep(1)
        print("Scraping song: ", song)
        lyrics.append(scrape_lyrics(song))
    return lyrics



# Selecting Sirivennela Seetharama Sastry
lyricist_page_url = 'https://www.lyricstape.com/lyricist-details/1'

albums = get_albums(lyricist_page_url)


lyrics = []

for album in albums:
    time.sleep(1)
    print("Scraping album: ", album)
    lyrics.extend(scrape_album_lyrics(album))

df = pd.DataFrame(lyrics)

# Filter only Sirivennela Seetharama Sastry. Some albums have songs by other lyricists
df = df[df['lyricist'] == 'Sirivennela Seetharama Sastry']

df.to_csv('sirivennela_lyrics.csv', index=False)