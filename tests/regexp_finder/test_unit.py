from regexp_finder.base import RegexpFinderBase

def test_regexp_match():
    finder = RegexpFinderBase(
        default_dict={
            "pos": "positive",
            "neg": "negative"
        },
        default_cls='neg'
    )

    texts = [
        "positive text",
        "negative text",
        "another positive text",
        "and another positive text",
        "and another negative text",
        "a text without matches"
    ]

    predicted_labels = finder.predict(texts)
    assert predicted_labels == ['pos', 'neg', 'pos', 'pos', 'neg', 'neg']