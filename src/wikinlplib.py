from textblob import TextBlob
import wikipedia
from transformers import AutoModelForSequenceClassification
from transformers import AutoTokenizer, AutoConfig
from transformers import pipeline
import numpy as np
from scipy.special import softmax


def search_wikipedia(name):
    """Search wikipedia"""
    print(f"Searching for {name}")
    return wikipedia.search(name)


def summarize_wiki(name):
    """Summarize wikipedia"""
    print(f"Printing wikipedia summary for {name}")
    return wikipedia.summary(name)


def get_text_blob(text):
    """Get text blob and returns"""
    print("Getting text blob")
    blob = TextBlob(text)
    return blob


def get_phrase(name):
    """Find wikipedia name and return back phrases"""
    text = summarize_wiki(name)
    blob = get_text_blob(text)
    phrases = blob.noun_phrases
    return phrases

def preprocess(text):
    new_text = []
    cnt = 1
    for t in text.split(" "):
        t = '@user' if t.startswith('@') and len(t) > 1 else t
        t = 'http' if t.startswith('http') else t
        new_text.append(t)
        cnt = cnt + 1
        if cnt > 500: continue
    return " ".join(new_text)

def conclude_text(name):
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    text = summarizer(summarize_wiki(name), max_length=130, min_length=30, do_sample=False)
    return text[0]['summary_text']

def get_sentiment(name):
    # pylint: disable=W1309
    MODEL = f"cardiffnlp/twitter-roberta-base-sentiment-latest"
    tokenizer = AutoTokenizer.from_pretrained(MODEL)
    config = AutoConfig.from_pretrained(MODEL)

    model = AutoModelForSequenceClassification.from_pretrained(MODEL)
    encoded_input = tokenizer(preprocess(conclude_text(name)), return_tensors='pt')
    output = model(**encoded_input)
    scores = output[0][0].detach().numpy()
    scores = softmax(scores)

    ranking = np.argsort(scores)
    ranking = ranking[::-1]
    for i in range(scores.shape[0]):
        l = config.id2label[ranking[i]]
        s = scores[ranking[i]]
        print(f"{i+1}) {l} {np.round(float(s), 4)}")
    return ranking