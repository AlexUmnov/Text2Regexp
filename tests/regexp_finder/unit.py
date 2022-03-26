from regexp_finder.base import RegexpFinderBase

def test_regexp_match():
    finder = RegexpFinderBase(
        {
            "pos": "positive",
            "neg": "negative"
        }
    )

    texts = [
        "positive text",
        "negative text",
        "another positive text",
        "and another positive text",
        "and another negative text"
    ]

    predicted_labels = finder.predict(texts)
    assert predicted_labels == ['pos', 'neg', 'pos', 'pos', 'neg']