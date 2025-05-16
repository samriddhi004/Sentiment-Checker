from app.sentiment import analyze_sentiment


def test_positive_sentiment():
    assert analyze_sentiment("I love this!") == "positive"


def test_negative_sentiment():
    assert analyze_sentiment("I hate this.") == "negative"


def test_neutral_sentiment():
    assert analyze_sentiment("It is sunny today.") == "neutral"
