select
    to_timestamp(Date) as telemetry_date,
    RPM::int as rpm,
    Speed::int as speed,
    nGear::int as gear,
    Throttle::int as throttle,
    Break as brake, 
    to_interval(Time) as lap_time,
    DriverNumber::int as driver_number
from {{ source('formula1', 'car_datas') }}