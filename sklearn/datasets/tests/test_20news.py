"""Test the 20news downloader, if the data is available,
or if specifically requested via environment variable
(e.g. for CI jobs)."""

from functools import partial
from unittest.mock import patch, call,MagicMock
import numpy as np
import pytest
import scipy.sparse as sp
import unittest


from sklearn.datasets._twenty_newsgroups import strip_newsgroup_footer,fetch_20newsgroups

from sklearn.datasets.tests.test_common import (
    check_as_frame,
    check_pandas_dependency_message,
    check_return_X_y,
)
from sklearn.preprocessing import normalize
from sklearn.utils._testing import assert_allclose_dense_sparse



class TestFetch20Newsgroups(unittest.TestCase):

    @patch('sklearn.datasets._twenty_newsgroups.fetch_20newsgroups', side_effect=fetch_20newsgroups)
    def test_20news(self, mock_fetch):
        data = fetch_20newsgroups(subset="all", shuffle=False)
        self.assertTrue(data.DESCR.startswith(".. _20newsgroups_dataset:"))

        data2cats = fetch_20newsgroups(
            subset="all", categories=data.target_names[-1:-3:-1], shuffle=False
        )
        self.assertEqual (data2cats.target_names == data.target_names[-2:])
        self.assertEqual (np.unique(data2cats.target).tolist() == [0, 1])

        assert len(data2cats.filenames) == len(data2cats.target)
        assert len(data2cats.filenames) == len(data2cats.data)

        entry1 = data2cats.data[0]
        category = data2cats.target_names[data2cats.target[0]]
        label = data.target_names.index(category)
        entry2 = data.data[np.where(data.target == label)[0][0]]
        self.assertEqual(entry1 == entry2)

        X, y = fetch_20newsgroups(subset="all", shuffle=False, return_X_y=True)
        self.assertEqual(len(X) == len(data.data))
        self.assertEqual(y.shape == data.target.shape)


    @patch('sklearn.datasets._twenty_newsgroups.fetch_20newsgroups', side_effect=fetch_20newsgroups)
    def test_20news_length_consistency(self, mock_fetch):
        """Checks the length consistencies within the bunch

        This is a non-regression test for a bug present in 0.16.1.
        """

        # Extract the full dataset
        data = fetch_20newsgroups(subset="all")
        self.assertEqual(len(data["data"]) == len(data.data))
        self.assertEqual(len(data["target"]) == len(data.target))
        self.assertEqual(len(data["filenames"]) == len(data.filenames))
    @patch('sklearn.datasets._twenty_newsgroups.fetch_20newsgroups', side_effect=fetch_20newsgroups)
    def test_cache_loading_failure(self, mock_fetch):
        def side_effect(*args, **kwargs):
            raise Exception("Cache loading failed")

        with patch("'sklearn.datasets._twenty_newsgroups.fetch_20newsgroups'.open", MagicMock(side_effect=side_effect)):
            data = fetch_20newsgroups(subset="all", shuffle=False)


    @patch('sklearn.datasets._twenty_newsgroups.fetch_20newsgroups', side_effect=fetch_20newsgroups)
    @patch('sklearn.datasets._twenty_newsgroups.os.path.exists', return_value=False)
    @patch('sklearn.datasets._twenty_newsgroups._download_20newsgroups', return_value={})
    def test_download_if_cache_not_exists(self, mock_fetch, mock_exists, mock_download):
        
        fetch_20newsgroups(subset="train", shuffle=False)

    @patch('sklearn.datasets._twenty_newsgroups.fetch_20newsgroups', side_effect=fetch_20newsgroups)
    def test_remove_options(self, mock_fetch):
        data = fetch_20newsgroups(subset="all", remove=("headers", "footers", "quotes"))

    @patch('sklearn.datasets._twenty_newsgroups.fetch_20newsgroups', side_effect=fetch_20newsgroups)
    def test_subsets(self, mock_fetch):
        data_train = fetch_20newsgroups(subset="train")
        data_test = fetch_20newsgroups(subset="test")
        self.assertIsNotNone(data_train)
        self.assertIsNotNone(data_test)


    @patch('sklearn.datasets._twenty_newsgroups.fetch_20newsgroups', side_effect=fetch_20newsgroups)
    def test_categories_none(self, mock_fetch):
        data = fetch_20newsgroups(subset="all", categories=None)
        self.assertIsNotNone(data)
    
    @patch('sklearn.datasets._twenty_newsgroups.fetch_20newsgroups', side_effect=fetch_20newsgroups)
    @patch('sklearn.datasets._twenty_newsgroups.os.path.exists', return_value=False)
    def test_download_not_missing(self, mock_fetch, mock_exists):
        with self.assertRaises(OSError):
            fetch_20newsgroups(subset="all", download_if_missing=False)

    



