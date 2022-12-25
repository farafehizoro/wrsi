# Water requirement satisfaction index (WRSI) calculator

Calculation of the Water requirement satisfaction index (WRSI) for annual crop. 

# About
This package calculate the wrsi for crop based on bthe original method by FAO and the modified method.
The data used for the calculation are:
* actual evapotranspiration in mm(ETa)
* crop evapotranspiration in mm(called also water requirement) which is the maximum evapotranspiration for a crop where there is no water stress(ETc)
* rainfall in mm. The rainfall data is optionnal and is used to simulate the effect of water excess on the WRSI

Two timestep are avalaible for the calculation, depending on the input data: 
* daily
* dekadal 
The input data must have the same timestep and length

# Install