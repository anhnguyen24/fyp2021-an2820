"""
Plotting Gender count
============================

"""

# Libraries
import pandas as pd
import matplotlib.pyplot as plt


# --------------------------------
# Methods
# --------------------------------
def gender(data):
    """
    Create plot to see data distribution in each gender group
    Drop the NaN values so data won't be redundant
    :type name: data frame
    :param name: columns to import, if 1 then import everything
    """
    data_count = data.dropna(subset=['sex'])
    data_count.reset_index(inplace=True)
    count = data_count.groupby('sex').count()  # Count the occurence in each age group
    ax = count.plot.bar(y='id', rot=0, title="Number of patient in gender")
    ax.set_xlabel("Sex")
    ax.set_ylabel("Frequency")


# --------------------------------
# Configuration
# ---------------------------------
# Load data
data = pd.read_csv('./resources/datasets/dengue_merged_dec2020.csv')

# Plot
gender(data)

# Display
plt.show()