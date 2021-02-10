
{{
    config(
        materialized='table'
    )
}}


SELECT
    name,
    platform,
    year,
    genre,
    publisher,
    na_sales,
    eu_sales,
    jp_sales,
    other_sales,
    global_sales
from {{ source('game_sales_db', 'game_sales') }}