from unittest.mock import Mock
from numpy import DataSource
import numpy.testing as npt
from pathlib import Path
import pytest

from inflammation.compute_data import JSONDataSource


def test_analyse_data_CSV():
    from inflammation.compute_data import analyse_data, CSVDataSource
    path = Path.cwd() / "data"
    data_source = CSVDataSource(path)
    #data_source = JSONDataSource(path)
    result = analyse_data(data_source)
    print(repr(result))
    expected_output = [0.,0.22510286,0.18157299,0.1264423,0.9495481,0.27118211,
                       0.25104719,0.22330897,0.89680503,0.21573875,1.24235548,0.63042094,
                       1.57511696,2.18850242,0.3729574,0.69395538,2.52365162,0.3179312,
                       1.22850657,1.63149639,2.45861227,1.55556052,2.8214853,0.92117578,
                       0.76176979,2.18346188,0.55368435,1.78441632,0.26549221,1.43938417,
                       0.78959769,0.64913879,1.16078544,0.42417995,0.36019114,0.80801707,
                       0.50323031,0.47574665,0.45197398,0.22070227]
    npt.assert_array_almost_equal(result, expected_output)

def test_analyse_data_JSON():
    from inflammation.compute_data import analyse_data
    path = Path.cwd() / "data"
    data_source = JSONDataSource(path)
    result = analyse_data(data_source)
    print(repr(result))
    expected_output = [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
       0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
       0., 0., 0., 0., 0., 0.]
    npt.assert_array_almost_equal(result, expected_output)


def test_std_deviation():
    """Test normalisation works for arrays of one and positive integers."""
    from inflammation.compute_data import compute_standard_deviation_by_day

    # Entry is 2d array for the values with rows (patients) and column (days)
    file_1 = [[0,2,0], [0,2,0]]
    input_data = file_1
  
    npt.assert_almost_equal(compute_standard_deviation_by_day([input_data]),[0.,0.,0.])


def test_with_mocks():
    from inflammation.compute_data import analyse_data
    data_source = Mock()
    data_source.load_inflammation_data.return_value = [[[0,2,0]], [[0,2,0]]]

    result = analyse_data(data_source)
    npt.assert_array_almost_equal(result, [0., 0. ,0.])

