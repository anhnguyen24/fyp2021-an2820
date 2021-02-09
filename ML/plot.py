import csv
import numpy
import os
import pandas
from matplotlib import pyplot as plt 

def age_group(data):
    """
    Create plot to see data distribution in each age group
    Drop the NaN values so data won't be redundant 
    :type name: data frame
    :param name: data
    """
    data_count = data.dropna(subset=['age'])
    data_count.reset_index(inplace=True)
    data_count['age']=data_count.age.astype('int64')
    print(data_count.head())
    count = data_count.groupby('age').count() #Count the occurence in each age group
    ax = count.plot.bar(y='dengue', rot=0, title="Number of patients in each age group")
    ax.set_xlabel("Age")
    ax.set_ylabel("Frequency")

def gender(data):
    """
    Create plot to see data distribution in each gender group
    Drop the NaN values so data won't be redundant 
    :type name: data frame
    :param name: columns to import, if 1 then import everything
    """
    data_count = data.dropna(subset=['sex'])
    data_count.reset_index(inplace=True)
    count = data_count.groupby('sex').count() #Count the occurence in each age group
    ax = count.plot.bar(y= 'id', rot=0, title="Number of patient in gender")
    ax.set_xlabel("Sex")
    ax.set_ylabel("Frequency")

def shock(data):
    """
    Create plot to see data distribution in shock outcome
    Drop the NaN values so data won't be redundant 
    :type name: data frame
    :param name: columns to import, if 1 then import everything
    """
    data_count = data.dropna(subset=['shock'])
    data_count.reset_index(inplace=True)
    #data_count['study']=data_count.age.astype('int64')
    count = data_count.groupby('shock').count() #Count the occurence in each age group
    ax = count.plot.bar(y= 'id', rot=0, title="Shock statistic")
    ax.set_xlabel("Dengue Result")
    ax.set_ylabel("Frequency")

def reshock(data):
    """
    Create plot to see data distribution in in reshock outcome
    Drop the NaN values so data won't be redundant 
    :type name: data frame
    :param name: columns to import, if 1 then import everything
    """

    #Count by shock
    data_count = data.dropna(subset=['reshock'])
    data_count.reset_index(inplace=True)
    #data_count['study']=data_count.age.astype('int64')
    count = data_count.groupby('reshock').count() #Count the occurence in each age group
    ax = count.plot.bar(y= 'id', rot=0, title="Reshock statistic")
    ax.set_xlabel("Dengue Result")
    ax.set_ylabel("Frequency")

def mucosal_bleed(data):
    """
    Create plot to see data distribution in mucosal bleeding outcome
    Drop the NaN values so data won't be redundant 
    :type name: data frame
    :param name: columns to import, if 1 then import everything
    """
    #Count by mucosalbleed
    data_count = data.dropna(subset=['mucosalbleed'])
    data_count.reset_index(inplace=True)
    #data_count['study']=data_count.age.astype('int64')
    count = data_count.groupby('mucosalbleed').count() #Count the occurence in each age group
    ax = count.plot.bar(y= 'id', rot=0, title="Mucosal Bleeding statistic")
    ax.set_xlabel("Dengue Result")
    ax.set_ylabel("Frequency")
    #plt.show()
