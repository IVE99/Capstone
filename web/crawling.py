"""
#from gensim.summarization.summarizer import summarize
from newspaper import Article
import requests
from bs4 import BeautifulSoup


url = 'https://media.naver.com/press/020' #동아일보

r = requests.get(url, headers={'User-Agent':'Mozilla/5.0'})
html = r.content
soup = BeautifulSoup(html, 'html.parser')
titles_html = soup.select('div.ofra_list_txwrap > div.ofra_list_tx > div.ofra_list_tx_headline')
imgs_html = soup.select('li.ofra_list_item > a > div.ofra_list_img > div > img')
url_html = soup.select('li.ofra_list_item > a')


titleArr = []    #주제
imgArr = []   #이미지 src
urlArr = []   #url
newsContent = []

#이미지 - url 길이 다름
for i in range(10):
    titleArr.append(titles_html[i].text)
    imgArr.append(imgs_html[i]['data-src'])
    urlArr.append(url_html[i]['href'])


    #print(titleArr[i])
    #print(imgArr[i])
    #print(urlArr[i])
    #print()

for j in range(10):
    news = Article(urlArr[j], language='ko')
    news.download()
    news.parse()
    #print(news.text)
    newsContent.append(news.text)



#print(len(titleArr), len(urlArr), len(imgArr))

#summArr = [] # 요약문 배열
#for k in range(10):
#    news = Article(urlArr[k], language='ko')
#    news.download()
#    news.parse()
    #summArr.append(summarize(news.text, ratio=0.1))
    #print(k,summArr[k])
    #print()



#print('!!!!!!!!!!!!!!!!!',summArr)

#news = Article(url_html, language='ko')
#news.download()
#news.parse()
#print(news.text)

# 문장 비율 설정
#summ = summarize(news.text, ratio=0.1)
#print('result',summ)
#summ = summarize(news.text, word_count=50)
"""