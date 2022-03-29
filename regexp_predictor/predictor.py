from typing import List, Dict, Optional
import re

class RegexpPredictor:
    def __init__(
        self, 
        default_dict: Optional[Dict[str, str]] = {}, 
        default_cls: Optional[str] = None
    ) -> None:
        self._regexp_dict: Dict[str, str] = default_dict
        self._default_cls = default_cls
    
    def get_regexp_dict(self) -> Dict[str, str]:
        return self._regexp_dict

    def predict(self, texts: List[str]) -> List[str]:
        labels = []
        for text in texts:
            for cls, regexp in self._regexp_dict.items():
                if re.search(regexp, text):
                    labels.append(cls)
                    break
            else:
                labels.append(self._default_cls)
        return labels