# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 14:28:45 2021

@author: jevange1
"""

import pandas as pd
from scipy.optimize import minimize

wi = -0.145
gdps = [-3, -2, -1, 0, 1, 2, 3, 4, 5]

array_fronteiras = []

for gdp in gdps:
    
    array_c = []
    array_i = []
    
    for i in range(-1500, 2000, 1):
    
        g = 0.1
        x = 4.8
        
        b1 = 1.1042
        b2 = 1.2485
        b12 = 0.1187
        b22 = 0.0093
        b0 = 0.3438
        
        i = i / 100
        
        w = [0.646, 0.2, 0.151, 0.148, -0.145]
        
        def fun(c):
    
            return (c*w[0] + g*w[1] + i*w[2] + x*w[3] + (b0 + b2**i + b22*i**2)*w[4] - gdp)**2
        
        def con(c):
    
            return c*w[0] + g*w[1] + i*w[2] + x*w[3] +  (b0 + b2**i + b22*i**2)*w[4] - gdp
        
        cons = ({'type':'eq', 'fun':con})
        result = minimize(fun, x0=1)
        array_c.append(float(result['x']))
        array_i.append(i)
        
    fronteira = pd.DataFrame()
    
    fronteira['Investimento GDP'.format(gdp)] = array_i    
    fronteira['Consumo GDP'.format(gdp)] = array_c

    array_fronteiras.append(fronteira)

    
df_fronteira = pd.concat(array_fronteiras) 

aux_ext = r'I:\ECONOMIC\Working\Apresentacoes\2021\English\Fim de Ano\Atividade\fronteira_gdp.xlsx'

with pd.ExcelWriter(aux_ext, engine = 'openpyxl') as writer:
    df_fronteira.to_excel(writer)

#%% PLOTTING
    
x = [-8.87530237359192,
    4.81319159129421,
    1.30447551303365,
    -1.44377480491277,
    -3.98451236685347,
    8.48696339826473,
    1.9563000854953,
    6.66078973770292,
    11.9524077675073,
    12.2869570612863,
    -2.13387372887173,
    17.8539193057876,
    6.83404646691463,
    0.778776996364594,
    5.82837033026529,
    -4.22582047936972,
    -13.9459416148073,
    -12.1,
    -2.6,
    5.2,
    3.4,
    -0.8,
    17,
    -1.3]

y = [0.378257570707019,
    4.03263240959952,
    0.771306565531726,
    1.31884706061531,
    -0.545992777699744,
    3.92349408784476,
    4.42187681368913,
    5.28469926079227,
    6.3762694252208,
    6.46426620808109,
    4.45639698027867,
    6.22937173207199,
    4.8184595372895,
    3.4994506815113,
    3.47145580415371,
    2.3,
    -3.2,
    -3.8,
    2,
    2.4,
    2.2,
    -5.5,
    3.9,
    -0.6]

z = [0.92151586100755,
    2.86564365670904,
    1.1391774415179,
    1.42575141073693,
    0.438025412014609,
    2.81159523452246,
    3.06848015743866,
    3.52894930037541,
    4.11084712702927,
    4.15766627331223,
    3.08269714195138,
    4.0390396174224,
    3.28279677349869,
    2.57998832294211,
    2.57016187557353,
    1.94137741846878,
    -0.973926460607355,
    -1.2891027,
    1.7844802,
    2.0034748,
    1.8960418,
    -2.1761354,
    2.8075512,
    0.4121313]

years = ['1999',
        '2000',
        '2001',
        '2002',
        '2003',
        '2004',
        '2005',
        '2006',
        '2007',
        '2008',
        '2009',
        '2010',
        '2011',
        '2012',
        '2013',
        '2014',
        '2015',
        '2016',
        '2017',
        '2018',
        '2019',
        '2020',
        '2021',
        '2022']

import matplotlib.pyplot as plt

cm = plt.cm.get_cmap('RdYlBu')

fig, ax = plt.subplots()
ax.scatter(x, y, c=z, cmap=cm)

sc = plt.scatter(x, y, c=z, cmap=cm)
plt.colorbar(sc)


for i, txt in enumerate(years):
    plt.annotate(txt, (x[i], y[i]))

plt.figure(figsize=(20, 20))
plt.show()