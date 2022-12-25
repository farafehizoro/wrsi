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
        self.same_length_ET = _check_same_length(self.ETa, self.ETc)
        self.ETa_negative = _check_negative(self.ETa)
        self.ETc_negative = _check_negative(self.ETc)
        self.rain_negative = False
        self.same_length_rain = False
        if (self.with_rain):
            self.rain_negative = _check_negative(self.rain)
            self.same_length_rain = _check_same_length(self.ETa, self.rain)
        
    def update_method(self, method = "Original"):
        """
        Parameters
        ----------
        method : string, optional
            update the method used to calculate wrsi. The default is "Original".

        Returns
        -------
        None.

        """
        self.method = method
        
    
def _check_negative(dat):
    """
    Check if there is negative value within the evapotranspiration and rainfall data

    Parameters
    ----------
    dat : list
        

    Returns
    -------
    bool: True if there is <0 value, false otherwise

    """
    for i in range(len(dat)):
        if (dat[i] < 0):
            return True
    return False
    
def _check_same_length(dat1, dat2):
    """
    Check if the two data has the same length
    Parameters
    ----------
    dat1 : list
    dat2 : list
        
    Returns
    -------
    bool : True if the two list has the same length, false otherwise.

    """
    if (len (dat1) == len(dat2)): 
        return True
    else: 
        return False
