# quickly put together message for PAR sensor
#

# Data Output:  Data output may be chosen between volts, volts‐offset (default),
# calibrated irradiance, or calibrated irradiance adjusted for immersion in water.  
# Optionally, sensor temperature and line voltage may be included in the data
# stream. A preamble may be defined to the data frame to easily identify data in
# a multi‐sensor environment. For example "$" may be used in a NEMA applica‐
# tion.  As delivered, the output is in volts‐offset.  
# Typical output data stream: Displayed are irradiance in µE m‐2 sec‐1
# , tempera‐
# ture  in °C  and line voltage in volts:
# .013016, 16.06, 6.137
# .012990, 16.06, 6.137
# .012998, 16.06, 6.137
# .013000, 16.06, 6.137

Header header

# irradiance in µE m‐2 sec‐1
# (see Data Output section above)
float32 irradiance

# temperature  in °C
# (see Data Output section above)
float32 temperature

# line voltage in volts
# (see Data Output section above)
float32 line_voltage
