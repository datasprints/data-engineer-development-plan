{{
    config(
        materialized='table'
    )
}}

SELECT
    *
from {{ ref('group_sales_genre') }}