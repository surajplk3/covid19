import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

individual_details = pd.read_csv('IndividualDetails.csv')

class remove_na_leaveonlyint():
    def __init__(self, dataframe, index):
        self.dataframe = dataframe
        self.index = index
        
    def remove_na_str(self):
        strdf = self.dataframe[pd.to_numeric(self.dataframe[self.index], errors = 'coerce').notnull()]
        
    def remove_na_conv_str(self):
        strdf = self.dataframe[pd.to_numeric(self.dataframe[self.index], errors = 'coerce').notnull()][self.index].astype(int)
        new_strdf = pd.DataFrame(strdf)
        return new_strdf
  
dfclass = remove_na_leaveonlyint(individual_details, 'age')
ind_det_obj1 = dfclass.remove_na_conv_str()
sns_plot = sns.distplot(ind_det_obj1['age'])
sns_plot.figure.savefig('age_distribution.jpg')