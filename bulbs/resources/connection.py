import configparser
import psycopg2


con = None

def init():
    """ make the database connection available globally; initialize connection """
    config = configparser.RawConfigParser()
    config.read("sql.cfg")
    
    global con
    con = psycopg2.connect(
        database=config.get("auth", "name"), user=config.get("auth", "user"), 
        password=config.get("auth", "pass"), port=config.get("auth", "port")
    )