def test_20news_vectorized(fetch_20newsgroups_vectorized_fxt):
    # test subset = train
    bunch = fetch_20newsgroups_vectorized_fxt(subset="train")
    assert sp.issparse(bunch.data) and bunch.data.format == "csr"
    assert bunch.data.shape == (11314, 130107)
    assert bunch.target.shape[0] == 11314
    assert bunch.data.dtype == np.float64
    assert bunch.DESCR.startswith(".. _20newsgroups_dataset:")

    # test subset = test
    bunch = fetch_20newsgroups_vectorized_fxt(subset="test")
    assert sp.issparse(bunch.data) and bunch.data.format == "csr"
    assert bunch.data.shape == (7532, 130107)
    assert bunch.target.shape[0] == 7532
    assert bunch.data.dtype == np.float64
    assert bunch.DESCR.startswith(".. _20newsgroups_dataset:")

    # test return_X_y option
    fetch_func = partial(fetch_20newsgroups_vectorized_fxt, subset="test")
    check_return_X_y(bunch, fetch_func)

    # test subset = all
    bunch = fetch_20newsgroups_vectorized_fxt(subset="all")
    assert sp.issparse(bunch.data) and bunch.data.format == "csr"
    assert bunch.data.shape == (11314 + 7532, 130107)
    assert bunch.target.shape[0] == 11314 + 7532
    assert bunch.data.dtype == np.float64
    assert bunch.DESCR.startswith(".. _20newsgroups_dataset:")


def test_20news_normalization(fetch_20newsgroups_vectorized_fxt):
    X = fetch_20newsgroups_vectorized_fxt(normalize=False)
    X_ = fetch_20newsgroups_vectorized_fxt(normalize=True)
    X_norm = X_["data"][:100]
    X = X["data"][:100]

    assert_allclose_dense_sparse(X_norm, normalize(X))
    assert np.allclose(np.linalg.norm(X_norm.todense(), axis=1), 1)


def test_20news_as_frame(fetch_20newsgroups_vectorized_fxt):
    pd = pytest.importorskip("pandas")

    bunch = fetch_20newsgroups_vectorized_fxt(as_frame=True)
    check_as_frame(bunch, fetch_20newsgroups_vectorized_fxt)

    frame = bunch.frame
    assert frame.shape == (11314, 130108)
    assert all([isinstance(col, pd.SparseDtype) for col in bunch.data.dtypes])

    # Check a small subset of features
    for expected_feature in [
        "beginner",
        "beginners",
        "beginning",
        "beginnings",
        "begins",
        "begley",
        "begone",
    ]:
        assert expected_feature in frame.keys()
    assert "category_class" in frame.keys()
    assert bunch.target.name == "category_class"


def test_as_frame_no_pandas(fetch_20newsgroups_vectorized_fxt, hide_available_pandas):
    check_pandas_dependency_message(fetch_20newsgroups_vectorized_fxt)


def test_outdated_pickle(fetch_20newsgroups_vectorized_fxt):
    with patch("os.path.exists") as mock_is_exist:
        with patch("joblib.load") as mock_load:
            # mock that the dataset was cached
            mock_is_exist.return_value = True
            # mock that we have an outdated pickle with only X and y returned
            mock_load.return_value = ("X", "y")
            err_msg = "The cached dataset located in"
            with pytest.raises(ValueError, match=err_msg):
                fetch_20newsgroups_vectorized_fxt(as_frame=True)
class TestStripNewsgroupFooter(unittest.TestCase):


    def test_remove_footer_with_hyphens(self):
        text = """
        Some news text.

        ----------------
        Signature
        """
        expected_result = """
        Some news text.
        """
        result = strip_newsgroup_footer(text)
        self.assertEqual(result.strip(), expected_result.strip())
        

    def test_remove_footer_with_blank_line(self):
        text = """
        Some news text.

        Signature

        """
        expected_result = """
        Some news text.
        """
        result = strip_newsgroup_footer(text)
        self.assertEqual(result.strip(), expected_result.strip())
        

    def test_no_footer(self):
        text = """
        Some news text.
        """
        result = strip_newsgroup_footer(text)
        self.assertEqual(result.strip(), text.strip())
        

    def test_multiple_consecutive_hyphens(self):
        text = """
        Some news text.

        --------------------
        Signature
        """
        expected_result = """
        Some news text.
        """
        result = strip_newsgroup_footer(text)
        self.assertEqual(result.strip(), expected_result.strip())
        

    def test_empty_text(self):
        text = ""
        result = strip_newsgroup_footer(text)
        self.assertEqual(result.strip(), "")
        
