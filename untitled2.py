# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 13:57:04 2019

@author: purva patel
"""

import pandas as pd
dataset = pd.read_table('New Text Document.txt',
sep=',',
header=1,
skiprows=1,
skipfooter=2,
index_col=0,
parse_dates=True,
na_values=['-'])

from openpyxl.workbook import Workbook
writer = pd.ExcelWriter('practice.xlsx')
dataset.to_excel(writer, sheet_name = 'first')
dataset.to_excel(writer, sheet_name = 'second')
writer.save()