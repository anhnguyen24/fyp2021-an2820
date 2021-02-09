import csv
import numpy
import os
import pandas
from matplotlib import pyplot as plt 
import sys
sys.path.insert(0, '.\ML')
import data
import plot 

if __name__ == "__main__":
    columns = ['id', 'study', 'reshock', 'shock', 'date_admission', 'dengue', 'age', 'sex', 'weight', 'mucosalbleed']
    data = data.import_file(columns)
    plot.age_group(data)
    plot.gender(data)
    plot.shock(data)
    plot.reshock(data)
    plot.mucosal_bleed(data)
    plt.show()