from flask import Flask, redirect,render_template, request
from flask_socketio import SocketIO, send
from subprocess import call
import requests
from result_test import summarize, summary
#from crawling import titleArr, imgArr, urlArr, newsContent
from crawling2 import titleArr2, contentArr2, imgArr2, urlArr2, newsContent2
#from practice2 import summaries, summarize_news_articles
#from practice import summary, summarize

app = Flask(__name__)

'''
@app.route("/", methods=['GET','POST'])
def hello_world():

    if request.method == 'POST':
        value = request.form['input-box']
        value = str(value)
        #print('--------------------------')
        #print(value)
    else:
        value = ''

    #resultSumm = summarize(value)
    #resultSumm = summarize_news_articles(value)
    resultSumm = summarize(value)

    newsSumm = []
    #for i in range(4):
        #newsSumm.append(summarize(newsContent[i]))
        #print(newsSumm[i])
        #print()

    return render_template('index.html', value = value,  titleArr2 = titleArr2, imgArr2 = imgArr2, urlArr2 = urlArr2, resultSumm = resultSumm)
'''

@app.route("/article", methods=['GET','POST'])
def articlePage():

    #newsSumm2 = []
    #for i in range(len(titleArr2)):
        #newsSumm2.append(summarize(newsContent2[i]))
        #print(newsSumm[i])
        #print()

    #print(newsSumm2)
    
    return render_template('article.html', titleArr2 = titleArr2, contentArr2 = contentArr2, imgArr2 = imgArr2, urlArr2 = urlArr2, summary = summary)



@app.route("/chat", methods=['GET','POST'])
def chatPage():
   
    value = ''
    chatSumm = ''
    if request.method == 'POST':
        value = request.form['reply-text']
        #value = request.form['aa']
        value = str(value)
        print('--------------------------')
        print(value)
        chatSumm = summarize(value)
        print('chatSumm: ', chatSumm)




    #chatSumm = summarize(msg)

    return render_template('chat.html',chatSumm = chatSumm, value = value)


@app.route("/", methods=['GET','POST'])
def homePage():

  
    
    return render_template('home.html')




if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=80)
