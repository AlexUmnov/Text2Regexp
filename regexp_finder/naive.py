from regexp_finder.base import RegexpFinderBase
from common.dataset import Dataset
from typing import Set, List

class NaiveRegexpFinder(RegexpFinderBase):
    """Naively searches for regexps for classification"""
    def __init__(self, max_regexp_length: int = 32) -> None:
        super().__init__()

    def _get_unique_chars(self, dataset: Dataset) -> Set[str]:
        chars_set = set()
        for text in dataset.texts:
            chars_set.update(text)
        return chars_set

    def fit(self, dataset: Dataset) -> None:
        """Searches for regexps based on the dataset"""
        raise NotImplemented

    def predict(self, texts: List[str]) -> List[str]:
        """Predicts classes for given texts"""
        raise NotImplemented