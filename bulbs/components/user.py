from bulbs.components import db
from bulbs.components.auth import generate_password

def username_from_id(user_id):
    """Return the username corresponding to the user id."""
    try:
        cursor = db.con.cursor()
        cursor.execute(
            "SELECT username FROM bulbs_User WHERE id = %s", (user_id, ))        
        username = cursor.fetchone()[0]
    except Exception as e:
        raise ValueError("failed to get username, ", e)
        
    return username
    
def register_user(group_id, username, password, email, ip):
    """Insert a user into the database."""
    cursor = db.con.cursor()
    hashed_password = generate_password(password)
    try:
        cursor.execute(
            "INSERT INTO bulbs_user (username, password, email, ip, date, karma, title, group_id) \
             VALUES (%s, %s, %s, %s, now(), %s, %s, %s)",
             (username, hashed_password, email, ip, 0, "Newbie", group_id))
    except psycopg2.DataError as e:
        cursor.execute("rollback")
        return False
        
    db.con.commit()
    
    return True
    
def username_taken(username):
    """Check if the username already exists in the database and return a boolean."""
    cursor = db.con.cursor()
    cursor.execute(
        "SELECT id FROM bulbs_user WHERE lower(username) = %s", 
         (username.lower(), ))
    try:
        data = cursor.fetchone()[0]
    except TypeError:
        return False    # Username doesn't exist.
        
    return True