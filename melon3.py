import requests
from bs4 import BeautifulSoup
import random
import csv

# 멜론 차트 URL
url = 'https://www.melon.com/chart/index.htm'

# 헤더 설정
headers = {
    'User-Agent': 'Mozilla/5.0'
}

# 웹 요청
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

# 노래 정보 추출
songs = []
for entry in soup.select('tr.lst50, tr.lst100'):
    rank = entry.select_one('span.rank').get_text()
    title = entry.select_one('div.ellipsis.rank01 a').get_text()
    artist = entry.select_one('div.ellipsis.rank02 a').get_text()
    songs.append((rank, title, artist))

# 메뉴 출력
print("==========================")
print("1. 멜론 TOP100")
print("2. 멜론 TOP50")
print("3. 멜론 TOP10")
print("4. 노래 추천 기능")
print("5. TOP100 가수 검색")
print("6. 파일에 저장 (멜론TOP100)")
print("==========================")

n = input("메뉴를 입력하세요: ")

if n == "1":
    print("[멜론 TOP 100]")
    for song in songs:
        print(f"{song[0]}. {song[1]} - {song[2]}")

elif n == "2":
    print("[멜론 TOP 50]")
    for i in range(50):
        print(f"{songs[i][0]}. {songs[i][1]} - {songs[i][2]}")

elif n == "3":
    print("[멜론 TOP 10]")
    for i in range(10):
        print(f"{songs[i][0]}. {songs[i][1]} - {songs[i][2]}")

elif n == "4":
    print("[노래 추천 기능]")
    song = random.choice(songs)
    print(f"오늘의 추천곡: {song[1]} - {song[2]}")

elif n == "5":
    artist_name = input("검색할 가수 이름을 입력하세요: ")
    found = False
    for song in songs:
        if artist_name.lower() in song[2].lower():
            print(f"{song[0]}. {song[1]} - {song[2]}")
            found = True
    if not found:
        print("해당 가수가 TOP100에 없습니다.")

elif n == "6":
    filename = 'melon_top100.csv'
    with open(filename, 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.writer(f)
        writer.writerow(['순위', '곡명', '아티스트'])
        for song in songs:
            writer.writerow(song)
    print(f"{filename} 파일에 저장되었습니다.")
