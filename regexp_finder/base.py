from abc import abstractclassmethod, ABC
from common.dataset import Dataset
from typing import List
from regexp_predictor.predictor import RegexpPredictor

class RegexpFinderBase(ABC):
    """
    Base class for regexp finder classes
    This class is aimed at finding regexps for proper classification of texts
    """
    @abstractclassmethod
    def fit(self, dataset: Dataset) -> None:
        """Searches for regexps based on the dataset"""
        raise NotImplemented

    @abstractclassmethod
    def predict(self, texts: List[str]) -> List[str]:
        """Predicts classes for given texts"""
        raise NotImplemented
