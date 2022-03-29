from regexp_predictor import RegexpPredictor

def test_regexp_match():
    default_cls = 'neg'

    finder = RegexpPredictor(
        default_dict={
            "pos": "positive",
            "neg": "negative"
        },
        default_cls=default_cls
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
    assert predicted_labels == ['pos', 'neg', 'pos', 'pos', 'neg', default_cls]