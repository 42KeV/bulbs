from bulbs.resources import connection

import bcrypt

class UserSession(object):
    def __init__(self, username=None, id=None, group_id=None):#, authorized=False):
        self.username = username
        self.id = id
        self.group_id = group_id
        
    def is_mod(self):
        pass
        
    def is_admin(self):
        pass
        
    def is_banned(self):
        pass
             

def generate_password(pt_password):
    twelve = 12
    salt = bcrypt.gensalt(twelve);
    
    pt_password = bytes(pt_password, encoding="utf-8")
    hashed_password = bcrypt.hashpw(pt_password, salt)
    
    return hashed_password

def authorize(username, password):
    cursor = connection.con.cursor()
    
    try:
        cursor.execute("SELECT password FROM bulbs_user WHERE username = %s", (username, ))
        stored_password = cursor.fetchone()[0].tobytes()
    except IndexError:
        # specified user doesn't exist
        return dict(
            sucess=False,
            session=None
        )

    if not bcrypt.hashpw(
        bytes(password, encoding="utf-8"), stored_password) == stored_password:
        # failure to authenticate
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

