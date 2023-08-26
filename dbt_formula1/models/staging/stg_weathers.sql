select
    to_time(Time) as weather_time,
    AirTemp as air_temperature,
    Humidity as humidity,
    Pressure as pressure,
    Rainfall as rainfall,
    TrackTemp as track_temperature, 
    WindDirection:: int as wind_direction,
    WindSpeed as wind_speed
from {{ source('formula1', 'weathers') }}