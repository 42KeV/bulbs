from bulbs.components import db

import bcrypt

class UserSession(object):
    def __init__(self, username=None, id=None, group_id=None):
        self.username = username
        self.id = id
        self.group_id = group_id
        
    def is_mod(self):
        pass
        
    def is_admin(self):
        pass
        
    def is_banned(self):
        pass


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
    
    cursor.execute("SELECT group_id FROM bulbs_User WHERE username = %s", (username, ))
    group_id = cursor.fetchone()[0]
    
    return dict(
        success=True,
        session=UserSession(username, user_id, group_id)
    )

