#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 12:46:32 2023

@author: alex
"""


import pandas as pd
from os import path
import os

currentPath = os.getcwd()
path1 = os.path.split(currentPath)[0]
path2 = os.path.split(path1)[0]
dataPath = os.path.join(path2, 'data', 'problems')

# 3.0.1

# Load the 2018 aggregated pitching data (./data/2018-seasons/pitches.csv) into
# a DataFrame named dfp. You'll use it for the rest of the problesms in this
# section.

dfp = pd.read_csv(path.join(dataPath, '2018-season/pitches.csv'))
dfp.head()

# 3.0.2

# Use the dfp DataFrame to create another DataFrame, dfp50, the ais the top 50 
# (by lowest ERA) players.

dfp50 = dfp.sort_values('ERA').reset_index().head(50)

# 3.0.3

# Sort dfp by first name in descending order (so Zack Greinke is on the first
# line). On another line, look at dfp in the repl and make sure it worked.

dfp = dfp.sort_values('nameFirst', ascending=(False))
dfp.head()

# 3.0.4

# What is the type of dfp.sort_values('W')?

type(dfp.sort_values('W'))

# Should be "pandas.core.frame.DataFrame"

# 3.0.5

# a) Make a new DataFrame, dfp_simple, with just the columns 'nameFirst', 
#    'nameLast', 'W', 'L', 'ERA' in that order.

dfp_simple = (dfp[['nameFirst', 'nameLast',
                   'W', 'L', 'ERA']].copy().reset_index(drop=True))
dfp_simple.head()

# b) Rearrange dfp_simple so the order is 'nameLast', 'nameFirst', 'ERA', 'W',
#    'L'.

dfp_simple = dfp_simple[['nameLast', 'nameFirst', 'ERA', 'W', 'L']].copy()
dfp_simple.head()

# c) Using the original dfp DataFrame, add the 'teamID' column to dfp_simple.

dfp_simple['teamID'] = dfp['teamID']
dfp_simple.head()

# d) Write a copy of dfp_simple to ./data/problems/dfp_simple.txt. Make it '|'
# (pipe) delimited instead of ',' (comma) delimited.

dfp_simple.to_csv(path.join(dataPath, 'problems', 'dfp_simple.txt'),
                  sep = '|')
