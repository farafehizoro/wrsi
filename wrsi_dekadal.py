# -*- coding: utf-8 -*-
"""
Created on Sun Dec 25 16:18:33 2022

@author: farafehizoro
"""
from wrsi import Wrsi

class wrsi_dekadal(Wrsi):
    """
    Class to calculate daily wrsi
    
    
    """
    def __init__(self, ETa, ETc, method = "Original", rain = []):
        
        Wrsi.__init__(self, ETa, ETc, method, rain)
        self.wrsi = []
