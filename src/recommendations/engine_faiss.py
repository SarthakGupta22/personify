from logging import getLogger

import faiss
import numpy as np

from .base import BaseRecommender

logger = getLogger(__name__)

class FaissRecommender(BaseRecommender):
    def __init__(self, data_corpus: np.ndarray, metric: str = 'l2'):
        assert metric in ['l2', 'cosine'], "Invalid metric! Use `l2` or `cosine`"
        super().__init__(data_corpus)
        
        self.metric = metric
        if metric == 'cosine':
            logger.debug("Metric is cosine. Will normalize everything to unit length.")
            faiss.normalize_L2(self.data_corpus)
            self.index = faiss.IndexFlatIP(data_corpus.shape[1])
        else:
            logger.debug("Metric is L2. Good.")
            self.index = faiss.IndexFlatL2(data_corpus.shape[1])
        
        self.index.add(self.data_corpus)

    def recommend(self, query_vector: np.ndarray, top_k: int = 1) -> list[int]:
        assert query_vector.ndim == 1, "query_vector must be a 1D array"
        assert query_vector.shape[0] == self.data_corpus.shape[1], "query_vector dimensions must match the second dimension of data_corpus"
        assert query_vector.dtype == np.float32, "query_vector must be of type float32"
        
        query_vector = query_vector.reshape(1, -1)

        if self.metric == 'cosine':
            faiss.normalize_L2(query_vector)
        
        actual_top_k = min(top_k, self.data_corpus.shape[0])
        if actual_top_k < top_k:
            logger.warning(f"Requested top_k ({top_k}) exceeds data corpus size ({self.data_corpus.shape[0]}). Adjusted top_k to {actual_top_k}.")
        else:
            logger.debug(f"top_k is set to {actual_top_k}")

        _, indices = self.index.search(query_vector, actual_top_k)
        return indices[0].tolist()
