from urllib.request import urlopen
from bs4 import BeautifulSoup

'''
추가할 것 
1) 대학명 검색 -> 각각의 targetUrl로
'''

# 크롤링하고자 하는 url
targetUrl = "http://addon.jinhakapply.com/RatioV1/RatioH/Ratio11080161.html?1537707368320"

soupData = BeautifulSoup(urlopen(targetUrl).read(), 'html.parser')

# 크롤링으로 얻을 data 저장
data = []

# div 태그를 가진 코드를 전부 찾는다
divs = soupData.find_all("div")

# 각 div 태그 안, tr과 td 찾기
for div in divs:
    for tr in soupData.find_all("tr",{"onmouseover" : "this.className='over';"}):
        tds = list(tr.find_all("td"))
        for td in tds:
            # 단과대학 포함된 경우
            if '대학' in tds[0].text.strip() and len(tds) >=5:
                # 학과명
                displayName = tds[1].text.strip()
                # 모집인원
                mojip = tds[2].text.strip()
                # 지원인원
                jiwon = tds[3].text.strip()
                # 경쟁률
                ratio = tds[4].text.strip()

            # 단과대학 포함되지 않은 경우
            elif '대학' not in tds[0].text.strip() and len(tds) >= 4:
                displayName = tds[0].text.strip()
                mojip = tds[1].text.strip()
                jiwon = tds[2].text.strip()
                ratio = tds[3].text.strip()
            # 모집인원/ 경쟁률 합쳐진 경우 + 단과대 포함
            elif '대학' in tds[0].text.strip() and len(tds)>=3:
                displayName = tds[1].text.strip()
                mojip = " "
                jiwon = tds[2].text.strip()
                ratio = " "
            # 모집인원/ 경쟁률 합쳐진 경우 + 단과대 포함 X
            elif '대학' not in tds[0].text.strip() and len(tds)>=2:
                displayName = tds[0].text.strip()
                mojip = " "
                jiwon = tds[1].text.strip()
                ratio = " "
        data.append([displayName, mojip, jiwon, ratio])

for i in range(0,len(data)):
    print(data[i])
# file로 저장
f = open("ratioInfo.txt",'w')
f.close
for i in data:
    f.write('{0},{1},{2},{3}\n'.format(i[0],i[1],i[2],i[3]))
#print(data)
