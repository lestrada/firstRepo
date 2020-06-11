# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 20:35:55 2020

@author: Luis Estrada
"""
import pandas as pd

import numpy as np

import seaborn as sns

iris = sns.load_dataset("iris")

iris.head(10)

iris.describe()

sns.set()
%matplotlib inline
sns.swarmplot(x="species",y="petal_length", data=iris)
