# Arizona Cardinals SQL Query - Quick Reference

## Basic Query
```sql
SELECT *
FROM team_data
WHERE team = 'ARI'
ORDER BY week;
```

## What This Query Does
1. **SELECT *** - Retrieves all columns from the table
2. **WHERE team = 'ARI'** - Filters for only Arizona Cardinals records
3. **ORDER BY week** - Sorts results by week number (1, 2, 3, ...)

## Available Columns
- `team` - Team abbreviation (ARI)
- `week` - Game week number
- `opponent` - Opponent team code
- `home_away` - Location (home/away)
- `points_scored` - Points scored by ARI
- `points_allowed` - Points allowed by ARI
- `total_yards` - Total offensive yards
- `passing_yards` - Passing yards
- `rushing_yards` - Rushing yards
- `turnovers` - Number of turnovers
- `first_downs` - Number of first downs
- `time_of_possession` - Time of possession
- `result` - Game result (W/L)

## Quick Start

### Option 1: Use Python Script (Easiest)
```bash
python run_query.py
```

### Option 2: Direct SQLite Query
```bash
# Create database first
sqlite3 team_data.db
.mode csv
.import team_data.csv team_data
.quit

# Run query
sqlite3 -header -column team_data.db < query_ari_cardinals.sql
```

### Option 3: Use Summary Query for Cleaner Output
```bash
sqlite3 -header -column team_data.db < query_ari_cardinals_summary.sql
```

## Example Output
```
week  opponent  location  points_scored  outcome
----  --------  --------  -------------  -------
1     BUF       AWAY      28             LOSS
2     NYG       HOME      31             WIN
3     DAL       AWAY      16             LOSS
...
```

## Variations

### Get Only Wins
```sql
SELECT * FROM team_data WHERE team = 'ARI' AND result = 'W' ORDER BY week;
```

### Get Home Games Only
```sql
SELECT * FROM team_data WHERE team = 'ARI' AND home_away = 'home' ORDER BY week;
```

### Get Season Statistics
```sql
SELECT 
    COUNT(*) as games,
    SUM(CASE WHEN result = 'W' THEN 1 ELSE 0 END) as wins,
    AVG(points_scored) as avg_points
FROM team_data 
WHERE team = 'ARI';
```
