select
    Date as telemetry_date,
    RPM as rpm,
    Speed as speed,
    nGear as gear,
    Throttle as throttle,
    Break as brake, 
    Time as lap_time,
    DriverNumber as driver_number
from {{ source('formula1', 'car_datas') }}