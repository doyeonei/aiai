import requests
from bs4 import BeautifulSoup

# 네이버 뉴스 URL
url = "https://news.naver.com/"

# 페이지 요청
response = requests.get(url)

# 응답 받은 HTML을 BeautifulSoup으로 파싱
soup = BeautifulSoup(response.text, 'html.parser')

# 뉴스 제목 가져오기 (주요 뉴스는 <ul> 태그 안에 <a> 태그로 표시됨)
news_list = soup.select('ul.headline_list a')

# 상위 10개 뉴스 정보 출력
print("Naver News Top 10:\n")
for idx, news in enumerate(news_list[:10], 1):
    title = news.text.strip()  # 뉴스 제목
    print(f"{idx}. {title}")
