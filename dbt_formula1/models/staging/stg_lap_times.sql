select
    CAST(date as DATE) as race_date,
    carNumber::int as car_number,
    lap::int as lap,
    position::int as position,
    time,
    milliseconds
from {{ source('formula1', 'lap_times') }}