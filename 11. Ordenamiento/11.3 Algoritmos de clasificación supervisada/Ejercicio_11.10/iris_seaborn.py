# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 17:14:15 2020

@author: Claudio Collado

"""

import pandas as pd
import seaborn as sns
from sklearn.datasets import load_iris

#Cargo el dataframe
iris_dataset = load_iris()


iris_dataframe = pd.DataFrame(iris_dataset['data'], columns = iris_dataset.feature_names)

#Agrego lo sugerico
iris_dataframe['target'] = iris_dataset['target']

#Utilizo seaborn para graficar
grafico = sns.pairplot(iris_dataframe,hue="target")
grafico.fig.suptitle("Grafico de Parejas - Dataset Iris", y=1.03,fontsize=20) #Agrego titulo