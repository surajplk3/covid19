# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 19:44:39 2020

@author: utpal
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#convert dd-mm-yyyy to yyyy-mm-dd
df_stat = pd.read_csv('IndividualDetails.csv', parse_dates=['status_change_date'], dayfirst = True)
recov = df_stat.loc[df_stat['current_status'] == 'Recovered']
decease = df_stat.loc[df_stat['current_status'] == 'Deceased']
hospitalised = df_stat.loc[df_stat['current_status'] == 'Hospitalized']


newrecov = recov['status_change_date']
newrecov = pd.DataFrame(newrecov)
newrecov.groupby([newrecov['status_change_date'].dt.year, newrecov['status_change_date'].dt.month, newrecov['status_change_date'].dt.day]).count().plot(kind='bar')
plt.savefig('daily_recovery.jpg')


#newdf = df['diagnosed_date']
#newdf = pd.DataFrame(newdf)
#newdf.groupby([newdf['diagnosed_date'].dt.year, newdf['diagnosed_date'].dt.month, newdf['diagnosed_date'].dt.day]).count().plot(kind='bar')
#plt.savefig('date_count_histo.jpg')

newdecease = decease['status_change_date']
newdecease = pd.DataFrame(newdecease)
newdecease.groupby(newdecease['status_change_date'].dt.date).count().plot(kind='bar')
plt.savefig('daily_deceased.jpg')

newhospit = hospitalised['status_change_date']
newhospit = pd.DataFrame(newhospit)
newhospit.groupby(newhospit['status_change_date'].dt.date).count().plot(kind='bar')
plt.savefig('daily_hospitalized.jpg')