select
    "0" as name
from {{ source('formula1', 'drivers') }}