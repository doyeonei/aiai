import requests
from bs4 import BeautifulSoup

# 넷플릭스 TOP 10 페이지 URL
url = "https://www.netflix.com/tudum/top10"

# User-Agent 설정
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

# 페이지 요청
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# 영화 정보 추출
movies = soup.select('div[data-uia="top10-item"]')
for idx, movie in enumerate(movies, 1):
    title = movie.select_one('p[data-uia="top10-title"]').get_text(strip=True)
    print(f"{idx}위: {title}")
