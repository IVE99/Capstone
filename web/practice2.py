"""
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import nltk
nltk.download('punkt')

tokenizer = AutoTokenizer.from_pretrained("lcw99/t5-large-korean-text-summary")
model = AutoModelForSeq2SeqLM.from_pretrained("results_t5")
"""

text = """
오늘(31일)부터 금융 소비자가 영업점을 방문하지 않고도 대출비교 플랫폼을 이용해 온라인에서 '원스톱'으로 대출을 갈아탈 수 있는 '대환대출 인프라'가 출범한다. 온라인에서 클릭 몇 번 만으로 금리가 저렴한 상품을 비교할 수 있게 되면서 금융권에서의 금리 경쟁이 치열해질 전망이다.

31일 금융권에 따르면 이날부터 1·2금융권의 53개 금융회사가 대환대출 인프라에 참여한다. 은행 19곳, 저축은행 18곳, 카드 7곳, 캐피탈 9곳 등이다. 토스, 카카오페이, 네이버파이낸셜 등 23개 대출비교 플랫폼 업체도 참여한다.

김소영 금융위원회 부위원장은 전날 서울 종로구 정부서울청사에서 열린 온라인·원스톱 대환대출 인프라 개시 브리핑에서 "정부는 지난해부터 비상경제민생회의 등을 통해 고금리 시기 국민이 실질적으로 체감할 수 있는 생활공감형 정책 마련에 주력해 왔다"며 "금융위는 그동안 금융감독원, 금융결제원, 주요 금융회사, 핀테크사와 함께 국민이 간편하게 더 낮은 금리로 이동할 수 있는 대환대출 인프라를 구축해 왔다"고 말했다.

'대환대출 인프라'는 영업점 방문 없이 차주가 유리한 대출 상품으로 쉽게 갈아탈 수 있도록 한 서비스다. 금융위원회에 따르면 이날부터 금융소비자는 금융회사 영업점을 방문하지 않고도 스마트폰을 이용해 기존에 받은 신용대출을 더 유리한 조건으로 갈아탈 수 있다. 온라인‧원스톱 대출 갈아타기는 스마트폰 앱으로 이용이 가능하다.

다만 대출 비교 플랫폼 앱과 주요 금융 회사 앱별로 제공하는 서비스가 다를 수 있어 확인이 필요하다. 대출 비교 플랫폼과 주요 금융 회사 앱에서 다른 금융사의 상품과 금리 등을 비교·확인할 수는 있지만 '갈아타기'는 대출 비교 플랫폼 앱에서만 가능하다. 특정 금융회사 앱에서는 해당 금융회사의 다른 대출 상품으로만 갈아탈 수 있다.

이날 기준 서비스 개시가 가능한 플랫폼은 네이버페이, 뱅크샐러드, 카카오페이, 토스, 핀다, KB국민카드, 웰컴저축은행 등 7개다. 금융사 앱에서 기존 대출조회가 가능한 53개 금융회사는 은행 19곳 전체, 저축은행 18곳, 카드사 7곳, 캐피탈사 9곳 등이다. 금융위는 향후 금융회사들이 플랫폼을 통한 고객유치 경쟁에 적극 참여할 것으로 보고 있다.

서비스 이용 시간은 은행 영업시간인 오전 9시부터 오후 4시(영업일 기준)까지다. 서비스 가능 횟수는 제한이 없다. 다만 중도상환수수료가 없는 대출의 경우 대출계약을 실행한 지 6개월이 경과한 이후에만(오프라인은 미해당) 이용 가능하다.

대환 서비스 이용이 가능한 상품은 53개 금융회사에서 받은 10억 이하의 기존 대출 중 직장인대출과 마이너스통장 등 보증이나 담보가 없는 신용대출이다. 기존 대출에서 갈아탈 수 있는 새로운 대출 역시 동일하다. 다만 기존 대출을 새희망홀씨 등 서민·중저신용자 대상 정책대출로 갈아타는 것은 보증 여부와 관계없이 가능하다.

카드론(장기카드대출)의 경우 대출 비교 플랫폼에서는 오는 7월 1일부터, 각 카드사 별 앱에서는 이날부터 가능하다. 연체대출 또는 법률분쟁, 압류와 거래정지 상태의 대출 등은 갈아탈 수 없다.
금융권에서는 자사 대출로 고객을 끌어들이기 위해 분주한 모습이다. KB국민은행, 신한은행, 하나은행은 대환대출 인프라 전용 상품을 출시할 계획이다. 우리은행은 기존 타행 대출을 자사 대출로 갈아타는 고객에게 6월 말까지 중도상환 해약금과 인지세 등 대출 거래 비용을 최대 10만 원까지 지원하기로 했다.

핀테크 회사들도 금리인하나 대출 비교 기능 강화 등으로 경쟁에 불을 붙이고 있다. 네이버페이를 운영하는 네이버파이낸셜은 '네이버페이 대출 갈아타기' 개시를 예고하며 '전 국민 이자 지원 이벤트' 사전신청 접수를 시작했다. 네이버페이에서 대출을 갈아타는 모든 이용자에게 '이자 지원 포인트 티켓'을 제공한다. 뱅크샐러드는 대환대출 서비스의 모든 대출 상품에 대해 0.1%포인트 추가 금리 인하를 지원하기로 했다.

카카오페이는 대환대출 플랫폼 중 유일하게 KB국민은행·신한은행·우리은행·하나은행·NH농협은행 등 5대 은행을 모두 입점시켰다. 지난 10일 사전신청을 받기 시작한 토스에는 2주만에 30만 명이 넘는 신청자가 몰렸다. 핀다도 사전신청에 하루 평균 4000여 명이 몰렸다.

시장에서는 온라인으로 쉽게 대환대출이 가능해지면서 금융사별 금리 경쟁이 치열해지는 만큼 금리 인하 효과가 있을 것으로 보고 있다.

김 부위원장은 "개시 초반에는 작년에 고금리 대출을 받은 차주가 상대적으로 낮아진 금리로 이동하고 2금융권 고신용자가 1금융권 중금리 상품으로 이동하는 경우 등을 중심으로 이자경감 혜택이 있을 것으로 기대된다"며 "핀테크사, 금융회사가 운영하는 플랫폼 모두 6월 이후 서비스를 추가 개시함에 따라 플랫폼 간 경쟁 역시 확대될 것으로 기대된다"고 말했다.
"""

