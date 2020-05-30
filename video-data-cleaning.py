# -*- coding: utf-8 -*-
"""
Created on Sat May 30 15:17:13 2020

@author: JOAO VICTOR
"""
import pandas as pd
from data_covid import get_covid_data

dic = { 'Nome' : ['Isa', 'Lott', 'X Ae A-Xii'],
        'Idade' : [19, 20, 0],
        'Sexo' : ['F', 'M', 'Unknown']
      }
df = pd.DataFrame(dic)

df = pd.get_dummies(df, columns = ['Sexo'])

data = get_covid_data()

data = data.drop(columns=['#'])
data = data.drop([0,216])

data['NewCases'].fillna('0', inplace = True)
data['NewDeaths'].fillna('0', inplace = True)
data.fillna('-', inplace = True)

lista = []
for i in data['NewCases']:
    i = i.replace(',', '')
    lista.append(i)

data['NewCases'] = lista



