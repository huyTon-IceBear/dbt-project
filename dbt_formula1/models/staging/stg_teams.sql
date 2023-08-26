select
    "0" as driver_name
from {{ source('formula1', 'teams') }}