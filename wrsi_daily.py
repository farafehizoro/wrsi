# -*- coding: utf-8 -*-
"""
Created on Sun Dec 25 13:16:29 2022

@author: farafehizoro
"""
from .wrsi import Wrsi

class wrsi_daily(Wrsi):
    """
    Class to calculate daily wrsi
    
    
    """
    def __init__(self, ETa, ETc, method = "Original", rain = []):
        
        Wrsi.__init__(self, ETa, ETc, method, rain)
        self.wrsi = []
        
    def calculate_wrsi_daily(self):
        """
        calculate wrsi for daily data

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
            self.wrsi = self._wrsi_original_daily()
        else: 
            self.wrsi = self._wrsi_modified_daily()
        return self.wrsi
        
        
        
    def _wrsi_original_daily(self):
        """
        calculate wrsi using original method for daily data

        Returns
        -------
        a list containing daily wrsi data .

        """
        wrsi_original = []
           
        wrsi_temp = 100 
        ETc_tot = sum (self.ETc)
        for i in range(len(self.ETa)): 
            if ( self.ETa[i] < self.ETc[i]): #if there was water deficit
                diff = self.ETc[i] - self.ETa[i]
                wrsi_temp = wrsi_temp - 100 * (diff / ETc_tot) #water déficit
                if(self.with_rain_data): 
                    if(i < 9): 
                        if(self._water_excess_daily(self.ETa[0:(i+1)], self.rain[0:(i+1)])):
                            wrsi_temp = wrsi_temp - 0.3 #3 divided by 10
                    else:
                        if(self._water_excess_daily(self.ETa[(i-9):(i+1)], self.rain[(i-9):(i+1)])):
                            wrsi_temp = wrsi_temp - 0.3 #3 divided by 10
                            
            wrsi_original.append(wrsi_temp)
        return wrsi_original
    
    def _wrsi_modified_daily(self):
        """
        calculate daily wrsi with modified method

        Returns
        -------
        wrsi: list of daily wrsi.

        """
        wrsi_modified = []
        ETa_cumul = 0
        ETc_cumul = 0
        excess_number = 0
        for i in range(len(self.ETa)):
            ETa_cumul += self.ETa[i]
            ETc_cumul += self.ETc[i]
            if(self.with_rain_data):
                if(i < 9): 
                    if(self._water_excess_daily(self.ETa[0:(i+1)], self.rain[0:(i+1)])):
                        excess_number += 0.1 #plus 1 jour, soit 0.1 dekad
                else:
                    if(self._water_excess_daily(self.ETa[(i-9):(i+1)], self.rain[(i-9):(i+1)])):
                        excess_number += 0.1 #plus 1 jour, soit 0.1 dekad
            wrsi_temp = 100 * ETa_cumul / ETc_cumul - (excess_number * 3)
            wrsi_modified.append(wrsi_temp)
        return wrsi_modified
        
    def _water_excess_daily(list_ETa, list_RR):
        """
        Method to determine if there was a water success 
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
        sum_RR = sum(list_RR)
        sum_ETa = sum(list_ETa)
        water_excess = sum_RR - sum_ETa
        if (water_excess > 100):
            return True
        return False
    
    
        
