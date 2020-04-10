# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 18:36:00 2020

@author: utpal
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('IndividualDetails.csv', parse_dates=['diagnosed_date'], dayfirst = True)

newdf = df['diagnosed_date']
newdf = pd.DataFrame(newdf)

newdf.groupby(newdf['diagnosed_date'].dt.month).count().plot(kind='bar')
plt.savefig('monthly_confirm.jpg')

newdf.groupby([newdf['diagnosed_date'].dt.year, newdf['diagnosed_date'].dt.month, newdf['diagnosed_date'].dt.day]).count().plot(kind='bar')
plt.savefig('daily_confirm.jpg')

fig = newdf.groupby(newdf['diagnosed_date'].dt.date).count().plot(kind='bar')

