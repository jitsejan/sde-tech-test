{{ config(materialized='table') }}

WITH bets AS (
    SELECT * FROM {{ source('raw', 'bet') }}
),

bet_outcomes AS (
    SELECT * FROM {{ source('raw', 'bet_outcome') }}
),

games AS (
    SELECT * FROM {{ source('raw', 'game') }}
),

core_bets AS (
    SELECT
        b.id AS bet_id,
        b.user_id,
        b.game_id,
        g.name AS game_name,
        g.category AS game_category,
        g.created_at AS game_created_at,
        b.wager,
        b.is_cash_wager,
        b.winnings,
        b.created_at AS bet_created_at,
        b.settled_at,
        bo.name AS outcome_name
    FROM bets AS b
    LEFT JOIN outcomes AS bo ON b.bet_outcome_id = bo.id
    LEFT JOIN games AS g ON b.game_id = g.id
)

SELECT * FROM core_bets