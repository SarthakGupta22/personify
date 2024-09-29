import pytest
import numpy as np
from recommendations.engine_faiss import FaissRecommender

@pytest.fixture(scope='module')
def data_matrix_l2():
    return np.random.rand(100, 10).astype(np.float32)

@pytest.fixture(scope='module')
def query_vector_l2():
    return np.random.rand(10).astype(np.float32)

@pytest.fixture(scope='module')
def recommender_l2(data_matrix_l2):
    return FaissRecommender(data_corpus=data_matrix_l2, metric='l2')

def test_faiss_recommender_l2(recommender_l2, query_vector_l2):
    top_k_indices = recommender_l2.recommend(query_vector_l2, top_k=3)    
    assert len(top_k_indices) == 3
    assert isinstance(top_k_indices, list)

@pytest.fixture(scope='module')
def data_matrix_cosine():
    return np.random.rand(50, 8).astype(np.float32)

@pytest.fixture(scope='module')
def query_vector_cosine():
    return np.random.rand(8).astype(np.float32)

@pytest.fixture(scope='module')
def recommender_cosine(data_matrix_cosine):
    return FaissRecommender(data_corpus=data_matrix_cosine, metric='cosine')

def test_faiss_recommender_cosine(recommender_cosine, query_vector_cosine):
    top_k_indices = recommender_cosine.recommend(query_vector_cosine, top_k=5)    
    assert len(top_k_indices) == 5
    assert isinstance(top_k_indices, list)

def test_invalid_metric(data_matrix_l2):
    with pytest.raises(AssertionError):
        FaissRecommender(data_corpus=data_matrix_l2, metric='invalid_metric')

def test_assertions(recommender_l2):
    # Generate a query vector with correct dimensions but incorrect dtype
    query_vector_wrong_dtype = np.random.rand(10).astype(np.float64)
    
    # Test for AssertionError on non-float32 input types
    with pytest.raises(AssertionError):
        recommender_l2.recommend(query_vector_wrong_dtype, top_k=3)
    
    # Generate a query vector with incorrect dimensions
    invalid_query_vector = np.random.rand(5).astype(np.float32)
    
    # Test for AssertionError on shape mismatch
    with pytest.raises(AssertionError):
        recommender_l2.recommend(invalid_query_vector, top_k=3)

def test_faiss_recommender_expected_result():
    data_matrix = np.array([
        [0.0, 1.0],
        [1.0, 0.0],
        [0.5, 0.5]
    ], dtype=np.float32)
    
    query_vector = np.array([1.0, 0.0], dtype=np.float32)
    recommender = FaissRecommender(data_corpus=data_matrix, metric='l2')
    top_k_indices = recommender.recommend(query_vector, top_k=1)

    print("Top K Indices: ", top_k_indices)
    
    assert len(top_k_indices) == 1, f"Expected 1 result, but got {len(top_k_indices)}"
    assert top_k_indices[0] == 1, f"Expected index 1, but got {top_k_indices[0]}"
