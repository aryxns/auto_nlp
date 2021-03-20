from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from transformers import pipeline
#from sentiment import SentimentAnalysis
#sentiment_analysis = SentimentAnalysis()

def sentiment(txt, arg):
    if "vader" in arg.lower():
        answer = vader_sentiment(txt)
        return answer
    elif "bert" or "transformers" or "huggingface" in arg.lower():
        answer = transformers_sentiment(txt)
        return answer

#def emotion_sentiment(txt):
    sadness_score = sentiment_analysis.get_sadness_score() # get depression score.
    anger_score = sentiment_analysis.get_anger_score() # get anger score.
    anxiety_score = sentiment_analysis.get_anxiety_score() # get anxiety score.
    agony_score = sentiment_analysis.get_agony_score() # get agony score.
    embarrassed_score = sentiment_analysis.get_embarrassed_score() # get embarrassed score.
    happiness_score = sentiment_analysis.get_happiness_score() # get happiness score.
    result = {"sadness": sadness_score, "anger": anger_score, "anxiety": anxiety_score, "happiness":happiness_score, "embarrassed": embarrassed_score}
    return result

def transformers_sentiment(txt):
    text = txt
    sentiment_analysis = pipeline("sentiment-analysis")
    result = sentiment_analysis(text)[0]
    answer = ({"Label:": result['label'], "Confidence Score:": result['score']})
    return answer

#def pos_neg_sentiment(txt):
    positive_score = sentiment_analysis.get_positive_score(txt)
    negative_score = sentiment_analysis.get_negative_score(txt)
    return ({"Positive Score": positive_score, "Negative Score": negative_score})

def vader_sentiment(txt):
    analyzer = SentimentIntensityAnalyzer()
    vs = analyzer.polarity_scores(txt)
    return(txt, ({"pos":vs["pos"], "neg":vs["neg"], "neu":vs["neu"]}))