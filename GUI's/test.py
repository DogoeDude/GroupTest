import mysql.connector

# Your database connection details
DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "password"
DB_DATABASE = "finproj_dbgui"

# Database connection
try:
    conn = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_DATABASE
    )

    cursor = conn.cursor()

    # Example query
    query = "SELECT * FROM loginfo"

    cursor.execute(query)

    # Fetch and print the result
    result = cursor.fetchall()

    if result:
        for row in result:
            print("Column1:", row[0], "Column2:", row[1])
    else:
        print("No rows found.")

except mysql.connector.Error as e:
    print(f"Error: {e}")

finally:
    # Close the cursor and connection
    if cursor:
        cursor.close()
    if conn:
        conn.close()
