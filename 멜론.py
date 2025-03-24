import requests
from bs4 import BeautifulSoup

# 멜론 차트 URL
url = "https://www.melon.com/chart/day/index.htm"

# User-Agent 설정 (봇 차단 우회)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Referer": "https://www.melon.com/"
}

# 요청 보내기
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# 노래 정보 가져오기
songs = soup.select('tr[data-song-no]')
for song in songs:
    rank = song.select_one('span.rank').get_text(strip=True)
    title = song.select_one('div.ellipsis.rank01 > span > a').get_text(strip=True)
    artist = song.select_one('div.ellipsis.rank02 > a').get_text(strip=True)
    album = song.select_one('div.ellipsis.rank03 > a').get_text(strip=True)
    print(f"{rank}위: {title} - {artist} ({album})")