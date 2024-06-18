from functools import partial

import pytest
from unittest.mock import patch, MagicMock

from sklearn.datasets._kddcup99 import (
    fetch_kddcup99,
    print_coverage,
)

@pytest.mark.parametrize("as_frame", [True, False])
@pytest.mark.parametrize(
    "subset, n_samples, n_features",
    [
        (None, 494021, 41),
        ("SA", 100655, 41),
        ("SF", 73237, 4),
        ("http", 58725, 3),
        ("smtp", 9571, 3),
    ],
)
def test_fetch_kddcup99_percent10(subset, n_samples, n_features, as_frame):
    data = fetch_kddcup99(subset=subset, as_frame=as_frame)
    assert data.data.shape == (n_samples, n_features)
    assert data.target.shape == (n_samples,)
    if as_frame:
        assert data.frame.shape == (n_samples, n_features + 1)
    assert data.DESCR.startswith(".. _kddcup99_dataset:")


def test_fetch_kddcup99_return_X_y():
    fetch_func = partial(fetch_kddcup99, subset="smtp")
    data, target = fetch_func(return_X_y=True)
    assert data.shape[1] == 3  
    assert target.shape[0] == data.shape[0]

def test_fetch_kddcup99_as_frame():
    bunch = fetch_kddcup99(as_frame=True)
    assert hasattr(bunch, 'frame')
    assert hasattr(bunch, 'data')
    assert hasattr(bunch, 'target')


def test_fetch_kddcup99_shuffle():
    dataset = fetch_kddcup99(
        random_state=0,
        subset="SA",
        percent10=True,
    )
    dataset_shuffled = fetch_kddcup99(
        random_state=0,
        subset="SA",
        shuffle=True,
        percent10=True,
    )
    assert set(dataset["target"]) == set(dataset_shuffled["target"])
    assert dataset_shuffled.data.shape == dataset.data.shape
    assert dataset_shuffled.target.shape == dataset.target.shape


def test_fetch_kddcup99_download_if_missing():
    #cover the case where dataset is not available locally 

    #patch so we can simulate their behavior in a controlled env 
    #functions work correctly without the need for network calls 

    with patch("sklearn.datasets._kddcup99.exists", return_value=False), \
         patch("sklearn.datasets._kddcup99._fetch_remote"), \
         patch("sklearn.datasets._kddcup99.joblib.load", return_value=(MagicMock(), MagicMock())), \
         patch("sklearn.datasets._kddcup99.GzipFile") as mock_gzipfile, \
         patch("sklearn.datasets._kddcup99.os.remove"), \
         patch("sklearn.datasets._kddcup99.os.makedirs"), \
         patch("sklearn.datasets._kddcup99.join", return_value="/tmp/scikit_learn_data/kddcup99_10-py3/kddcup99_10_data"), \
         patch("builtins.open", new_callable=MagicMock):
        
        #mock  data to be returned by GzipFile
        mock_gzipfile.return_value.__enter__.return_value.readlines.return_value = [
            b"0,tcp,http,SF,181,5450,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,511,511,0.00,0.00,0.00,0.00,0.00,0.00,0,0,1.00,0.00,0.00,0.00,0.00,0.00,normal.\n"
        ]

        data_home = '/tmp/scikit_learn_data'
        kddcup99 = fetch_kddcup99(
            data_home=data_home,
            download_if_missing=True,
            subset='SA'
        )
        assert kddcup99.data.shape[0] > 0

def test_pandas_dependency_message():
    pass

def test_corrupted_file_error_message(tmp_path):
    """Check that a nice error message is raised when cache is corrupted."""
    kddcup99_dir = tmp_path / "kddcup99_10-py3" 
    #create a temporary directory to simulate the cache location and put corrupted data to it
    kddcup99_dir.mkdir()
    samples_path = kddcup99_dir / "samples"

    with samples_path.open("wb") as f:
        f.write(b"THIS IS CORRUPTED")

    msg = (
        "The cache for fetch_kddcup99 is invalid, please "
        f"delete {str(kddcup99_dir)} and run the fetch_kddcup99 again"
    )
    #check if the error is there
    with pytest.raises(OSError, match=msg):
        fetch_kddcup99(data_home=str(tmp_path))

if __name__ == "__main__":
    pytest.main()
    print_coverage()
