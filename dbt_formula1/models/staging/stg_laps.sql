select
    Time as lap_time,
    LapTime as lap_time_total,
    LapNumber as lap_number,
    PitOutTime as pit_out_time,
    PitInTime as pit_in_time,
    Sector1Time as sector_1_time, 
    Sector2Time as sector_2_time,
    Sector3Time as sector_3_time,
    SpeedI1 as speed_sector_1,
    SpeedI2 as speed_sector_2,
    SpeedI3 as speed_sector_3,
    Compound as tire_compound, 
    TypeLife as tire_life
from {{ source('formula1', 'laps') }}