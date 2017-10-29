import configparser

from bulbs.components import db


def write_sql_config(dbname, dbuser, dbpass, dbport):
    """Write the database configuration to file sql.conf."""
    config = configparser.RawConfigParser()
    config.add_section("auth")
    config.set("auth", "name", dbname)
    config.set("auth", "user", dbuser)
    config.set("auth", "pass", dbpass)
    config.set("auth", "port", dbport)
    with open("sql.cfg", "w") as configfile:
        config.write(configfile)

        
def database_setup(dbtype, dbname, dbuser, dbpass, dbport):
    """Setup the database."""
    tables = [
        #sqlite3"CREATE TABLE IF NOT EXISTS bulbs_category (id INTEGER PRIMARY KEY AUTOINCREMENT ,title varchar(64),description text,date timestamp without time zone,ip varchar(20),slug varchar(256))",
        "CREATE TABLE IF NOT EXISTS bulbs_category (id SERIAL, title varchar(64), description text, date timestamp without time zone, ip varchar(20), slug varchar(256))",
        "CREATE TABLE IF NOT EXISTS bulbs_group (id SERIAL, permission smallint, name varchar(32), description varchar(256))",
        "CREATE TABLE IF NOT EXISTS bulbs_moderator (subcat_id smallint, user_id smallint, username varchar(36))",
        "CREATE TABLE IF NOT EXISTS bulbs_post (id SERIAL, subcategory_id integer, user_id integer, parent_post integer, title varchar(90), content text, ispoll boolean, date timestamp without time zone, ip varchar(20), latest_reply timestamp without time zone, islocked boolean, slug varchar(256))",
        "CREATE TABLE IF NOT EXISTS bulbs_postview (post_id integer, views integer)",
        "CREATE TABLE IF NOT EXISTS bulbs_subcategory (id SERIAL, category_id integer, title varchar(45), description text, date timestamp without time zone, ip varchar(20), slug varchar(256))",
        "CREATE TABLE IF NOT EXISTS bulbs_user (id SERIAL, username varchar(36), password bytea, email varchar(128), date timestamp without time zone, karma float, ip varchar(20), title varchar(128), name varchar(64), city varchar(64), state varchar(64), country varchar(64), biography text, avatar varchar(256), group_id smallint)"
    ]
    
    if dbtype == "sqlite3":
        import sqlite3
        con = sqlite3.connect("bulbs.db")
        
    elif dbtype == "postgresql":
        import psycopg2
        try:
            con = psycopg2.connect(
                database=dbname, user=dbuser,
                password=dbpass, port=dbport)
        except Exception as e:
            raise Exception(e)
            #raise Exception(psycopg2.errorcodes.lookup(e.pgcode))
            
            write_sql_config(dbname, dbuser, dbpass, dbport)
            
    for c in tables:
        cursor = con.cursor()
        cursor.execute(c)
    
    con.commit()
    
    return True
