# Water requirement satisfaction index (WRSI) calculator
```
from wrsi import wrsi_dekadal
from wrsi import wrsi_daily

calculate_wrsi_dek = wrsi_dekadal(ETa, ETc, method = "Modified", rain = Rain_data_list)
calculate_wrsi_dek.calculate_wrsi_dekadal()
print(calculate_wrsi_dek.wrsi)

calculate_wrsi_daily = wrsi_dekadal(ETa, ETc, method = "Original")
calculate_wrsi_dek.calculate_wrsi_daily()
print(calculate_wrsi_daily.wrsi)

```

Calculation of the Water requirement satisfaction index (WRSI) for annual crop. 

# About
This package calculate the wrsi for crop based on the original method by FAO (Frere and Popov 1979) and the modified method.
The data needed for the calculation are:
* actual evapotranspiration in mm (ETa).
* reference crop evapotranspiration in mm (called also water requirement) which is the maximum evapotranspiration for a crop where there is no water stress(ETc).
* rainfall in mm. Rainfall data is optionnal and is used to simulate the effect of water excess on the WRSI.

Two timestep are avalaible for the calculation, depending on the input data: 
* daily
* dekadal 
The input data must have the same timestep and length.

# Install

pip install wrsi