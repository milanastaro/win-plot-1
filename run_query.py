#!/usr/bin/env python3
"""
Script to import team_data.csv into SQLite database and run queries.
This demonstrates how to use the SQL query for Arizona Cardinals data.
"""

import sqlite3
import csv
import os

def create_database_and_import_csv():
    """Create SQLite database and import team_data.csv"""
    
    # Database file path
    db_path = 'team_data.db'
    csv_path = 'team_data.csv'
    
    # Remove existing database if it exists
    if os.path.exists(db_path):
        os.remove(db_path)
    
    # Connect to SQLite database (creates it if it doesn't exist)
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Create table
    cursor.execute('''
    CREATE TABLE team_data (
        team TEXT,
        week INTEGER,
        opponent TEXT,
        home_away TEXT,
        points_scored INTEGER,
        points_allowed INTEGER,
        total_yards INTEGER,
        passing_yards INTEGER,
        rushing_yards INTEGER,
        turnovers INTEGER,
        first_downs INTEGER,
        time_of_possession TEXT,
        result TEXT
    )
    ''')
    
    # Read CSV and insert data
    with open(csv_path, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            cursor.execute('''
            INSERT INTO team_data VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                row['team'],
                int(row['week']),
                row['opponent'],
                row['home_away'],
                int(row['points_scored']),
                int(row['points_allowed']),
                int(row['total_yards']),
                int(row['passing_yards']),
                int(row['rushing_yards']),
                int(row['turnovers']),
                int(row['first_downs']),
                row['time_of_possession'],
                row['result']
            ))
    
    conn.commit()
    print(f"Database created successfully: {db_path}")
    return conn

def run_ari_query(conn):
    """Run the Arizona Cardinals query"""
    
    # Read the SQL query from file
    with open('query_ari_cardinals.sql', 'r') as file:
        query = file.read()
    
    cursor = conn.cursor()
    cursor.execute(query)
    
    # Get column names
    columns = [description[0] for description in cursor.description]
    
    # Print header
    print("\n" + "="*120)
    print("ARIZONA CARDINALS (ARI) - ALL WEEKS DATA")
    print("="*120)
    print(f"{'Week':<6} {'Opponent':<10} {'H/A':<6} {'Pts':<5} {'Allowed':<8} {'Yards':<7} {'Pass':<7} {'Rush':<7} {'TO':<4} {'1stD':<6} {'TOP':<10} {'Result':<8}")
    print("-"*120)
    
    # Print results
    for row in cursor.fetchall():
        print(f"{row[1]:<6} {row[2]:<10} {row[3]:<6} {row[4]:<5} {row[5]:<8} {row[6]:<7} {row[7]:<7} {row[8]:<7} {row[9]:<4} {row[10]:<6} {row[11]:<10} {row[12]:<8}")
    
    print("-"*120)
    
    # Get some statistics
    cursor.execute('''
    SELECT 
        COUNT(*) as games_played,
        SUM(CASE WHEN result = 'W' THEN 1 ELSE 0 END) as wins,
        SUM(CASE WHEN result = 'L' THEN 1 ELSE 0 END) as losses,
        AVG(points_scored) as avg_points_scored,
        AVG(points_allowed) as avg_points_allowed,
        AVG(total_yards) as avg_total_yards
    FROM team_data
    WHERE team = 'ARI'
    ''')
    
    stats = cursor.fetchone()
    print(f"\nSEASON STATISTICS:")
    print(f"Games Played: {stats[0]}")
    print(f"Record: {stats[1]}-{stats[2]}")
    print(f"Average Points Scored: {stats[3]:.1f}")
    print(f"Average Points Allowed: {stats[4]:.1f}")
    print(f"Average Total Yards: {stats[5]:.1f}")
    print("="*120 + "\n")

def main():
    """Main function"""
    print("Creating database and importing data...")
    conn = create_database_and_import_csv()
    
    print("\nRunning Arizona Cardinals query...")
    run_ari_query(conn)
    
    conn.close()
    print("Done!")

if __name__ == "__main__":
    main()
