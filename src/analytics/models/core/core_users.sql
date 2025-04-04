{{ config(materialized='table') }}

WITH users AS (
    SELECT * FROM {{ source('raw', 'users') }}
),

addresses AS (
    SELECT * FROM {{ source('raw', 'user_address') }}
),

core_users AS (
    SELECT
        u.id AS user_id,
        u.name AS user_name,
        a.country_code,
        a.city,
        a.postcode,
        a.address_line_1,
        a.address_line_2
    FROM users AS u
    LEFT JOIN addresses AS a ON u.id = a.user_id
    WHERE a.country_code IN ('GB', 'IE')
      AND u.IsTestUser = FALSE
)

SELECT * FROM core_users