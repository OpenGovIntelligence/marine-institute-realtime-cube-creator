
import os

#logging

log_dir = os.path.abspath( os.path.join(os.path.dirname(__file__),os.pardir,'logs'))
log_file=log_dir+"/service.log"
log_name="ogi-realtime-service"


#cube builder API
cubeBuilderAPI = "http://localhost:4567/cubeBuilderAPI/cubeBuilderArgs?"



#dataSets/schemas names turtle-stored
ds_IWBNetwork = "IWBNetwork"
ds_IrishNationalTideGaugeNetwork = "IrishNationalTideGaugeNetwork"
ds_IWaveBNetwork_spectral="IWaveBNetwork_spectral"
ds_IWaveBNetwork_zerocrossing="IWaveBNetwork_zerocrossing"


"""


https://erddap.marine.ie/erddap/griddap/IMI_EATL_WAVE.csv?


significant_wave_height

[(2017-09-16T21:00:00Z):1:(2017-09-16T21:00:00Z)]
[(36.5125):1:(59.987500000000004)]
[(-19.9875):1:(-0.01249999999999929)]

,
swell_wave_height

[(2017-09-16T21:00:00Z):1:(2017-09-16T21:00:00Z)]
[(36.5125):1:(59.987500000000004)]
[(-19.9875):1:(-0.01249999999999929)]

,
mean_wave_direction

[(2017-09-16T21:00:00Z):1:(2017-09-16T21:00:00Z)]
[(36.5125):1:(59.987500000000004)]
[(-19.9875):1:(-0.01249999999999929)]
,
mean_wave_period

[(2017-09-16T21:00:00Z):1:(2017-09-16T21:00:00Z)]
[(36.5125):1:(59.987500000000004)]
[(-19.9875):1:(-0.01249999999999929)]


https://erddap.marine.ie/erddap/tabledap/IWBNetwork.csv?

station_id%2Clongitude%2Clatitude%2Ctime%2CAtmosphericPressure%2CWindDirection%2CWindSpeed%2CGust%2CWaveHeight%2CWavePeriod%2CMeanWaveDirection%2CHmax%2CAirTemperature%2CDewPoint%2CSeaTemperature%2Csalinity%2CRelativeHumidity%2CQC_Flag&

time%3E=2017-09-04T00%3A00%3A00Z

https://erddap.marine.ie/erddap/tabledap/IWaveBNetwork_spectral.csv?buoy_id%2Ctime%2Clatitude%2Clongitude%2Cstation_id%2CPeakDirection%2CPeakSpread%2CSignificantWaveHeight%2CEnergyPeriod%2CMeanWavePeriod_Tm01%2CMeanWavePeriod_Tm02%2CPeakPeriod%2Cqcflag&time%3E=2017-09-08T16%3A49%3A20Z


"""