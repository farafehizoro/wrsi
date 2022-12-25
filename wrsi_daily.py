# -*- coding: utf-8 -*-
"""
Created on Sun Dec 25 13:16:29 2022

@author: farafehizoro
"""
from .wrsi import wrsi

class wrsi_daily(Wrsi):
    """
    Class to calculate daily wrsi
    
    
    """
    def __init__(self, ETa, ETc, method = "Original", rain = []):
        
        wrsi.__init__(self, ETa, ETc, method, rain)
        
    
        
