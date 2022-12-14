# from fileinput import filename
# from http import client
# from re import X
# from unittest import result
from flask import Flask, jsonify
from flask import send_file
from SavingImage import ImageDictionary
# from pymongo import MongoClient

from Sentiment import Sentiment
import nltk
from flask import Response
import io

# import datetime

#mongodb+srv://vedant:vedantserver@cluster0.mvtfwnx.mongodb.net/?retryWrites=true&w=majority

app = Flask(__name__)

# cluster = MongoClient('mongodb+srv://vedant:vedantserver@cluster0.mvtfwnx.mongodb.net/?retryWrites=true&w=majority')

# db = cluster["sentimentanalysis"]
# collection = db["imagesdb"]

# collection.insert_one({"reqImage": "new"})



nltk.download('vader_lexicon')
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('all')

@app.route('/home')
def home_screen():
    return "welcome"

@app.route('/1406/<string:n>')
def sentimentAnalysisOfEssayInput(n):
    essayInput = str(n)
    RegexOutput = Sentiment.contentRegex(essayInput)
    tokenization = Sentiment.tokenizationAndLemma(RegexOutput)
    emotionList = Sentiment.emotionsListMaker(tokenization)
    counterResult = Sentiment.CountingEmotions(emotionList)
    PositiveNeutralOrNegative = Sentiment.sentiment_analyse(RegexOutput)

    fileName = Sentiment.plottingGraph(counterResult)
    ImageDictionary.dict1.clear()
    ImageDictionary.dict1['1'] = fileName

    result = {"initialEssay": essayInput,

              "finalAfterRegex": (str(RegexOutput)),

              "emotionsPresent": emotionList,

              "tokenizationOutput": tokenization,

              "counterResult": counterResult,

              "NatureOfSentiment": PositiveNeutralOrNegative,

              }

    return jsonify(result)
    # return send_file(fileName, mimetype='Image/png')


@app.route('/2906/image')
def SentimentAnalysisImage():

    x = ImageDictionary.dict1['1']

    # with open(f'graph.png') as  file1:
    #     file1.name
    return Response(x,mimetype='image/png')
    # return send_file('graph.png', mimetype='image/png')


if __name__ == "__main__":
    app.run(debug=True)
