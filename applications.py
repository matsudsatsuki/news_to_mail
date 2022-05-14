from joblib import PrintTime
from matplotlib.pyplot import title
import requests
import pandas as pd
import streamlit as st
import numpy as np
import os
import urllib.request
import json
import configparser
import codecs
import requests
from bs4 import BeautifulSoup
import re
from newspaper import Article
import nltk
import time
import streamlit as st
#nltk.download('punkt')

option = ['business','technology','entertainment']
headers = {'X-Api-Key': 'a64fadec7ec7420cb83b631a2f1b203a'}
st.title('News Letter')
if st.button('メール送信'):
    for i in range(3):
        url = 'https://newsapi.org/v2/top-headlines'
        params = {
            'category' : option[i],
            'country' : 'jp',
            'pageSize' : 1
        }
        response = requests.get(url, headers=headers, params=params)
        pd.options.display.max_colwidth = 25
        if response.ok:
            data = response.json()
            df = pd.DataFrame(data['articles'])
            #print('totalResults:', data['totalResults'])

        #print(df[['publishedAt','title','url']])
        URL = df['url'][0]
        url1 = 'http://www8.kobe-np.co.jp/nie/2015/12/post-494.html'
        #url1 = 'https://news.yahoo.co.jp/pickup/6426184'
        article = Article(URL)
        article.download()
        article.parse()
        nltk.download('punkt')
        #print(article.text)
        text = article.text
        #print(df['url'])
        article.nlp()
        #f = open('example2.txt', 'w')
        #f.write(df['url'][0])
        #f.write(article.title)
        #f.write(article.text)

        from email.mime.text import MIMEText
        import smtplib

        # SMTP認証情報
        account = "junfulingmu374@gmail.com"
        password = "shinei3420"
        # 送受信先
        to_email = "junfulingmu374@gmail.com"
        from_email = "junfulingmu374@gmail.com"
        
        # MIMEの作成
        subject = "ニュース要約"
        message = df['url'][0]
        titles = article.title
        articles = article.text
        msg1 = MIMEText(message, "html")
        msg2 = MIMEText(titles, "html")
        msg3 = MIMEText(articles, "html")
        msg1["Subject"] = subject
        msg1["To"] = to_email
        msg1["From"] = from_email
        msg2["Subject"] = subject
        msg2["To"] = to_email
        msg2["From"] = from_email
        msg3["Subject"] = subject
        msg3["To"] = to_email
        msg3["From"] = from_email
        
        # メール送信処理
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(account, password)
        server.send_message(msg1)
        server.send_message(msg2)
        server.send_message(msg3)

        server.quit()
        if i == 2:
            st.write('Done!')


