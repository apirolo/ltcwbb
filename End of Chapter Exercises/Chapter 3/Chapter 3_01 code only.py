#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 14:51:27 2023

@author: alex
"""

import pandas as pd
from os import path
import os

dataPath = path.join(path.dirname(path.dirname(os.getcwd())),
                        'data')

# 3.1.1

dfb = pd.read_csv(path.join(dataPath, '100-game-sample/atbats.csv'))
dfb.head()

# 3.1.2

dfb['runs_scored'] = (dfb['b_score_end'] - dfb['b_score_start'])
dfb.head()

# 3.1.3

dfb['ab_desc'] = (dfb['batter'] + ' got a ' +
                  dfb['event'] + ' vs ' + dfb['pitcher'])

dfb.head()

# 3.1.4

dfb['final_out'] = dfb['o'] == 3
dfb.head()

# 3.1.5

dfb['len_last_name'] = dfb['pitcher'].apply(lambda x : len(x.split('.')[-1]))
dfb.head()

# 3.1.6

dfb['ab_id'] = dfb['ab_id'].astype(str)

# 3.1.7

# a)

dfb.columns = [x.replace('_', ' ') for x in dfb.columns]
dfb.head()

# b) 

dfb.columns = [x.replace(' ', '_') for x in dfb.columns]
dfb.head()

# 3.1.8

# a) 

dfb['run_portion'] = (dfb['runs_scored']) / (dfb['b_score_end'])
dfb.head()

# b)

dfb['run_portion'].fillna(-99, inplace = True)
dfb.head()

# 3.1.9

dfb.drop('run_portion', axis = 1, inplace = True)
dfb.head()
