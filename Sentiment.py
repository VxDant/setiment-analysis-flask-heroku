# from email.mime import image
# import imp
import re
from collections import Counter
# import string
# from tkinter import Image
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
import datetime
# from PIL import Image


class Sentiment:

    def contentRegex(content):

        listOfReqSentimentalWords = []

        content = content.lower()

        content_re = re.sub('[""$#%&*()=:;''<>/|\!@?.,]', ' ', content)
        content_re = re.sub('\s+', " ", content_re)

        listOfTokenWords = word_tokenize(content_re, "english")

        for word in listOfTokenWords:
            if word not in stopwords.words('english'):
                listOfReqSentimentalWords.append(word)

        return content_re


    def tokenizationAndLemma(contentOutputAfterRegex):
        lis_words = word_tokenize(contentOutputAfterRegex, "english")
        final_words = []
        lemma_words = []
        for word in lis_words:
            if word not in stopwords.words('english'):
                final_words.append(word)

        for word in final_words:
            word = WordNetLemmatizer().lemmatize(word)
            lemma_words.append(word)
        return lemma_words


    def emotionsListMaker(lemma_words):
        emotionList = []

        with open('emotions.txt', 'r') as file1:
            for line in file1:
                clear_line = line.replace('\n', '').replace(
                    "'", "").replace(",", "").strip()
                word, emotion = clear_line.split(':')

                if word in lemma_words:
                    emotionList.append(emotion)

        return emotionList

    
    def CountingEmotions(emotionList):
        return Counter(emotionList)

    def plottingGraph(counter):
        ct = str(datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S'))
        fig, ax1 = plt.subplots()
        fig.autofmt_xdate()
        ax1.bar(counter.keys(), counter.values())
        # plt.savefig(f'graph.png')
        # f = plt.figure(fig,plt,format='png')
        # plt.close()



            

            

    def sentiment_analyse(regexOutput):
        score = SentimentIntensityAnalyzer().polarity_scores(regexOutput)
        if score['neg'] > score['pos']:
            return 'negative sentiment'
        elif score['neg'] < score['pos']:
            return("Positive Sentiment")
        else:
            return("Neutral Sentiment")


        
