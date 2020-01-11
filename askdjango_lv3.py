import re
import requests

url = 'http://askdjango.github.io/lv3/'
html = requests.get(url).text

#정규표현식에서 일부만 매칭되길 원하면 search
#정규표현식에서 전부를 매칭되길 원하면 match를 사용
#re.search(r'var courses = ();')
#끝에있는 () 부분을 뽑아내겠다는 뜻

matched = re.search(r'var courses = (.*);', html, re.S)