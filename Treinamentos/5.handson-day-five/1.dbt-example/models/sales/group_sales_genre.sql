{{
    config(
        materialized='ephemeral'
    )
}}


    SELECT
        genre,
        sum(global_sales) as total
    from {{ ref('stg_games_sales') }}
    group by genre