select
    year::int as year,
    round::int as round,
    name as race_name,
    CAST(date as DATE) as race_date,
    team,
    points:: int as points
FROM {{ source('formula1', 'constructor_results') }}