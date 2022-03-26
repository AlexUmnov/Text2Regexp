from abc import ABC, abcstractmethod, abstractmethod
from typing import List, Dict, Optional
from common.dataset import Dataset
import re

class RegexpFinderBase(ABC):
    def __init__(self, default_dict: Optional[Dict[str, str]] = {}) -> None:
        self._regexp_dict: Dict[str, str] = default_dict
    
    def get_regexp_dict(self) -> Dict[str, str]:
        return self._regexp_dict

    @abcstractmethod
    def fit(self, dataset: Dataset) -> None:
        return NotImplementedError

    def predict(self, texts: List[str]) -> List[str]:
        labels = []
        for text in texts:
            for cls, regexp in self._regexp_dict:
                if re.match(regexp, text):
                    labels.append(cls)
                    continue
        return labels