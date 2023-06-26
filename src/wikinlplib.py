from textblob import TextBlob
import wikipedia


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