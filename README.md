# win-plot-1

SQL Query for Arizona Cardinals Team Data

## Overview

This repository contains SQL queries and data for NFL team statistics, specifically focused on retrieving data for the Arizona Cardinals (ARI).

## Files

- **team_data.csv** - CSV file containing team statistics for multiple NFL teams organized by week
- **query_ari_cardinals.sql** - SQL query to retrieve all Arizona Cardinals data ordered by week
- **run_query.py** - Python script that demonstrates how to import the CSV data into SQLite and run the query

## Data Structure

The `team_data.csv` file contains the following columns:
- `team` - Team abbreviation (e.g., ARI for Arizona Cardinals)
- `week` - Week number
- `opponent` - Opponent team abbreviation
- `home_away` - Whether the game was home or away
- `points_scored` - Points scored by the team
- `points_allowed` - Points allowed by the team
- `total_yards` - Total offensive yards
- `passing_yards` - Passing yards
- `rushing_yards` - Rushing yards
- `turnovers` - Number of turnovers
- `first_downs` - Number of first downs
- `time_of_possession` - Time of possession (MM:SS format)
- `result` - Game result (W for win, L for loss)

## SQL Query

The main SQL query for Arizona Cardinals data is:

```sql
SELECT *
FROM team_data
WHERE team = 'ARI'
ORDER BY week;
```

This query:
1. Selects all columns from the team_data table
2. Filters for only Arizona Cardinals (ARI) records
3. Orders the results by week in ascending order

## Usage

### Using with SQLite (Recommended)

Run the Python script to automatically create the database and execute the query:

```bash
python run_query.py
```

This will:
1. Create a SQLite database (`team_data.db`)
2. Import data from `team_data.csv`
3. Execute the Arizona Cardinals query
4. Display formatted results and statistics

### Using with Other Databases

#### MySQL
```bash
# Import CSV
mysqlimport --local --fields-terminated-by=',' --lines-terminated-by='\n' \
  --ignore-lines=1 your_database team_data.csv

# Run query
mysql -u your_user -p your_database < query_ari_cardinals.sql
```

#### PostgreSQL
```bash
# Import CSV
psql -d your_database -c "\COPY team_data FROM 'team_data.csv' WITH CSV HEADER"

# Run query
psql -d your_database -f query_ari_cardinals.sql
```

## Sample Output

The query will return all Arizona Cardinals games with their weekly statistics, ordered by week:

```
Week   Opponent   H/A    Pts   Allowed  Yards   Pass    Rush    TO   1stD   TOP        Result  
1      BUF        away   28    34       378     245     133     2    22     28:45      L       
2      NYG        home   31    28       420     310     110     1    25     32:15      W       
3      DAL        away   16    28       305     220     85      3    18     26:30      L       
...
```

## Requirements

- Python 3.x (for the demo script)
- SQLite3 (usually included with Python)
- For other databases: MySQL, PostgreSQL, etc. with their respective clients

## License

This is a sample project for educational purposes.