# Contains the core logic for database interactions.
import db_connector
from datetime import datetime # 1. Import the datetime library

def add_waste_record(user_id, object_name, metallic_load, moisture, gas_percent, category_id):
    """Inserts a new waste data record into the database."""
    conn = db_connector.get_db_connection()
    cursor = conn.cursor()
    
    # 2. Add 'record_time' to the SQL query
    sql = """
    INSERT INTO waste_data 
    (user_id, object_name, record_time, metallic_load, moisture, gas_percent, category_id) 
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    
    current_time = datetime.now() # Get the current timestamp
    
    # 3. Add the timestamp to the values tuple
    val = (user_id, object_name, current_time, metallic_load, moisture, gas_percent, category_id)
    
    cursor.execute(sql, val)
    conn.commit()
    conn.close()
    print("Waste record added.")

def get_records_by_user(user_id):
    """Retrieves all waste records for a specific user, joining table names."""
    conn = db_connector.get_db_connection()
    cursor = conn.cursor(dictionary=True)
    sql = """
    SELECT wd.object_name, wd.record_time, wc.category_name
    FROM waste_data wd
    JOIN waste_categories wc ON wd.category_id = wc.category_id
    WHERE wd.user_id = %s
    """
    cursor.execute(sql, (user_id,))
    results = cursor.fetchall()
    conn.close()
    return results