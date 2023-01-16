#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 12:46:32 2023

@author: alex
"""

import pandas as pd
from os import path

dataPath = '/Users/alex/Documents/Personal Projects/ltcwbb/ltcwbb-files-0.9.0/data'

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

