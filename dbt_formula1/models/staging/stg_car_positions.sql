select
    Time as position_date,
    LapTime as lap_time,
    LapNumber as x_position,
    PitOutTime as y_position,
    PitInTime as z_position,
    Sector1Time as driver_number
from {{ source('formula1', 'laps') }}