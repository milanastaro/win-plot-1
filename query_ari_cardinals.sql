-- SQL Query to retrieve all data for Arizona Cardinals (ARI) by week
-- This query selects all columns from the team_data table for the ARI team
-- and orders the results by week in ascending order

SELECT *
FROM team_data
WHERE team = 'ARI'
ORDER BY week;
