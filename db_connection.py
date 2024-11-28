import pyodbc

def get_db_connection():
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=127.0.0.1,1433;'
        'DATABASE=3110DEMO;'
        'UID=sa;'
        'PWD=!QAZ2wsx;'
    )
    return conn