from src.wikinlplib import search_wikipedia, summarize_wiki, get_phrase, preprocess, conclude_text, get_sentiment
import numpy as np

def test_search_wiki():
    assert 'Germany' in search_wikipedia("Germany")

def test_summarize_wiki():
    assert 'Germany, officially the Federal Republic of Germany,' in summarize_wiki("Germany")


def test_get_phrase():
    assert 'germany' in get_phrase("Germany")


def test_preprocess():
    assert "@user haha http I am so happy" in preprocess("@user haha https://okdocky.com I am so happy")


def test_conclude_text():
    assert "Germany, officially the Federal Republic of Germany" in conclude_text("Germany")

def test_get_sentiment():
    np.testing.assert_array_equal([2,1,0], get_sentiment("Germany")) 