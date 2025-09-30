-- SQL Query to retrieve aggregated statistics for Arizona Cardinals (ARI) by week
-- This query provides a summary view of weekly performance

SELECT 
    week,
    opponent,
    CASE 
        WHEN home_away = 'home' THEN 'HOME'
        ELSE 'AWAY'
    END as location,
    points_scored,
    points_allowed,
    CASE 
        WHEN result = 'W' THEN 'WIN'
        ELSE 'LOSS'
    END as outcome,
    total_yards,
    passing_yards,
    rushing_yards,
    turnovers,
    first_downs
FROM team_data
WHERE team = 'ARI'
ORDER BY week;
