import sqlite3

def initialize_db():
    conn = sqlite3.connect('measurements.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS measurements
                (uuid TEXT PRIMARY KEY NOT NULL,
				id TEXT,
                temperature INTEGER,
                humidity INTEGER,
                timestamp INTEGER,
              	red INTEGER,
              	green INTEGER,
              	blue INTEGER);''')
    conn.commit()
    conn.close()


def add_row(uuid: str, id: str, timestamp: int , temp: int,
            humidity: int, red: int, green: int, blue: int):
    conn = sqlite3.connect('measurements.db')
    c = conn.cursor()
    c.execute("INSERT INTO measurements (uuid, id, temperature, humidity, timestamp, red, green, blue) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
              (uuid, id, temp, humidity, timestamp, red, green, blue))
    conn.commit()
    conn.close()


def delete_row(row_uuid):
    conn = sqlite3.connect('measurements.db')
    c = conn.cursor()
    c.execute("DELETE FROM measurements WHERE uuid = ?", (row_uuid,))
    conn.commit()
    conn.close()

def get_array_from_db():
    conn = sqlite3.connect('./measurements.db')
    cursor = conn.cursor()

    # Execute query to fetch array of integers
    cursor.execute("SELECT humidity FROM *")
    rows = cursor.fetchall()

    # Process retrieved data into an array of integers
    int_array = [row[0] for row in rows]

    # Close the database connection
    conn.close()

    return int_array

# tbd ??

# def fetch_row_by_uuid(row_uuid):
#     conn = sqlite3.connect('measurements.db')
#     c = conn.cursor()
#     c.execute("SELECT status, content FROM users WHERE uuid = ?", (row_uuid,))
#     row = c.fetchone()
#     conn.close()
#     if row is None:
#         return None  # Return None if no row is found
#     else:
#         return int(row[0]), row[1]  # Return status and content as a dictionary


# def update_single_column(row_uuid, column_name, new_value):
#     conn = sqlite3.connect('generations.db')
#     c = conn.cursor()
#     # Use parameterized query to update the specified column
#     query = f"UPDATE users SET {column_name} = ? WHERE uuid = ?"
#     c.execute(query, (new_value, row_uuid))
#     conn.commit()
#     conn.close()
