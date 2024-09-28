import faiss
import numpy as np

def topk_similar(query_vector: np.ndarray, data_matrix: np.ndarray, top_k: int = 5, metric: str = 'l2') -> list[int]:
    """
    Find the top K most similar vectors in a data matrix using FAISS.

    Parameters:
    - query_vector (np.ndarray): 1D numpy array of shape (n,) representing the query vector (must be float32).
    - data_matrix (np.ndarray): 2D numpy array of shape (K, n) where K is the number of vectors and n is the vector dimensions (must be float32).
    - top_k (int): The number of top similar vectors to return (default: 5).
    - metric (str): Similarity metric to use ('l2', 'cosine', or 'inner_product', default is 'l2').

    Returns:
    - list: Indices of the top_k most similar vectors in the data matrix.

    Example usage:
    ```python
    query_vec = np.random.rand(10).astype(np.float32)  # A query vector of dimension 10
    data_matrix = np.random.rand(1000, 10).astype(np.float32)  # A matrix of 1000 vectors of dimension 10
    top_k_indices = faiss_topk_similar(query_vec, data_matrix, top_k=5, metric='cosine')
    print(top_k_indices)
    ```
    
    Raises:
    - AssertionError: If input types or shapes are incorrect.
    - ValueError: If an invalid metric is provided.
    """
    
    # Assertions to ensure inputs are correct
    assert isinstance(query_vector, np.ndarray), "query_vector must be a numpy array"
    assert isinstance(data_matrix, np.ndarray), "data_matrix must be a numpy array"
    assert query_vector.dtype == np.float32, "query_vector must be of type float32"
    assert data_matrix.dtype == np.float32, "data_matrix must be of type float32"
    assert query_vector.ndim == 1, "query_vector must be a 1D array"
    assert data_matrix.ndim == 2, "data_matrix must be a 2D array"
    assert query_vector.shape[0] == data_matrix.shape[1], \
        "query_vector dimensions must match the second dimension of data_matrix"
    
    # Choose the FAISS index type based on the metric
    if metric == 'l2':
        index = faiss.IndexFlatL2(data_matrix.shape[1])
    elif metric == 'cosine':
        faiss.normalize_L2(data_matrix)
        faiss.normalize_L2(query_vector.reshape(1, -1))  # Reshape query to 2D to normalize
        index = faiss.IndexFlatIP(data_matrix.shape[1])  # Inner product for cosine similarity
    elif metric == 'inner_product':
        index = faiss.IndexFlatIP(data_matrix.shape[1])
    else:
        raise ValueError("Invalid metric! Use 'l2', 'cosine', or 'inner_product'.")
    
    index.add(data_matrix)
    
    _, indices = index.search(query_vector.reshape(1, -1), top_k)
    
    return indices[0].tolist()
