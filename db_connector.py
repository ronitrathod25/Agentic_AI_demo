# Handles the connection to the MySQL database.
import mysql.connector

def get_db_connection():
    """Establishes and returns a connection to the SIH database."""
    connection = mysql.connector.connect(
        host="ronits-macbook-air",
        user="ronit", # Replace with your MySQL username
        password="Ronit", # Replace with your MySQL password
        database="sih_data"
    )
    return connection