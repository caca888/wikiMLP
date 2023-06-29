from src.wikinlplib import search_wikipedia, summarize_wiki, get_phrase

def test_search_wiki():
    assert 'Germany' in search_wikipedia("Germany")

def test_summarize_wiki():
    assert 'Germany, officially the Federal Republic of Germany,' in summarize_wiki("Germany")


def test_get_phrase():
    assert 'germany' in get_phrase("Germany")

