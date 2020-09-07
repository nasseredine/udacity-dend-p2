import configparser


# CONFIG
config = configparser.ConfigParser()
config.read('dwh.cfg')

# DROP TABLES

staging_events_table_drop = "DROP TABLE IF EXISTS staging_events;"
staging_songs_table_drop = "DROP TABLE IF EXISTS staging_songs;"
songplay_table_drop = "DROP TABLE IF EXISTS songplays;"
user_table_drop = "DROP TABLE IF EXISTS users;"
song_table_drop = "DROP TABLE IF EXISTS songs;"
artist_table_drop = "DROP TABLE IF EXISTS artists;"
time_table_drop = "DROP TABLE IF EXISTS time;"

# CREATE TABLES

staging_events_table_create= ("""
CREATE TABLE IF NOT EXISTS staging_events (
    artist_name VARCHAR,
    auth VARCHAR(10),
    user_first_name VARCHAR,
    user_gender CHAR(1),
    item_in_session INTEGER,
    user_last_name VARCHAR,
    song_duration NUMERIC(9,5),
    user_membership_level CHAR(4),
    artist_location VARCHAR,
    method CHAR(3),
    page VARCHAR(16),
    registration BIGINT,
    session_id INTEGER,
    song_title VARCHAR,
    status CHAR(3),
    ts BIGINT,
    user_agent VARCHAR,
    user_id INTEGER
);
""")

staging_songs_table_create = ("""
CREATE TABLE IF NOT EXISTS staging_songs (
    num_songs INTEGER,
    artist_id CHAR(18),
    artist_latitude NUMERIC(8,5),
    artist_longitude NUMERIC(8,5),
    artist_location VARCHAR,
    artist_name VARCHAR,
    song_id CHAR(18),
    title VARCHAR,
    duration NUMERIC(9,5),
    year INTEGER
);
""")

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplays (
    songplay_id INT IDENTITY(0,1) PRIMARY KEY,
    start_time timestamp NOT NULL REFERENCES time(start_time),
    user_id INTEGER NOT NULL REFERENCES users(user_id),
    user_membership_level CHAR(4),
    song_id CHAR(18) NOT NULL REFERENCES songs(song_id),
    artist_id CHAR(18) NOT NULL REFERENCES artists(artist_id),
    session_id INTEGER,
    location VARCHAR,
    user_agent VARCHAR
);
""")

user_table_create = ("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    first_name VARCHAR,
    last_name VARCHAR,
    gender CHAR(1),
    membership_level CHAR(4)
);
""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS songs (
    song_id CHAR(18) PRIMARY KEY,
    title VARCHAR,
    artist_id CHAR(18) NOT NULL REFERENCES artists(artist_id),
    year INTEGER,
    duration NUMERIC(9,5)
);
""")

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artists (
    artist_id CHAR(18) PRIMARY KEY,
    name VARCHAR,
    location VARCHAR,
    latitude NUMERIC(8,5),
    longitude NUMERIC(8,5)
);
""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS time (
    start_time timestamp PRIMARY KEY,
    hour INTEGER,
    day INTEGER,
    week INTEGER,
    month INTEGER,
    year INTEGER,
    weekday INTEGER
);
""")

# STAGING TABLES

staging_events_copy = ("""
""").format()

staging_songs_copy = ("""
""").format()

# FINAL TABLES

songplay_table_insert = ("""
""")

user_table_insert = ("""
""")

song_table_insert = ("""
""")

artist_table_insert = ("""
""")

time_table_insert = ("""
""")

# QUERY LISTS

create_table_queries = [staging_events_table_create, staging_songs_table_create, songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [staging_events_table_drop, staging_songs_table_drop, songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
copy_table_queries = [staging_events_copy, staging_songs_copy]
insert_table_queries = [songplay_table_insert, user_table_insert, song_table_insert, artist_table_insert, time_table_insert]
