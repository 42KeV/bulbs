import configparser


con = None

def init_sqlite3():
    """Initialize the db connection and make it available globally."""
    import sqlite3
    global con
    
    con = sqlite3.connect("bulbs.db", check_same_thread=False)

def init_postgresql():
    """Initialize the db connection and make it available globally."""
    import psycopg2
    global con
    
    config = configparser.RawConfigParser()
    config.read("sql.cfg")
    con = psycopg2.connect(
        database=config.get("auth", "name"), user=config.get("auth", "user"), 
        password=config.get("auth", "pass"), port=config.get("auth", "port")
    )