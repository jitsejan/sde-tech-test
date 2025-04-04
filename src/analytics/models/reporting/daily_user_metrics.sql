{{ config(materialized='table') }}

WITH core_bets AS (
    SELECT * FROM {{ ref('core_bets') }}
),

core_users AS (
    SELECT * FROM {{ ref('core_users') }}
),

daily_metrics AS (
    SELECT
        cb.user_id,
        cu.country_code,
        DATE(cb.bet_created_at) AS activity_date,

        COUNT(cb.bet_id) AS total_bets,
        SUM(cb.wager_usd) AS total_wager_usd,
        SUM(cb.winnings_usd) AS total_winnings_usd,
        AVG(cb.wager_usd) AS avg_wager_usd,
        MAX(cb.wager_usd) AS max_wager_usd,

        COUNT(DISTINCT cb.game_id) AS distinct_games_played,
        COUNT(DISTINCT cb.bet_id) FILTER (WHERE cb.outcome = 'winner') AS total_wins

    FROM core_bets AS cb
    LEFT JOIN core_users AS cu ON cb.user_id = cu.user_id
    GROUP BY 1, 2, 3
)

SELECT * FROM daily_metrics