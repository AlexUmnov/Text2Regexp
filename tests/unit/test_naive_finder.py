from regexp_finder.naive import NaiveRegexpFinder
from common.dataset import Dataset 

def test_get_unique_chars():
    finder = NaiveRegexpFinder()
    mock_dataset = Dataset(
        texts=['i am a text', 'a test is me'],
        labels=['label', 'label']
    )
    true_char_set = set(['i', ' ', 'a', 'm', 't', 'e', 'x', 's'])
    assert finder._get_unique_chars(mock_dataset) ==  true_char_set