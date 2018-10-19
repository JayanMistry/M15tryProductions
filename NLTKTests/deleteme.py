#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 10:36:05 2018

@author: jay
"""

import pyphen

dic = pyphen.Pyphen(lang='nl_NL')

res = (dic.inserted('lettergrepen'))
print(res.count('-')+1) 


