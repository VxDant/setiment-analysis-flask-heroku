from fileinput import filename
from http import client
from re import X
from unittest import result
from flask import Flask, jsonify
from flask import send_file
from pymongo import MongoClient

from Sentiment import Sentiment

import datetime

#mongodb+srv://vedant:vedantserver@cluster0.mvtfwnx.mongodb.net/?retryWrites=true&w=majority

app = Flask(__name__)

# cluster = MongoClient('mongodb+srv://vedant:vedantserver@cluster0.mvtfwnx.mongodb.net/?retryWrites=true&w=majority')

# db = cluster["sentimentanalysis"]
# collection = db["imagesdb"]

# collection.insert_one({"reqImage": "new"})


@app.route('/1406/<string:essayInput>')
def sentimentAnalysisOfEssayInput(essayInput):

    RegexOutput = Sentiment.contentRegex(essayInput)
    tokenization = Sentiment.tokenizationAndLemma(RegexOutput)
    emotionList = Sentiment.emotionsListMaker(tokenization)
    counterResult = Sentiment.CountingEmotions(emotionList)
    PositiveNeutralOrNegative = Sentiment.sentiment_analyse(RegexOutput)
    # fileName = Sentiment.plottingGraph(counterResult)

    result = {"initialEssay": essayInput,

              "finalAfterRegex": (str(RegexOutput)),

              "emotionsPresent": emotionList,

              "tokenizationOutput": tokenization,

              "counterResult": counterResult,

              "NatureOfSentiment": PositiveNeutralOrNegative,

              }

    return result
    # return send_file(fileName, mimetype='Image/png')


@app.route('/image')
def SentimentAnalysisG():
    # with open(f'graph.png') as  file1:
    #     file1.name
    
    return send_file('graph.png', mimetype='image/png')


if __name__ == "__main__":
    app.run(debug=True)
