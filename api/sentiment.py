from transformers import pipeline
from transformers import pipeline
class Sentiment:
    def __init__(self, label, score):
        self.label = label
        self.score = score

classifier = pipeline("sentiment-analysis", model="michellejieli/emotion_text_classifier")

def get_sentiment(text):


    result = classifier(text)

    for c in result:
        label=result['label']
        score=result['score']

    sentiment_obj = Sentiment(
        label=label,
        score=score
    )
    print(sentiment_obj)
    return(sentiment_obj)




get_sentiment("I love cheese")
