select
    to_time(Time) as lap_time,
    to_interval(LapTime) as lap_time_total,
    LapNumber as lap_number,
    NULLIF(to_time(PitOutTime), '') as pit_out_time,
    NULLIF(to_time(PitInTime), '') as pit_in_time,
    to_interval(Sector1Time) as sector_1_time,
    to_interval(Sector2Time) as sector_2_time,
    to_interval(Sector3Time) as sector_3_time,
    COALESCE(SpeedI1::DOUBLE, 0.0) as speed_sector_1,
    COALESCE(SpeedI2::DOUBLE, 0.0) as speed_sector_2,
    COALESCE(SpeedFL::DOUBLE, 0.0) as speed_fl,
    COALESCE(SpeedST::DOUBLE, 0.0) as speed_st,
    Compound as tire_compound,
    TyreLife as tire_life
from {{ source('formula1', 'laps') }}