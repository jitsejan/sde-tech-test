{{ config(materialized='table') }}

WITH core_bets AS (
    SELECT * FROM {{ ref('core_bets') }}
),

game_weekly_stats AS (
    SELECT
        DATE_TRUNC('week', bet_created_at) AS week_start,
        game_id,
        game_name,
        game_category,

        COUNT(bet_id) AS total_bets,
        COUNT(DISTINCT user_id) AS unique_users,
        SUM(wager_usd) AS total_wager_usd,
        SUM(winnings_usd) AS total_winnings_usd,
        ROUND(SUM(winnings_usd) / NULLIF(SUM(wager_usd), 0), 2) AS payout_ratio

    FROM core_bets
    GROUP BY 1, 2, 3, 4
)

SELECT * FROM game_weekly_stats