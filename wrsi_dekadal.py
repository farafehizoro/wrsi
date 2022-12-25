# -*- coding: utf-8 -*-
"""
Created on Sun Dec 25 16:18:33 2022

@author: farafehizoro
"""
from wrsi import Wrsi

class wrsi_dekadal(Wrsi):
    """
    Class to calculate dekadal wrsi
    
    
    """
    def __init__(self, ETa, ETc, method = "Original", rain = []):
        
        Wrsi.__init__(self, ETa, ETc, method, rain)
        self.wrsi = []

    def calculate_wrsi_dekadal(self):
        """
        calculate wrsi for dekadal data

        Returns
        -------
        a list containing the wrsi data .

        """
        self.wrsi = []
        if (not self.same_length_ET):
            print ("ETa and ETo haven't different length, can't calculate wrsi")
            return self.wrsi
        #check if there are negative number
        
        if (self.ETa_negative or self.ETc_negative): 
            print("negative number for ETa or ETo, please check your data. Can't calculate wrsi")
            return self.wrsi
        
        #check rain data lenght and value (>0)
        if (self.with_rain):  #verify the rain data
            if(not self.same_length_rain):
                print ("Rain doesn't have the same length as evapotranspiration. Rain not considered for wrsi calculation.")
                self.rain = []
                self.with_rain = False
            if (self.rain_negative):
                print("Negative value for Rain data, please check your data. Rain not considered for wrsi calculation.")
                self.rain = []
                self.with_rain = False
        
        if (self.method == "Original"): #mbol tsy implémenter ko ny fahafatesan'ilay voly : to do
            self.wrsi = self._wrsi_original_dekadal()
        else: 
            self.wrsi = self._wrsi_modified_dekadal()
        return self.wrsi
        