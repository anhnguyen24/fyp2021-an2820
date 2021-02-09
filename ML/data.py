import csv
import numpy
import os
import pandas
from matplotlib import pyplot as plt 


def import_file(columnNames):
    """
    Imports data from ML folder 
    :type name: string
    :param name: columns to import, if 1 then import everything
    """
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(THIS_FOLDER, 'dengue_merged_dec2020.csv')
    if (columnNames == 1):
        data = pandas.read_csv(filename)
    else: 
        data = pandas.read_csv(filename, usecols=columnNames)
    print(data.shape)
    print(data.head(10))
    return data
