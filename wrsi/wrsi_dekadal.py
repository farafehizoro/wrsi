# -*- coding: utf-8 -*-
"""
Created on Sun Dec 25 16:18:33 2022

@author: farafehizoro
"""
from .wrsi import Wrsi

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
        self._update_status()
        if (not self._same_length_ET):
            print ("ETa and ETo haven't different length, can't calculate wrsi")
            return self.wrsi
        #check if there are negative number
        
        if (self._ETa_negative or self._ETc_negative): 
            print("negative number for ETa or ETo, please check your data. Can't calculate wrsi")
            return self.wrsi
        
        #check rain data lenght and value (>0)
        if (self._with_rain):  #verify the rain data
            if(not self._same_length_rain):
                print ("Rain doesn't have the same length as evapotranspiration. Rain not considered for wrsi calculation.")
                self._rain = []
                self._with_rain = False
            if (self._rain_negative):
                print("Negative value for Rain data, please check your data. Rain not considered for wrsi calculation.")
                self._rain = []
                self._with_rain = False
        
        if (self.method == "Original"): #mbol tsy implémenter ko ny fahafatesan'ilay voly : to do
            self.wrsi = self._wrsi_original_dekadal()
        else: 
            self.wrsi = self._wrsi_modified_dekadal()
        return self.wrsi
    
    def _wrsi_original_dekadal(self):
        """
        calculate wrsi using original method for dekadal data

        Returns
        -------
        a list containing dekadal wrsi data .

        """
        wrsi_original = []
           
        wrsi_temp = 100 
        ETc_tot = sum (self._ETc)
        for i in range(len(self._ETa)): 
            if ( self._ETa[i] < self._ETc[i]): #if there was water deficit
                diff = self._ETc[i] - self._ETa[i]
                wrsi_temp = wrsi_temp - 100 * (diff / ETc_tot) #water déficit
                if(self.with_rain): 
                    if(self._water_excess_dek(self._ETa[i], self._rain[i])):
                        wrsi_temp = wrsi_temp - 3    
                            
            wrsi_original.append(wrsi_temp)
        return wrsi_original
    
    def _wrsi_modified_dekadal(self):
        """
        calculate dekadal wrsi with modified method

        Returns
        -------
        wrsi: list of dekadal wrsi.

        """
        wrsi_modified = []
        ETa_cumul = 0
        ETc_cumul = 0
        excess_number = 0
        for i in range(len(self._ETa)):
            ETa_cumul += self._ETa[i]
            ETc_cumul += self._ETc[i]
            if(self.with_rain):
                if(self._water_excess_dek(self._ETa[i], self._rain[i])):
                    excess_number += 1  #on compte les nombre de dek avec exces
            wrsi_temp = 100 * ETa_cumul / ETc_cumul - (excess_number * 3)
            wrsi_modified.append(wrsi_temp)
            
        return wrsi_modified
    
    def _water_excess_dek(self, ET_a, RR):
        """
        Method to determine if there was a water excess within the dekad 
        Parameters
        ----------
        ETa : list
            evapotranpiration.
        RR : list
            evapptranspiration.

        Returns
        -------
        bool
            true if there is water excess.
        """
        water_excess = RR - ET_a
        if (water_excess > 100): 
            return True
        return False