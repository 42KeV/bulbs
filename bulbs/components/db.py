import configparser
import psycopg2


con = None

def init():
    '''Initializes the db connection and makes it available globally'''
    config = configparser.RawConfigParser()
    config.read("sql.cfg")
    
    global con
    con = psycopg2.connect(
        database=config.get("auth", "name"), user=config.get("auth", "user"), 
        password=config.get("auth", "pass"), port=config.get("auth", "port")
    )
