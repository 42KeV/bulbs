from bulbs.components import db

import bcrypt


def checkpw(username, password):
    cursor = db.con.cursor()

    try:
        cursor.execute("SELECT password FROM bulbs_user WHERE lower(username) = %s", (username.lower(), ))
        stored_password = cursor.fetchone()[0].tobytes()
    except (IndexError, TypeError):
        # specified user doesn't exist
        return False

    try:
        password_match = bcrypt.hashpw(
            bytes(password, encoding="utf-8"), stored_password) == stored_password
        if not password_match:
            raise ValueError
    except ValueError:
        return False

    return True
    

def whois(username):
    cursor = db.con.cursor()
    
    try:
        cursor.execute(
            "SELECT id, username, group_id FROM bulbs_user WHERE lower(username) = %s", 
            (username.lower(), ))
        data = cursor.fetchone()
        userinfo = dict(id=data[0], username=data[1], group_id=data[2])
    except TypeError:
        # username specified doesn't exist
        return None

    return userinfo

def authorize(username, password):
    '''
    Takes plaintext arguments and returns a dictionary object with the keys `success` and `session`. 
    If the login arguments match that of the database, `success` will have a value of True and `session` will have `UserSession` class.
    '''
    cursor = db.con.cursor()
    
    try:
        cursor.execute("SELECT password FROM bulbs_user WHERE username = %s", (username, ))
        stored_password = cursor.fetchone()[0].tobytes()
    except (IndexError, TypeError):
        # Specified user doesn't exist
        return dict(
            sucess=False,
            session=None
        )

    try:
        password_match = bcrypt.hashpw(
            bytes(password, encoding="utf-8"), stored_password) == stored_password
            
        if not password_match:
            # Password doesn't match what's in the DB
            raise ValueError
    except ValueError as e:
        return dict(
            success=False,
            session=None
        )

    cursor.execute("SELECT id FROM bulbs_User WHERE username = %s", (username, ))
    user_id = cursor.fetchone()[0]
    
    #cursor.execute("SELECT group_id FROM bulbs_User WHERE username = %s", (username, ))
    #group_id = cursor.fetchone()[0]
    
    return dict(
        success=True,
        session=UserSession(username, user_id, group_id)
    )