"""
import re
import emoji
from unidecode import unidecode
import numpy as np

#remove html tags
def removeHTML(x):
    html=re.compile(r'<.*?>')
    return html.sub(r'',x)
    

def dataPreprocessing(x):
    x = removeHTML(x)
    x = emoji.demojize(x, delimiters=(" ", " "))
    x = re.sub(r'[^ 가-힣A-Za-z0-9\'.,?!/\n\r()%\[\]\-+~$&"]·', '', x)
    x = re.sub(r'[ ]+', ' ', x) # 공백 두칸 이상 지우기
    x = x.strip()
    return x

from kss import split_sentences

refine= split_sentences(text)

def listToString(str_list):
    result = ""
    for s in str_list:
        result += s + "\n"
    return result.strip()
i=0
for i in range(len(refine)):
  refine[i]=dataPreprocessing(refine[i])
  
result = listToString(refine)

#len(result)
max_input_length = 1024

inputs = tokenizer(result, max_length=max_input_length, truncation=True, return_tensors="pt")
output = model.generate(**inputs, num_beams=4, do_sample=True, min_length=10, max_length=256)
decoded_output = tokenizer.batch_decode(output, skip_special_tokens=True)[0]
predicted_title = nltk.sent_tokenize(decoded_output.strip())[0]

print(predicted_title)


from crawling2 import newsContent2
def summarize_news_articles(articles):
    summaries = []
    for article in articles:
        inputs = tokenizer.encode("summarize: " + article, return_tensors="pt")
        outputs = model.generate(inputs, max_length=256, num_beams=8, early_stopping=True)
        summary = tokenizer.decode(outputs[0], skip_special_tokens=True)
        summaries.append(summary)
    return summaries



# 뉴스 기사 요약
summaries = summarize_news_articles(newsContent2)

# 요약문 출력
#for i, summary in enumerate(summaries):
#    print(f"Summary {i+1}: {summary}")


"""