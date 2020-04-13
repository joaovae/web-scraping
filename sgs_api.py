# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 09:53:34 2020

@author: JOAO VICTOR
"""

import resquests as req
import pandas as pd
import json

def sgs_api(codigo):

    sgs_url = f'http://api.bcb.gov.br/dados/serie/bcdata.sgs.{codigo}/dados?formato=json'
    serie = req.get(sgs_url)
    serie = json.loads(serie.text)

    data = pd.DataFrame(serie)
    return data