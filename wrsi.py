# -*- coding: utf-8 -*-
"""
Created on Sun Dec 25 12:18:32 2022

@author: Farafehizoro Ramanjatonirina
"""
class Wrsi:
    """
    General class to calculate the water requirement satisfaction index of annual crop
    
    Attributes: 
        * ETa (list): actual evapotranspiration for the crop
        * ETc (list): potentail evapotranspiration for the crop (max ETa if there is no water shortage)
        * method (str): the method to use "Original" or "Modified"
        * rain (list): rainfall data (optional)
    """
    def __init__(self, ETa, ETc, method = "Original", rain = []):
        self.ETa = ETa
        self.ETc = ETc
        self.method = method
        self.rain = rain
        self.with_rain = False
        if (len(self.rain)>0):
            self.with_rain = True
        
    

