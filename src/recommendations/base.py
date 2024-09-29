from abc import ABC, abstractmethod
import numpy as np

class BaseRecommender(ABC):
    def __init__(self, data_corpus: np.ndarray):
        assert isinstance(data_corpus, np.ndarray), "`data_corpus` must be a numpy array"
        assert data_corpus.ndim == 2, "`data_corpus` must be a 2D array of N x M dimensions"
        self.data_corpus = data_corpus
    
    @abstractmethod
    def recommend(self, query_vector: np.ndarray, *args, top_k : int = 1, **kwargs) -> list[int]:
        """
        Abstract method to recommend the top K most similar items to a query vector.

        Parameters:
        - query_vector (np.ndarray): 1D numpy array of shape (n,) representing the query vector.
        - top_k (int): Number of top similar items to return. Default is 1.

        Returns:
        - list[int]: Indices of the top K most similar items in the data corpus. 
                     If top_k is greater than the available items, return indices of all items.
        """
        pass
