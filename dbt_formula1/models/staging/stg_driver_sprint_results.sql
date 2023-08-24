select
    year::int as year,
    round::int as round,
    name as race_name,
    CAST(date as DATE) as race_date,
    "name:1" AS circuit_name,
    carNumber::int as car_number,
    COALESCE(position::int, 0) as position, -- Replace null with 0
    COALESCE(points::int, 0) as points, -- Replace null with 0
    COALESCE(time, 'N/A') as time, -- Replace null with 'N/A'
    reason
from {{ source('formula1', 'driver_sprint_results') }}