"""Module containing mechanism for calculating standard deviation between datasets.
"""

import glob
import os
import numpy as np

from inflammation import models, views


class CSVDataSource:
    """
    Loads all the inflammation csvs within a specified folder
    """
    def __init__(self, data_dir):
        self.data_dir = data_dir
    
    def load_inflammation_data(self):
        data_file_paths = glob.glob(os.path.join(self.data_dir, 'inflammation*.csv'))
        #print('path:',data_file_paths)
        if len(data_file_paths) == 0:
            raise ValueError(f"No inflammation csv's found in path {self.data_dir}")
        data = map(models.load_csv, data_file_paths)
        return data
    

class JSONDataSource:
    """
    Loads all the inflammation JSON within a specified folder
    """
    def __init__(self, data_dir):
        self.data_dir = data_dir
    
    def load_inflammation_data(self):
        data_file_paths = glob.glob(os.path.join(self.data_dir, 'inflammation*.json'))
        if len(data_file_paths) == 0:
            raise ValueError(f"No inflammation JSON files found in path {self.data_dir}")
        data = map(models.load_json, data_file_paths)
        return data


def analyse_data(data_source):
    """Calculate the standard deviation by day between datasets

    Gets all the inflammation csvs within a directory, works out the mean
    inflammation value for each day across all datasets, then graphs the
    standard deviation of these means."""
    data = data_source.load_inflammation_data()
    daily_standard_deviation = compute_standard_deviation_by_day(data)
        
    return daily_standard_deviation


def compute_standard_deviation_by_day(data):
    " Calculates the standard deviation from a set of data"

    means_by_day = map(models.daily_mean, data)
    means_by_day_matrix = np.stack(list(means_by_day))
    standard_deviation = np.std(means_by_day_matrix, axis=0)

    return standard_deviation