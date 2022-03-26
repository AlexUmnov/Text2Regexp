from dataclasses import dataclass
from typing import List
from pathlib import Path


@dataclass
class Dataset:
    texts: List[str]
    labels: List[str]

    @classmethod
    def from_imdb_dataset(cls, imdb_dataset_path: Path) -> 'Dataset':
        if not isinstance(imdb_dataset_path, Path):
            imdb_dataset_path = Path(imdb_dataset_path)
        assert (imdb_dataset_path / 'pos').is_dir(), f'No pos dir in {imdb_dataset_path}'
        assert (imdb_dataset_path / 'neg').is_dir(), f'No neg dir in {imdb_dataset_path}'
        texts, labels = [], []
        for label in ('pos', 'neg'):
            label_dir = imdb_dataset_path / label
            for review in label_dir.iterdir():
                texts.append(
                    review.read_text()
                )
                labels.append(label)
        return Dataset(
            texts=texts,
            labels=labels
        )

    def __str__(self) -> str:
        return f"texts: {self.texts[:2]}...\nlabels: {self.labels[:2]}..."
    
    def __repr__(self) -> str:
        return self.__str__()

