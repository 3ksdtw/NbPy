import requests
from bs4 import BeautifulSoup

response = requests.get('http://askdjango.github.io/lv1/')

#응답 요청 OK한 코드를 텍스트로 변환해서 html에 저장
htmltotext = response.text

#응답받은 코드를 BS에 사용하기 위해 인스턴스 지정
bs = BeautifulSoup(htmltotext, 'html.parser')

#원하는 태그만 골라뽑기
for tag in bs.select('li[class=course]'):
    print(tag.text)