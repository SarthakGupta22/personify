import pytest
import numpy as np
from recommendations.utils import topk_similar

def test_faiss_topk_similar_l2():
    # Generate a random data matrix of shape (100, 10)
    data_matrix = np.random.rand(100, 10).astype(np.float32)
    
    # Query vector of dimension 10
    query_vector = np.random.rand(10).astype(np.float32)
    
    # Run the function with L2 distance metric
    top_k_indices = topk_similar(query_vector, data_matrix, top_k=3, metric='l2')
    
    # Assert that top_k_indices returns the correct number of results
    assert len(top_k_indices) == 3
    assert isinstance(top_k_indices, list)

def test_faiss_topk_similar_cosine():
    # Generate a random data matrix of shape (50, 8)
    data_matrix = np.random.rand(50, 8).astype(np.float32)
    
    # Query vector of dimension 8
    query_vector = np.random.rand(8).astype(np.float32)
    
    # Run the function with cosine similarity metric
    top_k_indices = topk_similar(query_vector, data_matrix, top_k=5, metric='cosine')
    
    # Assert that top_k_indices returns the correct number of results
    assert len(top_k_indices) == 5
    assert isinstance(top_k_indices, list)

def test_faiss_topk_similar_inner_product():
    # Generate a random data matrix of shape (200, 20)
    data_matrix = np.random.rand(200, 20).astype(np.float32)
    
    # Query vector of dimension 20
    query_vector = np.random.rand(20).astype(np.float32)
    
    # Run the function with inner product metric
    top_k_indices = topk_similar(query_vector, data_matrix, top_k=7, metric='inner_product')
    
    # Assert that top_k_indices returns the correct number of results
    assert len(top_k_indices) == 7
    assert isinstance(top_k_indices, list)

def test_invalid_metric():
    # Generate random data
    data_matrix = np.random.rand(100, 10).astype(np.float32)
    query_vector = np.random.rand(10).astype(np.float32)
    
    # Check for ValueError when an invalid metric is provided
    with pytest.raises(ValueError):
        topk_similar(query_vector, data_matrix, top_k=3, metric='invalid_metric')

def test_assertions():
    data_matrix = np.random.rand(100, 10).astype(np.float32)
    query_vector = np.random.rand(10).astype(np.float32)
    
    # Test for AssertionError on non-float32 input types
    with pytest.raises(AssertionError):
        topk_similar(query_vector.astype(np.float64), data_matrix, top_k=3, metric='l2')
    
    # Test for AssertionError on shape mismatch
    with pytest.raises(AssertionError):
        topk_similar(np.random.rand(5).astype(np.float32), data_matrix, top_k=3, metric='l2')
