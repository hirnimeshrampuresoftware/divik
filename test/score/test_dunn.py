import unittest

import numpy as np

from divik._score._dunn import _dunn


class DummyKMeans:
    cluster_centers_ = np.array([[2], [5]])
    labels_ = np.array([1, 1, 2, 2], dtype=int)
    distance = 'euclidean'


class TestDunn(unittest.TestCase):
    def test_computes_inter_to_intracluster_distances_rate(self):
        data = np.array([[1], [3], [4], [6]])
        dunn = _dunn(DummyKMeans(), data)
        self.assertAlmostEqual(dunn, 3.)
