# Setup Postgres database connection
import psycopg2
from urllib.parse import quote

# Step1 : Manual configuration
PG_PORT = "5432"
PG_DB = "projects_db"
PG_USER = "postgres"
PG_HOST ="localhost"
PG_PASSWORD_RAW = "admin1411"
PG_PASSWORD = quote(PG_PASSWORD_RAW)

# Step2 : URL connection
POSTGRES_URL = f"postgresql://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{PG_DB}"
print("Connecting to:", POSTGRES_URL.replace(PG_PASSWORD, "****"))

#Step 3: Connect to database
conn = psycopg2.connect(POSTGRES_URL)
cursor = conn.cursor()
print("Connected successfully to PostgreSQL.")

#Step 4: Create table
create_table_query = """
CREATE TABLE events (
    event_id SERIAL PRIMARY KEY,
    event_name VARCHAR(100),
    event_date DATE,
    location VARCHAR(100)
);
"""
cursor.execute(create_table_query)
conn.commit()
print("Table 'events' created (if not exists).")

create_table_query = """
CREATE TABLE guests (
    guest_id SERIAL PRIMARY KEY,
    event_id INT REFERENCES events(event_id),
    name VARCHAR(100),
    email VARCHAR(100),
    rsvp_status VARCHAR(10),
    UNIQUE (event_id, email)
);
"""
cursor.execute(create_table_query)
conn.commit()
print("Table 'guests' created (if not exists).")

